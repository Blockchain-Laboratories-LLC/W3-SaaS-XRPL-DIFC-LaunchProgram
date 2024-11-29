## Certificates

![Screenshot from 2024-04-03 18-10-17](https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/63b00936-f865-47a3-8090-ea807e99cdff)


### Process
- This section displays all retired FMU certificates, with the option to view additional details by accessing the Bithomp explorer through the hash link

### File Path
- Page
  - Certificates - `src/pages/dashboard/portfolio/certificates.tsx`
- Components
  - Empty Content - `src/components/Molecules/EmptyContent/EmptyContent.tsx`
  - CertificateCard - `src/components/Templates/Holdings/List/CertificateCard.tsx`

- Api Service
  - Retire Service - `src/services/RetireService.tsx`

### Component Detail
  - Empty Content - Displays when no content is available
  - CertificateCard - Presents certificate images and hash values, providing links to detailed information in the Bithomp Explorer
