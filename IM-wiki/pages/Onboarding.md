## Onboarding

### Process
- During onboarding, users must complete their full account details
- Users have the option to create a new wallet through custody or connect using Xaman
- KYC verification requires government-issued ID (passport or driver's license)

### File Path
- Page
  - onboarding - `src/pages/auth/onboarding.tsx`
- Components
  - IndividualStepper Form - `src/components/Auth/forms/IndivisualStepper.tsx`
  - Individual Form - `src/components/Auth/forms/AIndividualForm.tsx`
  - Profile Form - `src/components/Auth/forms/AProfileForm.tsx`
  - Veriff Form - `src/components/Auth/forms/VeriffForm.tsx`
  - Wallet Form - `src/components/Services/Wallet/AddEdit/AWalletCreateForm.tsx`
  - Xaman Login Form - `src/components/Organisms/WalletProvider/connect/XummLogin.tsx`
  - Xaman QR Code Scanner - `src/components/Organisms/WalletProvider/connect/XummSigninQRWS/XummSigninQRWS.tsx`
  - Palisade Login Form - `src/components/Organisms/WalletProvider/connect/PalisadeLogin.tsx`
  - Palisade QR Code Scanner - `src/components/Organisms/WalletProvider/connect/PalisadeSigninQr/PalisadeSigninQr.tsx`
  - OTP Form - `src/components/Organisms/Otp'

- Api Service
  - Onboarding - `src/services/OnboardingService`
  - Upload Service - `src/services/UploadService`
  - Palisade - `srv/services/PalisadeService`

### Component Detail
  - IndividualStepper Form - Contains four sequential onboarding sections
  - Individual Form - Collects user contact information including phone and address
  - Profile Form - Handles profile photo upload and display name entry
  - Veriff Form - Manages user KYC verification through Veriff
  - Wallet Form - Presents wallet options between Xumm and custody wallet
  - Xaman Login Form - Facilitates wallet connection through Xaman mobile app
  - Xaman QR Code Scanner - Displays QR code for mobile app scanning
  - Palisade Login Form - Creates Palisade account with authentication via Google/Microsoft auth
  - Palisade QR Code Scanner - Generates QR code for authenticator app scanning
  - OTP Form - Validates OTP from authenticator app
