DEX (decentralized exchange)


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/dc4d7605-79d9-4225-9c58-6b9001a46cac



### Process
- Users can view all available buy and sell offers
- Offers can be purchased by selecting any row
- To create a buy offer, users must either enter a value manually or select from existing offers, then click the buy offer button
- If no trustline exists for the currency, one will be created before proceeding with the offer
- Transaction authentication requires either entering a code from an authenticator app (e.g. Google Authenticator) or scanning a QR code (varies by wallet type like custody or xamman)
- Trustlines can be established with any registry-owned currency
- Upon offer creation, a popup displays the transaction hash which links to the bithomp explorer for viewing transaction details

### File Path
- Page
  - detail - `src/pages/dashboard/projects/[id]/detail.tsx`
- Components
  - DEX - `src/components/Dex/Dex.tsx`
  - Order Book List - `/home/ritesh/Documents/IM-Production-Frontend/src/components/Dex/OrderBookList.tsx`
  - Order Book Row - `src/components/Dex/OrderBookRow.tsx`
  - Order Book Form - `src/components/Dex/OrderBookForm.tsx`
  - Order Success - `src/components/Dex/OrderSuccess.tsx`
  - Coming Soon - `src/components/Dex/ComingSoon.tsx`
  - Authenticator - `src/components/Services/Project/Admin/Authenticator.tsx`
  - Xamam Transaction - `src/components/Organisms/WalletProvider/transaction/XummTxn.tsx`

- Api Service
  - Project Wallet Balance - `src/services/TokenizationService.ts`
  - Dex Service - `src/services/DexService.tsx`
  - Xamam or Palisade Txn - `src/services/SurveyService.ts`

### Component Detail
  - DEX - Displays order book and order form information
  - Order Book List - Contains buy and sell offer listings
  - Order Book Row - Displays detailed row information for buy and sell offers
  - Order Book Form - Features buy/sell buttons, dropdowns for credit vintage and currency selection, and input fields for price and quantity
  - Order Success - Displays transaction hash information
  - Coming Soon - Shows a coming soon message with notify option
  - Authenticator - Provides OTP authentication interface
  - Xamam Transaction - Displays QR code for Xamam transactions

### Issues
  - Decimal multiplication and division - Frontend calculations with decimal values presented challenges. Resolved using [Decimal.js](https://mikemcl.github.io/decimal.js/) library. More details available [here](https://dev.to/rio14/front-end-dilemmas-tackling-precision-problems-in-javascript-with-decimaljs-35bl)
