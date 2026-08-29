# Asetonix

Asetonix is a web-based **Enterprise Asset Management System (EAM)** designed to help organizations manage the complete lifecycle of physical and digital assets.

The system provides centralized asset tracking, ownership, assignment, maintenance, transfers, retirement, lifecycle history, alerts, organizational tracking, and operational visibility through a custom enterprise interface.

---

## Vision

Asetonix aims to provide organizations with a structured way to answer:

- What assets does the organization own?
- Where is each asset currently located?
- Who is responsible for an assigned asset?
- What is the current condition and status of an asset?
- What happened to an asset throughout its lifecycle?
- Which assets require maintenance?
- Which assets are available, assigned, under maintenance, or retired?
- Which departments and locations are responsible for assets?
- Which users have access to specific parts of the system?

---

## Core Modules

### 1. Asset Management

Centralized management of organizational assets.

Each asset can contain information such as:

- Asset name
- Unique asset tag
- Category
- Brand
- Model
- Serial number
- Purchase information
- Current status
- Physical condition
- Location
- Additional notes

The asset module acts as the central component of Asetonix and connects assets with assignments, transfers, maintenance, retirement, and lifecycle history.

---

### 2. Employee Management

Asetonix maintains employee information required for asset ownership and assignment.

Employee information includes:

- Employee ID
- Name
- Email
- Department
- Designation
- Contact information
- Employee status

Employees can be associated with assets through the assignment workflow.

---

### 3. Asset Assignment

The assignment module manages the relationship between employees and organizational assets.

Asetonix records:

- Assigned asset
- Assigned employee
- Assignment date
- Return date
- Assignment notes
- Current assignment state

The system automatically reflects the asset's availability when an asset is assigned or returned.

Example:
Available
    ↓
Assigned
    ↓
Returned
    ↓
Available

4. Asset Transfers

The transfer module manages movement of assets between employees and organizational locations.

A transfer can record:

Asset
Previous employee
New employee
Previous location
New location
Transfer date
Transfer notes

This provides better visibility when an asset changes ownership or location.

5. Asset Lifecycle & Audit Trail

Asetonix maintains a historical record of important asset-related activities.

The audit trail provides visibility into events such as:

Assignment
Return
Transfer
Maintenance
Retirement
Location changes
Other important asset activities

Example lifecycle:

Acquired
   ↓
Available
   ↓
Assigned
   ↓
Returned
   ↓
Maintenance
   ↓
Available
   ↓
Transferred
   ↓
Retired

The Audit Trail module provides a chronological record of these activities.

6. Maintenance Management

The maintenance module tracks assets that require inspection, repair, servicing, or maintenance.

Maintenance information can include:

Asset
Maintenance status
Service date
Maintenance notes
Maintenance activity
Maintenance history

The system also provides maintenance-related alerts for operational visibility.

7. Retirements

The retirement module manages assets that have reached the end of their operational lifecycle.

Retirement information can include:

Asset
Retirement date
Retirement reason
Notes
Retirement status

Retired assets are removed from active operational use while their historical information remains available.

8. Categories

Categories provide a structured classification system for organizational assets.

Examples include:

Desktop
Laptop
Monitor
Networking
Printer
Other

The Categories module displays:

Category code
Category name
Description
Number of associated assets
Category status
9. Brands

The Brands module manages manufacturers associated with organizational assets.

The module provides:

Brand name
Associated asset count
Brand status

Example:

Dell
10. Models

The Models module manages specific asset models.

Model information can be associated with:

Brand
Asset category
Assets using the model
Model status

Example:

Dell
   ↓
Latitude 5450
   ↓
Organizational Assets
11. Departments

Asetonix supports organizational department tracking.

Department information includes:

Department code
Department name
Description
Employee count
Department status

Example:

IT
Information Technology
Technology and software operations
12. Locations

The Locations module manages physical and organizational locations where assets may be stored or operated.

Location information can include:

Location name
Building
Floor
Associated assets
Location status

Example:

Ahmedabad Office
Ahmedabad Branch
IT Department
13. Alerts

The Alerts module provides operational visibility into asset conditions that may require attention.

Current alert categories include:

High Risk Assets
Maintenance Required
Active Assignments
Retired Assets

The system can display:

Alert counts
High-risk assets
Asset condition
Asset status
Risk score
Maintenance alerts
Active assignments
Retired assets

Example:

Asset Condition
      ↓
Risk Evaluation
      ↓
Alert Detection
      ↓
Operational Review
14. Users & Roles

Asetonix includes user and access management functionality.

The Users & Roles module provides visibility into:

System users
User status
User roles
Staff users
Superusers
Configured groups
Permissions
Access levels

Current access classifications include:

Superuser
Staff
Standard User

The system is designed to support controlled access to different modules and operations.

15. Dashboard & Analytics

Asetonix provides an operational dashboard for monitoring asset activity.

The dashboard can provide information such as:

Total assets
Available assets
Assigned assets
Assets under maintenance
Retired assets
Asset distribution
Assignment activity
Maintenance activity
Lifecycle activity
Operational alerts

Analytics modules include:

Asset Health
Utilization
Risk Analysis
Cost Analysis
16. Reports

The Reports module is currently under development.

Planned reporting functionality includes structured reports based on:

