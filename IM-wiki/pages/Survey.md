## Survey


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/4395fe69-ff71-4882-a4a2-569a3912066f


### Workflow
- Users receive a complementary badge upon survey completion
- Badge claiming requires authentication through the user's default wallet

### File Structure
- Page
  - Survey - `src/pages/dashboard/survey/index.tsx`
- Components
  - Side by Side - `src/components/Templates/SideBySide/SideBySideRetire.tsx`
  - Check Step - `src/components/Templates/SideBySide/CheckoutSteps.js`
  - Left Side Survey - `src/components/Templates/SideBySide/LeftSideSurvey.tsx`
  - Right Side Survey - `src/components/Templates/SideBySide/RightSideSurvey.tsx`
  - SurveyCerticate - `src/components/Services/Survey/SurveyCertificate.tsx`
  - SurveyCanvas - `src/components/Atoms/Canvas/SurveyCanvas.tsx`
  - Survey Sucess - `src/components/Services/Survey/SurveySuccess.tsx`
  - Survey Form - `src/components/Services/Survey/SurveyForm.tsx`
  - Survey Claim - `src/components/Services/Survey/SurveyClaimNft.tsx`
  - Palisade Txn - `src/components/Services/Project/Admin/Authenticator.tsx`
  - Xumm Txn - `src/components/Organisms/WalletProvider/transaction/XummTxn.tsx`
  - Survey Result - `src/components/Services/Survey/SurveyResult.tsx`
  - Social Share - `src/components/Atoms/Share/SocialShare.tsx`


- API Services
  - ApiService - `src/services/ApiService.tsx`
  - SurveyService - `src/services/SurveyService.tsx`

### Component Overview
  - Side by Side - Displays parallel survey badge process steps
  - Check Step - Presents progress steps with text and checkmarks
  - Left Side Survey - Renders left panel survey components
  - Right Side Survey - Renders right panel survey components
  - SurveyCerticate - Generates user survey badges
  - SurveyCanvas - Converts HTML to badge imagery
  - Survey Success - Displays completion confirmation
  - Survey Form - Facilitates user survey input
  - Survey Claim - Enables badge claiming via wallet authentication
  - Palisade Txn - OTP verification for Palisade transaction authentication
  - Xumm Txn - QR code for Xamman transaction verification
  - Survey Result - Presents survey outcomes
  - Social Share - Enables social media URL sharing
