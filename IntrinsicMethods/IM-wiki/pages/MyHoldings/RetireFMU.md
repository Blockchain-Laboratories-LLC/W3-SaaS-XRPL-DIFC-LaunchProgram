## Retire FMU


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/72deec85-cc2a-42a7-8503-b41fcef4fa93



### Process
- Users specify the FMU amount they want to retire and provide a name for the certificate
- After entering the required information, users can preview their certificate
- Authentication is required to complete the transaction
- Upon successful retirement, users have the option to share on social media

### File Path
- Page
  - Retire - `src/pages/dashboard/portfolio/[id]/retire.tsx`
- Components
  - Side by Side Retire - `src/components/Templates/SideBySide/SideBySideRetire`
  - LeftSideRetire - `src/components/Templates/SideBySide/LeftSideRetire`
  - RightSideService - `src/components/Templates/SideBySide/RightSideRetire`
  - CheckOutSteps - `src/components/Templates/SideBySide/CheckoutSteps.js`
  - CreateCertificate - `src/components/Services/Retire/CreateCertificate.tsx`
  - Canvas - `src/components/Atoms/Canvas/Canvas.tsx`
  - PreviewCertificate - `src/components/Services/Retire/PreviewCertificate.tsx`
  - RetireSuccess - `src/components/Services/Retire/RetireSuccess.tsx`
  - Tx Result - `src/components/Services/Project/Tokenize/TxResult.tsx`
  - Full RetireSummary - `src/components/Services/Retire/FullRetireSummary.tsx`
  - RetireSummaryPreview - `src/components/Services/Retire/RetireSummaryReview.tsx`
  - ClaimRetire - `src/components/Services/Retire/ClaimRetire.tsx`
  - Palisade Txn - `src/components/Services/Project/Admin/Authenticator.tsx`
  - Xumm Txn - `src/components/Organisms/WalletProvider/transaction/XummTxn.tsx`
  - Download Certificate - `src/components/Services/Retire/DownloadCertificate.tsx`
  - Social Share - `src/components/Atoms/Share/SocialShare.tsx`

- Api Service
  - Project Service - `src/services/ProjectService.tsx`
  - Upload Service - `src/services/UploadService.tsx`
  - Retire Fmu Service - `src/services/RetireFmuService.tsx`
  - SurveyService - `src/services/SurveyService.tsx`

### Component Detail
  - Side by Side Retire - Displays retirement process steps in a side-by-side layout
  - LeftSideRetire - Renders the left panel components of the retirement process
  - RightSideService - Renders the right panel components of the retirement process
  - CheckOutSteps - Displays process steps with text and checkmark indicators
  - CreateCertificate - Generates certificates based on user input
  - Canvas - Converts HTML elements into certificate images
  - PreviewCertificate - Displays certificate preview
  - RetireSuccess - Shows retirement confirmation message
  - Tx Result - Displays transaction details with Bithomp Explorer link
  - Full RetireSummary - Contains user information and input fields for FMU amount and certificate name
  - RetireSummaryPreview - Displays retirement details for verification
  - ClaimRetire - Handles wallet-specific authentication
  - Palisade Txn - Provides OTP authentication interface for Palisade transactions
  - Xumm Txn - Displays QR code for Xumm wallet authentication
  - Download Certificate - Renders the complete certificate with all details
  - Social Share - Enables sharing via social media platforms
