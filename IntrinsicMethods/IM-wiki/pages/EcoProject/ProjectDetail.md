## Eco Project Detail


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/e8751deb-694e-435b-a47a-d9617038aa9e

### Process
- Users can view detailed information about any eco project by selecting it from the list.

### File Path
- Page
  - detail - `src/pages/dashboard/projects/[id]/detail.tsx`
- Components
  - Header - `src/components/Services/Project/Detail/Header.tsx`
  - Overview - `src/components/Services/Project/Detail/Overview.tsx`
  - Profile Status - `src/components/Services/Project/Detail/ProfileStatus.tsx`
  - DEX - `src/components/Dex/Dex.tsx`
  - Detail - `src/components/Services/Project/Detail/Details.tsx`
  - Co Benefits - `src/components/Services/Project/Detail/CoBenefits.tsx`
  - Order Tickets - `src/components/Services/Project/Detail/OrderTickets.tsx`
  - Transaction History - `src/components/Services/Project/Detail/TransactionHistory.tsx`

- Api Service
  - Project Service - `src/services/ProjectService.ts`
  - Project Wallet Balance - `src/services/ApiService.ts`
  - Order Ticket Service - `src/services/OrderTicketService.ts`

### Component Detail
  - Header - Displays the eco project's header image
  - Overview - Presents key project metrics including pfmuIssued, fmuIssued, fmu retired, total acres, proposed trees, and planted trees
  - Profile Status - Indicates the current project profile status, such as Pre Purchase FMUs Minted
  - DEX - Facilitates decentralized exchange between fmus, pfmus and other currencies
  - Detail - Contains project description and core carbon principles
  - Co Benefits - Presents a comprehensive list of co-benefits
  - Order Tickets - Displays all order-related activities like account activation and NFT minting
  - Transaction History - Provides a record of all project-related transactions
