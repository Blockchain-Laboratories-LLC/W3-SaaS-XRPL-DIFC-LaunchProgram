import xrpl 
from xrpl.clients import JsonRpcClient 
from xrpl.wallet import generate_faucet_wallet 
from xrpl.models.transactions import AccountSet, TrustSet, Payment
from xrpl.transaction import autofill_and_sign, submit_and_wait 
from xrpl.models.transactions import AccountSetAsfFlag 
from xrpl.models.requests import AccountLines

class XRPLTokenManager:
    def __init__(self, client, currency_code, token_limit):
        self.client = client
        self.currency_code = currency_code
        self.token_limit = token_limit
        self.issuer_wallet = None
        self.user_wallets = []
        self.transaction_urls = []

    def generate_transaction_url(self, tx_hash):
        """
        Generate URL for transaction on XRPL test explorer
        
        :param tx_hash: Transaction hash
        :return: Explorer URL for the transaction
        """
        return f"https://test.xrplexplorer.com/explorer/{tx_hash}"

    def generate_wallets(self, num_users):
        """
        Generate wallets for issuer and specified number of users
        
        :param num_users: Number of user wallets to generate
        :return: List of all generated wallets
        """
        # Reset transaction URLs
        self.transaction_urls = []

        # Generate issuer wallet
        self.issuer_wallet = generate_faucet_wallet(self.client)
        
        # Generate user wallets
        self.user_wallets = [
            generate_faucet_wallet(self.client) 
            for _ in range(num_users)
        ]
        
        # Print wallet addresses
        print(f"Issuer Wallet: {self.issuer_wallet.classic_address}")
        for i, wallet in enumerate(self.user_wallets, 1):
            print(f"User Wallet {i}: {wallet.classic_address}")
        
        return [self.issuer_wallet] + self.user_wallets

    def setup_token_issuance(self):
        """
        Setup token issuance process for all users
        """
        if not self.issuer_wallet or not self.user_wallets:
            raise ValueError("Wallets must be generated first")

        # Step 1: Enable Require Auth Flag on Issuer Account 
        set_flag_tx = AccountSet( 
            account=self.issuer_wallet.classic_address, 
            set_flag=AccountSetAsfFlag.ASF_REQUIRE_AUTH 
        ) 
        signed_set_flag_tx = autofill_and_sign(set_flag_tx, self.client, self.issuer_wallet) 
        response = submit_and_wait(signed_set_flag_tx, self.client) 
        print(f"Require Auth flag enabled. Transaction Hash: {response.result['hash']}")
        self.transaction_urls.append(self.generate_transaction_url(response.result['hash']))

        # Step 2 & 3: Create and Authorize Trust Lines 
        for user in self.user_wallets:
            # User creates trust line
            trust_set_user_tx = TrustSet( 
                account=user.classic_address, 
                limit_amount={
                    "currency": self.currency_code, 
                    "value": self.token_limit, 
                    "issuer": self.issuer_wallet.classic_address
                }, 
            ) 
            signed_trust_set_user_tx = autofill_and_sign(trust_set_user_tx, self.client, user) 
            response = submit_and_wait(signed_trust_set_user_tx, self.client) 
            print(f"Trust line created for {user.classic_address}. Transaction Hash: {response.result['hash']}")
            self.transaction_urls.append(self.generate_transaction_url(response.result['hash']))

            # Issuer authorizes trust line
            trust_set_issuer_tx = TrustSet( 
                account=self.issuer_wallet.classic_address, 
                limit_amount={
                    "currency": self.currency_code, 
                    "value": "0", 
                    "issuer": user.classic_address
                }, 
                flags=0x00010000  # tfSetfAuth 
            ) 
            signed_trust_set_issuer_tx = autofill_and_sign(trust_set_issuer_tx, self.client, self.issuer_wallet) 
            response = submit_and_wait(signed_trust_set_issuer_tx, self.client) 
            print(f"Trust line authorized for {user.classic_address}. Transaction Hash: {response.result['hash']}")
            self.transaction_urls.append(self.generate_transaction_url(response.result['hash']))

    def issue_tokens(self, token_amount="10"):
        """
        Issue tokens to all users
        
        :param token_amount: Amount of tokens to issue to each user
        """
        for user in self.user_wallets:
            payment_tx = Payment( 
                account=self.issuer_wallet.classic_address, 
                destination=user.classic_address, 
                amount={
                    "currency": self.currency_code, 
                    "value": token_amount, 
                    "issuer": self.issuer_wallet.classic_address
                }, 
            ) 
            signed_payment_tx = autofill_and_sign(payment_tx, self.client, self.issuer_wallet) 
            response = submit_and_wait(signed_payment_tx, self.client) 
            print(f"Tokens issued to {user.classic_address}. Transaction Hash: {response.result['hash']}")
            self.transaction_urls.append(self.generate_transaction_url(response.result['hash']))

    def get_token_balances(self):
        """
        Retrieve token balances for all users
        
        :return: Dictionary of user balances
        """
        balances = {}
        for user in self.user_wallets:
            request = AccountLines(
                account=user.classic_address,
                peer=self.issuer_wallet.classic_address
            )
            response = self.client.request(request)
            
            for line in response.result.get('lines', []):
                if (line['currency'] == self.currency_code and 
                    line['account'] == self.issuer_wallet.classic_address):
                    balances[user.classic_address] = line['balance']
                    break
        
        return balances

    def print_transaction_urls(self):
        """
        Print all transaction URLs
        """
        print("\nTransaction URLs:")
        for i, url in enumerate(self.transaction_urls, 1):
            print(f"{i}. {url}")

def main():
    # Connect to XRPL testnet 
    client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

    # Token Details 
    CURRENCY_CODE = "STO" 
    TOKEN_LIMIT = "1000" 
    NUM_USERS = 3  # Dynamically set number of users

    # Create token manager
    token_manager = XRPLTokenManager(client, CURRENCY_CODE, TOKEN_LIMIT)

    # Generate wallets for issuer and users
    token_manager.generate_wallets(NUM_USERS)

    # Setup token issuance
    token_manager.setup_token_issuance()

    # Issue tokens
    token_manager.issue_tokens()

    # Retrieve and display token balances
    print("\nToken Balances:")
    balances = token_manager.get_token_balances()
    for user_address, balance in balances.items():
        print(f"User {user_address}: {balance} {CURRENCY_CODE} tokens")

    # Print transaction URLs
    token_manager.print_transaction_urls()

    print("\nSTO Issue with Authorized Trust Lines Completed Successfully!")

# Run the main function
if __name__ == "__main__":
    main()