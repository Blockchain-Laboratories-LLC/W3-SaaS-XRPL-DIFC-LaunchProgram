FMU Holdings Overview

![Screenshot from 2024-04-03 18-14-05](https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/74a58189-f36d-4952-b5b0-cb83b2402c8a)

### Process
- This page displays a user's FMU portfolio, allowing them to either retire holdings or list them for sale via dedicated action buttons

### File Path
- Page
  - FMU - `src/pages/dashboard/portfolio/fmu.tsx`
- Components
  - Empty Content - `src/components/Molecules/EmptyContent/EmptyContent.tsx`
  - FMUCard - `src/components/Templates/Holdings/List/FMUCard.tsx`

- Api Service
  - Credit Service - `src/services/CreditService.tsx`

### Component Detail
  - Empty Content - Component for rendering empty state view
  - FMUCard - Card component that displays project details including image, FMU quantity and vintage year
