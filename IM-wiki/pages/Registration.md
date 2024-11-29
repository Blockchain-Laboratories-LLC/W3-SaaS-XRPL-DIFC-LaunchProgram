## Registration


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/4d44675c-590c-4a3c-891b-6676151d498f

### Process
- Users select whether they want a Business or Individual account type
- Users provide registration details including name, email and password
- After successful registration, the system requests device fingerprint data to store for security purposes

### File Path
- Page
  - register - `src/pages/auth/register.tsx`
- Components
  - Customer Form - `src/components/Auth/forms/CustomerForm.tsx`
  - Register Form - `src/components/Auth/forms/RegisterForm.tsx`
  - Device Finger Print - `src/components/Auth/forms/AddFingerPrintForm.tsx`
- Api Service
  - Register - `src/services/AuthService.ts`
  - Device Finger Print - `src/services/SecurityService.tsx`
  - CSRF Token - `src/services/SecurityService.tsx`

### Component Detail
  - Customer Form - Allows selection of account type
  - Register Form - Captures user's name, email and password information
  - Device Finger print - Prompts for device information after registration completion
