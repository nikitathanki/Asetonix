
# Asetonix

## Enterprise Asset Management System

Asetonix is a web-based **Enterprise Asset Management System (EAM)** designed to help organizations manage, track, and monitor the complete lifecycle of their physical and digital assets.

The system provides a centralized platform for asset management, employee management, assignments, transfers, maintenance, retirements, departments, locations, audit history, alerts, user management, and asset analytics.

---

## Overview

Organizations often manage assets across different departments, employees, offices, and operational locations. Without a centralized system, it can become difficult to determine the current ownership, location, condition, status, and history of an asset.

Asetonix addresses this problem by providing a structured platform for managing assets throughout their lifecycle.

The system helps answer important operational questions:

- What assets does the organization own?
- Where is each asset currently located?
- Who is responsible for an assigned asset?
- What is the current condition of an asset?
- Which assets are available, assigned, under maintenance, or retired?
- Which assets require attention?
- What activities have occurred during an asset's lifecycle?
- Which department or location is associated with an asset?
- Which users can access the system?

---

## Vision

The vision of Asetonix is to provide organizations with a reliable and centralized platform for managing their assets and related operational processes.

The system focuses on:

- Centralized asset tracking
- Employee and department management
- Asset assignment and return
- Asset transfers
- Maintenance management
- Asset retirement
- Lifecycle history
- Audit trail
- Asset health analysis
- Utilization analysis
- Risk analysis
- Cost analysis
- Operational alerts
- User and role management
- Reporting and data export

---

# Core Modules

## 1. Asset Management

The Asset Management module provides centralized management of organizational assets.

Asset information includes:

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

Assets act as the central entity connecting assignments, transfers, maintenance, retirement, and lifecycle activities.

---

## 2. Employee Management

The Employee Management module maintains employee information required for asset ownership and assignment.

Employee information includes:

- Employee ID
- Name
- Email
- Department
- Designation
- Contact information
- Employee status

Employees can be associated with organizational assets through the assignment workflow.

---

## 3. Asset Assignment

The Assignment module manages the relationship between employees and organizational assets.

The system records:

- Assigned asset
- Assigned employee
- Assignment date
- Return date
- Assignment notes
- Current assignment state

Typical workflow:

```text
Available
    ↓
Assigned
    ↓
Returned
    ↓
Available
````

The system automatically updates the operational status of an asset when it is assigned or returned.

---

## 4. Asset Transfers

The Transfer module manages the movement of assets between employees and organizational locations.

Transfer information includes:

* Asset
* Previous employee
* New employee
* Previous location
* New location
* Transfer date
* Transfer notes

This provides better visibility when an asset changes ownership or location.

---

## 5. Maintenance Management

The Maintenance module manages assets that require inspection, repair, servicing, or maintenance.

Maintenance information includes:

* Asset
* Maintenance status
* Service date
* Maintenance activity
* Maintenance notes
* Maintenance history

Maintenance information also contributes to asset monitoring and operational alerts.

---

## 6. Asset Retirements

The Retirement module manages assets that are no longer in active operational use.

Retirement information includes:

* Asset
* Retirement date
* Retirement reason
* Notes
* Retirement status

Retired assets are removed from active operations while their historical information remains available.

---

## 7. Categories

The Categories module provides structured classification for organizational assets.

Examples include:

* Desktop
* Laptop
* Monitor
* Networking
* Printer
* Other

Category information includes:

* Category code
* Category name
* Description
* Associated asset count
* Category status

---

## 8. Brands

The Brands module manages manufacturers associated with organizational assets.

It provides:

* Brand name
* Associated asset count
* Brand status

Examples:

* Dell
* HP
* Lenovo

---

## 9. Models

The Models module manages specific asset models and their associated brands.

Example:

```text
Brand
  ↓
Dell
  ↓
Latitude 5450
  ↓
