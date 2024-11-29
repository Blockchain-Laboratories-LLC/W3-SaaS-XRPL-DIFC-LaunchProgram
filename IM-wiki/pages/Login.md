## Login


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/73876ff6-81ba-4fe7-94da-5e5690f1cae1

### Process
- Users provide their email and password for authentication
- The system validates both the provided credentials and checks for device registration
- When an unregistered device is detected, users must complete device registration before continuing
- Password recovery is available through the "Forgot Password" feature for users who need to reset their credentials

### File Path
- Page
  - login - `src/pages/auth/login.tsx`
- Components
  - Login Form - `src/components/Auth/forms/LoginForm.tsx`
  - Device Finger Print - `src/components/Auth/forms/ResetFingerPrintDeviceForm.tsx`
  - OTP Form - `src/components/Organisms/Otp/OtpForm.tsx`
  - Forgot Password - `src/components/Auth/forms/ForgotForm.tsx`
- Api Service
  - Login - `src/services/AuthService.ts`
  - Device Finger Print - `src/services/SecurityService.tsx`
  - CSRF Token - `src/services/SecurityService.tsx`

### Component Detail
  - Login Form - The authentication interface consists of email and password input fields, accompanied by a login button and password reset option
  - Device Fingerprint - Contains a single 'Add Device Fingerprint' button that captures device information and transmits it to the backend database for storage
  - OTP Form - A dedicated input component for handling one-time password verification
  - Forgot Form - Provides password recovery functionality through three fields: email, OTP verification, and new password entry

### Security
  - Auth token - Authentication credentials are maintained in browser cookies for API request authorization
  - CSRF-Token - Cross-site request forgery protection token is preserved in context for secure API communication
  - Device Fingerprint - Device identification system that restricts simultaneous multi-device access
