## Help Center


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/5fe0ed82-1beb-428d-9c0c-a34dc950d863

### Process
- Users can submit support tickets and view all their tickets with current status

### File Path
- Page
  - Support Ticket - `src/pages/dashboard/help/user.tsx`
- Components
  - Support Form - `src/components/Services/SupportTicket/Contact/ContactForm.tsx`
  - Support Tickets List - `src/components/Services/SupportTicket/UserTickets/index.tsx`
  - Support Ticket Details - `src/components/Services/SupportTicket/UserTickets/Ticket.tsx`

- API Service
  - Support Service - `src/services/HelpService.tsx`

### Component Description
  - Support Form - Allows users to submit tickets with their phone number, type of issue, subject and detailed description
  - Support Tickets List - Displays all support tickets submitted by the user
  - Support Ticket Details - Shows complete ticket information including current status
