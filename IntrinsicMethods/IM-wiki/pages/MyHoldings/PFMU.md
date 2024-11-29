## PFMU (Personal Financial Management Unit Holdings)

![Screenshot from 2024-04-03 18-18-37](https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/2b02da48-048f-4166-9aef-c433512bd718)


### Process
- Users can view their complete PFMU portfolio and initiate swaps by selecting the swap option

### File Path
- Page
  - PFMU - `src/pages/dashboard/portfolio/pfmu.tsx`
- Components
  - Empty Content - `src/components/Molecules/EmptyContent/EmptyContent.tsx`
  - PFMUCard - `src/components/Templates/Holdings/List/PFMUCard.tsx`

- Api Service
  - PFMU Service - `src/services/PFMUService.tsx`

### Component Detail
  - Empty Content - Displays when no holdings are present
  - PFMUCard - Renders individual PFMU holdings with project imagery, holding details and issue year
