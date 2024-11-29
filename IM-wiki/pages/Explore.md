## Exploring Eco Projects


https://github.com/Blockchain-Laboratories-LLC/IM-Production-Frontend/assets/20131952/07fb385a-93d5-47e3-9eea-78d906a92c3e


### Functionality
- Users can browse the complete catalog of eco projects and utilize the search feature to find specific projects

### Directory Structure
- Page
  - Eco Project List - `src/pages/dashboard/projects/list.tsx`
- Components
  - Project List - `src/components/Services/Project/List/ProjectList.tsx`
  - Project Card - `src/components/Services/Project/List/ProjectCard.tsx`
  - Empty Content - `src/components/Molecules/EmptyContent/EmptyContent.tsx`
  - Project Status - `src/components/Molecules/Status/ProjectStatus.tsx`
  - Card Detail - `src/components/Molecules/Details/Details.tsx`
  - List Tool Bar - `src/components/Organisms/ListToolbar/ListToolbar.tsx`
- API Services
  - Project Service - `src/services/ProjectService.ts`
  - API Service - `src/services/ApiService.ts`
  - Survey Service - `src/services/SurveyService.ts`

### Component Overview
  - Project List - Core component that displays all eco projects
  - Project Card - Displays project imagery and key information in card format
  - Empty Content - Handles display when no content is available
  - Project Status - Indicates current project status
  - Card Detail - Presents geographical information for eco projects
  - List Tool Bar - Provides search functionality to filter projects by name