Organizational Assets
```

Model information can include:

* Model name
* Brand
* Category
* Associated assets
* Model status

---

## 10. Departments

The Departments module provides organizational tracking.

Department information includes:

* Department code
* Department name
* Description
* Employee count
* Department status

---

## 11. Locations

The Locations module manages physical and operational locations where assets may be stored or used.

Location information includes:

* Location name
* Building
* Floor
* Associated assets
* Location status

---

## 12. Asset Health

The Asset Health module evaluates the current health of assets.

The health score is calculated using factors such as:

* Asset condition
* Asset status
* Maintenance history

Health levels include:

* Excellent
* Good
* Fair
* Poor

---

## 13. Utilization

The Utilization module provides an overview of how organizational assets are currently being used.

It provides:

* Total assets
* Assigned assets
* Available assets
* Assets under maintenance
* Retired assets
* Utilization rate

---

## 14. Risk Analysis

The Risk Analysis module identifies assets that may require monitoring or intervention.

Risk analysis considers:

* Asset condition
* Asset status
* Maintenance history

Risk levels include:

* Low Risk
* Medium Risk
* High Risk

---

## 15. Cost Analysis

The Cost Analysis module provides visibility into asset-related financial information.

It can be used to analyze:

* Asset purchase costs
* Maintenance costs
* Asset-related expenditure
* Cost distribution

---

## 16. Audit Trail

The Audit Trail module maintains a chronological history of important asset activities.

Activities can include:

* Assignment
* Return
* Transfer
* Maintenance
* Retirement
* Location-related changes
* Other lifecycle activities

---

## 17. Alerts

The Alerts module provides operational visibility into asset conditions that may require attention.

Current alert categories include:

* High Risk Assets
* Maintenance Required
* Active Assignments
* Retired Assets

The alert page provides:

* Alert counts
* High-risk asset information
* Maintenance information
* Assignment information
* Retired asset information
* Risk scores

---

## 18. Users & Roles

The Users & Roles module provides visibility into system users and access levels.

It includes:

* System users
* User status
* User roles
* Staff users
* Superusers
* Groups
* Permissions
* Access levels

Current access classifications include:

* Superuser
* Staff
* Standard User

---

## 19. Dashboard & Analytics

The Dashboard provides centralized operational visibility into the asset environment.

Dashboard information can include:

* Total assets
* Available assets
* Assigned assets
* Assets under maintenance
* Retired assets
* Asset distribution
* Assignment activity
* Maintenance activity
* Lifecycle activity
* Operational alerts

Analytics modules include:

* Asset Health
* Utilization
* Risk Analysis
* Cost Analysis

---

## 20. Reports

The Reports module is currently **under development**.

Planned reporting functionality includes:

* Asset reports
* Assignment reports
* Transfer reports
* Maintenance reports
* Retirement reports
* Department reports
* Location reports
* Lifecycle reports

---

## 21. Export Data

The Export Data functionality is currently **under development**.

Planned export capabilities include:

* Asset data export
* Assignment data export
* Maintenance data export
* Lifecycle data export
* Reporting data export

Planned formats may include:

* CSV
* Excel
* PDF

---

# Asset Lifecycle

Asetonix follows a structured asset lifecycle:

```text
Acquisition
    ↓
Available
    ↓
Assigned
    ↓
Returned
    ↓
Available
    ↓
Maintenance
    ↓
Available
    ↓
Transferred
    ↓
Retired
```

Important lifecycle activities can be recorded through the audit trail.

---

# Technology Stack

## Backend

* Python
* Django
* Django ORM

## Database

* SQLite for development
* Django database migrations
* Architecture designed for migration to a production database

## Frontend

* HTML
* CSS
* JavaScript
* Django Templates

## Development Tools

* Visual Studio Code
* Git
* GitHub

---

# Project Architecture

```text
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
```

---

# Current Development Status

## Completed

* Django project setup
* Virtual environment setup
* Git and GitHub integration
* SQLite database setup
* Asset model
* Employee model
* Asset assignment model
* Asset assignment workflow
* Asset return workflow
* Automatic asset status updates
* Django Admin configuration
* Asset Management
* Categories
* Brands
* Models
* Assignments
* Transfers
* Maintenance
* Retirements
* Audit Trail
* Asset Health
* Utilization
* Risk Analysis
* Cost Analysis
* Alerts
* Departments
* Locations
* Users & Roles
* Authentication
* Custom Asetonix enterprise interface
* Sidebar navigation
* Dashboard and analytics sections

## In Progress

* Reports
* Export Data

## Planned / Refinement

* Advanced reporting
* Advanced analytics
* Comprehensive automated testing
* Security hardening
* Production database configuration
* Production deployment
* Final UI and UX refinement

---

# Development Roadmap

```text
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
Maintenance Management
    ↓
Asset Lifecycle & Audit Trail
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
```

---

# Development Environment

Asetonix is currently developed locally using Django.

## Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

## Run Development Server

```bash
python manage.py runserver
```

Application:

```text
http://127.0.0.1:8000/
```

---

# Version Control

Asetonix uses Git for source control and GitHub for repository hosting.

Typical workflow:

```bash
git status
git add .
git commit -m "Describe changes"
git push origin main
```

---

# Project Goal

Asetonix is being developed as a realistic enterprise software project rather than a simple CRUD application.

The project demonstrates:

* Software engineering
* Database design
* Backend development
* Frontend development
* Django application architecture
* Business workflows
* Asset lifecycle management
* Access control
* Operational analytics
* Auditability
* Enterprise application design

The long-term goal is to create a structured Enterprise Asset Management platform capable of managing assets from acquisition through retirement while maintaining operational and historical visibility.

---

# Future Enhancements

Future versions of Asetonix may include:

* Advanced asset search
* Advanced filtering
* Automated notifications
* Maintenance scheduling
* Advanced analytics
* Advanced reporting
* CSV and Excel export
* PDF reports
* Improved permission management
* Production database support
* API integration
* Automated testing
* Security improvements
* Production deployment

---

# Project Status

**🚧 Under Active Development**

Asetonix is currently being developed as an **MSc IT portfolio project** focused on building a realistic Enterprise Asset Management System with practical business workflows, lifecycle management, analytics, access control, alerts, and operational visibility.
```