Assets
Assignments
Transfers
Maintenance
Retirements
Departments
Locations
Asset lifecycle activity
17. Export Data

Data export functionality is currently under development.

The planned functionality will allow relevant Asetonix data to be exported for:

Reporting
Analysis
Backup
Administrative review
External processing
Asset Lifecycle

Asetonix follows a structured asset lifecycle:

                Acquisition
                    ↓
                Available
                    ↓
                 Assigned
                    ↓
                  Return
                    ↓
                Available
                    ↓
               Maintenance
                    ↓
                Available
                    ↓
                Transfer
                    ↓
                 Retired

Important lifecycle events are recorded through the system's audit trail.

Role-Based Access

Asetonix is designed with role-based access control.

The system supports different levels of access depending on the user's role.

Current access structure includes:

Superuser
    ↓
Full system administration access

Staff
    ↓
Administrative access to permitted modules

Standard User
    ↓
Regular application access
Technology Stack
Backend
Python
Django
Database
SQLite during development
Django ORM
Database architecture designed to support migration to a production database
Frontend
HTML
CSS
JavaScript
Django Templates
Development Tools
Visual Studio Code
Git
GitHub
Project Architecture
Asetonix/
│
├── assets/
│   │
│   ├── migrations/
│   │
│   ├── templates/
│   │   └── assets/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── assets.html
│   │       ├── categories.html
│   │       ├── brands.html
│   │       ├── models.html
│   │       ├── assignments.html
│   │       ├── transfers.html
│   │       ├── maintenance.html
│   │       ├── retirements.html
│   │       ├── audit_trail.html
│   │       ├── alerts.html
│   │       ├── users_roles.html
│   │       ├── departments.html
│   │       ├── locations.html
│   │       └── ...
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── .gitignore
└── README.md
Current Development Status
Completed
Django project setup
Virtual environment setup
Git and GitHub integration
SQLite database setup
Asset model
Employee model
Asset assignment model
Asset assignment workflow
Asset return workflow
Automatic asset status updates
Django Admin configuration
Asset Management
Categories
Brands
Models
Assignments
Transfers
Maintenance
Retirements
Audit Trail
Alerts
Departments
Locations
Users & Roles
Authentication
Custom Asetonix enterprise interface
Sidebar navigation
Dashboard and analytics sections
In Progress
Reports
Export Data
Planned / Refinement
Advanced reporting
Advanced analytics
Comprehensive automated testing
Security hardening
Production database configuration
Production deployment
Final UI and UX refinement
Development Roadmap
Foundation
    ↓
Asset Management
    ↓
Employee Management
    ↓
Assignment & Return Management
    ↓
Asset Transfers
    ↓
Asset Lifecycle & Audit Trail
    ↓
Maintenance Management
    ↓
Retirements
    ↓
Departments & Locations
    ↓
Authentication & Role-Based Access
    ↓
Dashboard & Alerts
    ↓
Analytics
    ↓
Reports
    ↓
Export Data
    ↓
Testing & Security
    ↓
Production Deployment
    ↓
Production-Ready Asetonix
Project Goal

Asetonix is being developed as a realistic enterprise software project rather than a basic CRUD application.

The goal is to create a structured Enterprise Asset Management platform that combines:

Asset tracking
Employee management
Assignment workflows
Asset transfers
Maintenance management
Retirement management
Lifecycle history
Audit trails
Organizational tracking
Role-based access
Alerts
Analytics
Reporting
Data export

The system is intended to demonstrate practical software engineering, database design, backend development, frontend development, business workflows, and enterprise application architecture.

Key Workflow

A typical Asetonix workflow is:

Create Asset
     ↓
Categorize Asset
     ↓
Assign Brand & Model
     ↓
Set Location
     ↓
Make Asset Available
     ↓
Assign to Employee
     ↓
Track Usage
     ↓
Transfer if Required
     ↓
Return / Maintain
     ↓
Record Lifecycle Events
     ↓
Retire Asset
     ↓
Preserve Historical Record
Interface

Asetonix uses a custom enterprise-style web interface with:

Centralized sidebar navigation
Dashboard-style summary cards
Structured data tables
Status badges
Alert indicators
Operational analytics
Responsive layouts
Consistent visual styling
Module-specific management pages

The interface is built using Django Templates, HTML, CSS, and JavaScript.

Development Environment

The project is currently developed locally using Django.

Typical development workflow:

# Activate virtual environment

# Windows
venv\Scripts\activate

# Start Django development server
python manage.py runserver

The application can then be accessed locally through:

http://127.0.0.1:8000/
Version Control

Asetonix uses Git for source control and GitHub for repository hosting.

Typical workflow:

git status
git add .
git commit -m "Describe changes"
git push origin main
Future Enhancements

Future versions of Asetonix may include:

Advanced asset search
Advanced filtering
Automated notifications
Maintenance scheduling
More detailed analytics
Advanced reports
CSV/Excel export
PDF reports
Improved permission management
Production database support
API integration
Automated testing
Security improvements
Production deployment
Status

🚧 Under Active Development

Asetonix is currently being developed as an MSc IT portfolio project focused on building a realistic Enterprise Asset Management System with practical business workflows, lifecycle management, analytics, access control, and operational visibility.

practical business workflows, lifecycle management, analytics, access control, and operational visibility.

