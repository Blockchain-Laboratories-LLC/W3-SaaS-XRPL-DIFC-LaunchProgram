## Account


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/c9deb85b-4a8c-4175-867b-7ac5a886100c



### Process
- This section allows users to manage their account information, view wallet details, and access their complete transaction history

### File Path
- Page
  - Account - `src/pages/dashboard/accounts/[id]/index.tsx`
- Components
  - Account Detail - `src/components/Services/Account/AddEdit/AccountIndividual.tsx`
  - Account Wallet - `src/components/Services/Account/AddEdit/AccountWallet.tsx`
  - Payment Methods - `src/components/Services/Account/List/PaymentMethods.tsx`
  - Transaction History - `src/components/Services/Account/List/TransactionHistory.tsx`

- Api Service
  - Onboarding Service - `src/services/OnboardingService.tsx`
  - Account Service - `src/services/AccountService.tsx`

### Component Detail
  - Account Detail - Displays and enables modification of user profile information
  - Account Wallet - Provides a view of the account's wallet information
  - Payment Methods - Displays available wallet options, enables default wallet selection and connection of existing wallets
  - Transaction History - Displays a comprehensive record of transactions for the default wallet
