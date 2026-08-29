
# Asetonix

## Enterprise Asset Intelligence Platform

Asetonix is a web-based **Enterprise Asset Management and Asset Intelligence Platform** designed to help organizations manage, track, analyze, and optimize the complete lifecycle of their physical and digital assets.

The platform provides centralized asset management together with employee management, assignments, transfers, maintenance, retirements, lifecycle history, auditability, alerts, analytics, reporting, data export, and an extensible foundation for AI-powered asset intelligence.

Asetonix is being designed as a **business-oriented enterprise application rather than a simple CRUD system**.

---

# Overview

Organizations manage assets across multiple employees, departments, locations, and operational environments.

Without a centralized system, it can become difficult to determine:

- What assets the organization owns
- Where each asset is located
- Who is responsible for an asset
- What condition an asset is in
- Whether an asset is available, assigned, under maintenance, or retired
- How much an asset costs to maintain
- What activities occurred during its lifecycle
- Which assets require attention
- Which assets may represent operational or financial risk

Asetonix addresses these challenges through a centralized platform for managing the complete asset lifecycle.

---

# Vision

The long-term vision of Asetonix is to evolve from a traditional Enterprise Asset Management System into an **Enterprise Asset Intelligence Platform**.

The platform is designed to help organizations:

- Track assets
- Manage ownership
- Manage assignments
- Monitor asset condition
- Manage maintenance
- Track transfers
- Maintain lifecycle history
- Analyze utilization
- Analyze asset risk
- Analyze asset costs
- Identify operational issues
- Generate reports
- Export business data
- Generate intelligent recommendations
- Predict maintenance and risk
- Detect unusual asset behavior
- Optimize asset utilization
- Support asset replacement decisions

---

# Core Capabilities

## 1. Asset Management

The Asset Management module provides centralized management of organizational assets.

Asset information includes:

- Asset name
- Unique asset tag
- Category
- Brand
- Model
- Serial number
- Purchase date
- Purchase price
- Current status
- Physical condition
- Location
- Notes
- Creation date
- Last updated date

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

The Transfer module manages movement of assets between employees and organizational locations.

Transfer information includes:

* Asset
* Previous employee
* New employee
* Previous location
* New location
* Transfer date
* Transfer notes

Transfers also contribute to lifecycle visibility and historical tracking.

---

## 5. Maintenance Management

The Maintenance module manages assets that require inspection, repair, servicing, or maintenance.

Maintenance information includes:

* Asset
* Maintenance title
* Description
* Priority
* Maintenance status
* Reported date
* Start date
* Completion date
* Maintenance cost
* Technician
* Notes

Maintenance records contribute to asset health, risk analysis, operational alerts, and future predictive maintenance capabilities.

---

## 6. Asset Retirements

The Retirement module manages assets that are no longer in active operational use.

Retirement information includes:

* Asset
* Retirement date
* Retirement reason
* Retirement notes
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

Examples include:

* Dell
* HP
* Lenovo
* Other manufacturers

Brand information includes:

* Brand name
* Associated asset count
* Brand status

---

## 9. Models

The Models module provides model-level organization of assets.

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

Departments can be used for organizational reporting, asset ownership analysis, and future cost and utilization analysis.

---

## 11. Locations

The Locations module manages physical and operational locations where assets may be stored or used.

Location information can include:

* Location name
* Building
* Floor
* Associated assets
* Location status

The location architecture is designed to support organizations operating across multiple offices, branches, facilities, and operational environments.

---

# Asset Intelligence

## 12. Asset Health

The Asset Health module evaluates the operational health of assets.

Health analysis can consider factors such as:

* Asset condition
* Asset status
* Maintenance history
* Operational activity

Health levels include:

* Excellent
* Good
* Fair
* Poor

The health layer provides a foundation for future predictive asset intelligence.

---

## 13. Utilization Analysis

The Utilization module provides visibility into how organizational assets are being used.

Current analysis includes:

* Total assets
* Assigned assets
* Available assets
* Assets under maintenance
* Retired assets
* Utilization rate

Future enhancements can include:

* Underutilized asset detection
* Department utilization comparison
* Location utilization comparison
* Historical utilization trends
* Asset usage optimization recommendations

---

## 14. Risk Analysis

The Risk Analysis module identifies assets that may require monitoring or intervention.

Current risk analysis considers:

* Asset condition
* Asset status
* Maintenance history

Risk levels include:

* Low Risk
* Medium Risk
* High Risk

The planned intelligence layer will extend this into predictive risk analysis using historical operational data.

---

## 15. Cost Analysis

The Cost Analysis module provides visibility into asset-related financial information.

Analysis can include:

* Asset purchase costs
* Maintenance costs
* Asset-related expenditure
* Cost distribution

Future financial intelligence will include:

* Total Cost of Ownership
* Maintenance cost trends
* Cost by department
* Cost by location
* High-cost assets
* High-maintenance assets
* Replacement candidates

---

# Lifecycle & Governance

## 16. Asset Lifecycle

Asetonix follows a structured asset lifecycle.

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
Retirement Review
    ↓
Retired
```

Important lifecycle activities are recorded through the asset history and audit mechanisms.

---

## 17. Audit Trail

The Audit Trail provides a chronological history of important asset activities.

Activities can include:

* Assignment
* Return
* Transfer
* Maintenance
* Retirement
* Location changes
* Other lifecycle activities

Example:

```text
Asset Assigned
      ↓
Asset Returned
      ↓
Asset Transferred
      ↓
Maintenance Reported
      ↓
Maintenance Completed
      ↓
Asset Retired
```

This provides historical visibility and supports accountability.

---

## 18. Alerts

The Alerts module provides operational visibility into conditions that may require attention.

Current alert categories include:

* High Risk Assets
* Maintenance Required
* Active Asset Returns
* Retired Assets

Alert information can include:

* Alert counts
* High-risk asset information
* Maintenance information
* Assignment information
* Retirement information
* Risk scores

Future enhancements will include automated notifications and intelligent alerts.

---

## 19. Users & Roles

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

Planned enterprise roles include:

```text
Administrator
     ↓
Asset Manager
     ↓
Department Manager
     ↓
Employee
     ↓
Auditor
```

Role-based permissions will control access to operational and administrative functionality.

---

# Dashboard & Analytics

## 20. Dashboard

The Dashboard provides centralized operational visibility into the asset environment.

Current dashboard capabilities include operational asset statistics and key asset information.

The advanced dashboard will provide:

* Total assets
* Available assets
* Assigned assets
* Maintenance assets
* Retired assets
* Total asset value
* Maintenance expenditure
* Utilization rate
* High-risk assets
* Asset condition distribution
* Asset distribution by category
* Asset distribution by department
* Asset distribution by location
* Assignment trends
* Maintenance trends
* Retirement trends
* Operational alerts

---

# Advanced Analytics

Asetonix is planned to include a dedicated advanced analytics layer.

## Planned Analytics

### Asset Distribution

Analyze assets by:

* Category
* Brand
* Model
* Department
* Location
* Status
* Condition

### Utilization Analytics

Analyze:

* Assigned assets
* Available assets
* Underutilized assets
* Department utilization
* Location utilization
* Historical utilization trends

### Maintenance Analytics

Analyze:

* Maintenance frequency
* Maintenance cost
* Maintenance status
* Maintenance trends
* Repeated maintenance
* High-maintenance assets

### Financial Analytics

Analyze:

* Purchase expenditure
* Maintenance expenditure
* Total asset value
* Cost distribution
* Total Cost of Ownership

---

# Advanced Reports

## 21. Reports

The Reports module provides centralized operational reporting.

Current reporting capabilities include:

* Asset reports
* Organization reports
* Asset statistics
* Operational summaries

The advanced reporting layer will provide:

* Asset reports
* Assignment reports
* Transfer reports
* Maintenance reports
* Retirement reports
* Department reports
* Location reports
* Lifecycle reports
* Risk reports
* Cost reports
* Utilization reports
* AI insight reports

Advanced reports will support:

* Filters
* Charts
* Trends
* KPIs
* Tables
* Business summaries
* Data export

---

# Data Export

## 22. Export Data

The Export Data module currently provides CSV export functionality.

Available exports include:

* Asset Data
* Assignment Data
* Maintenance Data
* Lifecycle Data

Example export structure:

```text
Asset Data
     ↓
CSV File

Assignment Data
     ↓
CSV File

Maintenance Data
     ↓
CSV File

Lifecycle Data
     ↓
CSV File
```

Planned additional formats include:

* Excel
* PDF

---

# Artificial Intelligence & Asset Intelligence

## 23. AI Asset Insights

Asetonix is being extended with an AI-powered intelligence layer.

The goal is to use actual organizational asset data to generate useful operational insights rather than providing a simple chatbot interface.

Planned AI capabilities include:

* Asset health insights
* Risk explanations
* Maintenance recommendations
* Asset replacement recommendations
* Utilization recommendations
* Cost insights
* Operational recommendations

Example:

```text
Asset
  +
Condition
  +
Maintenance History
  +
Age
  +
Usage
  +
Cost
  +
Lifecycle History
       ↓
AI Analysis
       ↓
Business Insight
       ↓
Recommended Action
```

Example output:

```text
Asset Risk Insight

AST-0001 shows elevated operational risk due to
repeated maintenance activity and declining asset
condition.

Recommended Action:
Schedule preventive inspection and evaluate
replacement cost versus continued maintenance.
```

---

# Predictive Maintenance

## 24. Predictive Maintenance

The planned predictive maintenance capability will analyze historical maintenance information to identify assets that may require attention before a failure occurs.

Potential inputs include:

* Maintenance frequency
* Maintenance cost
* Asset age
* Asset condition
* Previous failures
* Maintenance history
* Operational activity

Conceptual workflow:

```text
Historical Asset Data
        ↓
Data Preparation
        ↓
Feature Analysis
        ↓
Prediction Model
        ↓
Maintenance Risk
        ↓
Recommended Action
```

The objective is to move from reactive maintenance toward preventive and predictive maintenance.

---

# Predictive Risk Analysis

## 25. Intelligent Risk Prediction

Future risk analysis will extend the current rule-based risk model into a data-driven prediction system.

Potential factors include:

* Asset age
* Asset condition
* Maintenance frequency
* Maintenance cost
* Assignment activity
* Transfer frequency
* Lifecycle events
* Operational status

Possible outputs:

```text
Low
Medium
High
Critical
```

The system will also provide an explanation of the major factors contributing to the predicted risk.

---

# Anomaly Detection

## 26. Asset Anomaly Detection

Asetonix will support detection of unusual operational patterns.

Potential anomalies include:

* Unusually frequent transfers
* Repeated maintenance events
* Unexpected maintenance costs
* Very short assignment periods
* Long periods of inactivity
* Abnormal utilization
* Unusual lifecycle activity

Example:

```text
Assignment
    ↓
Return
    ↓
Assignment
    ↓
Maintenance
    ↓
High Cost
    ↓
Repeated Activity
    ↓
Potential Anomaly
```

This can help organizations identify assets requiring investigation.

---

# Asset Replacement Intelligence

## 27. Replacement Recommendations

Asetonix will help organizations identify assets that may be candidates for replacement.

Potential factors include:

* Asset age
* Declining condition
* Maintenance frequency
* Maintenance cost
* Operational downtime
* Lifecycle history
* Total Cost of Ownership

Example:

```text
High Maintenance Cost
          +
Poor Condition
          +
Repeated Failures
          +
High Asset Age
          ↓
Replacement Candidate
```

---

# Financial Intelligence

## 28. Total Cost of Ownership

Asetonix will support financial analysis beyond the original purchase price.

Conceptually:

```text
Purchase Cost
      +
Maintenance Cost
      +
Operational Cost
      +
Other Asset Costs
      ↓
Total Cost of Ownership
```

This can help organizations compare:

* Continue maintaining an asset
* Replace the asset
* Reallocate the asset
* Retire the asset

---

# Interactive 3D Asset Visualization

## 29. 3D Asset Environment

A future visualization module will provide an interactive 3D representation of organizational assets and locations.

The goal is to provide spatial asset intelligence rather than a decorative 3D interface.

Potential capabilities include:

* Interactive office environment
* Building visualization
* Floor visualization
* Location-based asset visualization
* Asset selection
* Asset information panels
* Department filtering
* Location filtering
* Status filtering
* Maintenance asset visualization
* Assigned asset visualization

Conceptual structure:

```text
Organization
     ↓
Building
     ↓
Floor
     ↓
Location
     ↓
Department
     ↓
Assets
     ↓
Asset Details
```

The 3D layer will connect with the actual Asetonix asset database.

---

# Workflow & Approval Automation

## 30. Business Workflows

Future enterprise workflows will support approval-based asset operations.

Example:

```text
Employee Request
       ↓
Department Manager
       ↓
Asset Manager
       ↓
Approval
       ↓
Asset Assignment
       ↓
Audit Record
```

Retirement workflow:

```text
Retirement Request
       ↓
Manager Review
       ↓
Approval
       ↓
Asset Retired
       ↓
Lifecycle History
```

This allows Asetonix to support more structured enterprise processes.

---

# Business Applicability

Asetonix is designed to be configurable for different types of organizations.

## Corporate Offices

Possible assets:

* Laptops
* Desktops
* Monitors
* Printers
* Networking equipment
* Office equipment

## Universities

Possible assets:

* Computers
* Projectors
* Laboratory equipment
* Library equipment
* Furniture
* Networking equipment

## Hospitals

Possible assets:

* Medical equipment
* Monitoring equipment
* Laboratory equipment
* Beds
* Emergency equipment

## Manufacturing

Possible assets:

* Machines
* Tools
* Production equipment
* Safety equipment
* Vehicles

## Retail

Possible assets:

* POS systems
* Barcode scanners
* Displays
* Networking equipment
* Store equipment

The system is designed around configurable categories, locations, departments, users, and workflows rather than being limited to a single industry.

---

# Technology Stack

## Backend

* Python
* Django
* Django ORM

## Database

* SQLite for development
* Django database migrations
* Production database support planned

## Frontend

* HTML
* CSS
* JavaScript
* Django Templates

## Visualization

Planned:

* Interactive charts
* Advanced dashboards
* 3D visualization

## AI / Machine Learning

Planned:

* Data analysis
* Predictive modeling
* Risk prediction
* Predictive maintenance
* Anomaly detection
* AI recommendations

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
│   │       ├── reports.html
│   │       ├── export_data.html
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
* Employee Management
* Categories
* Brands
* Models
* Assignments
* Transfers
* Maintenance
* Retirements
* Asset Lifecycle
* Asset History
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
* Dashboard
* Reports
* Asset CSV Export
* Assignment CSV Export
* Maintenance CSV Export
* Lifecycle CSV Export

---

# Advanced Development

The following capabilities are part of the advanced Asetonix development roadmap:

* Advanced dashboard visualizations
* Interactive charts
* Advanced reporting
* Advanced filtering
* Asset utilization intelligence
* Financial intelligence
* Total Cost of Ownership analysis
* AI asset insights
* Predictive maintenance
* Predictive risk analysis
* Anomaly detection
* Asset replacement recommendations
* Automated intelligent alerts
* Workflow approvals
* Advanced role-based access control
* Interactive 3D asset visualization
* Location-based 3D asset exploration

---

# Testing & Security

Final development will include:

* Automated testing
* Workflow testing
* Authentication testing
* Authorization testing
* Permission testing
* Input validation
* Error handling
* CSRF protection
* Security hardening
* Audit verification
* Data integrity testing
* Export testing
* Production configuration testing

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
Advanced Analytics & Visualization
    ↓
Advanced Reports
    ↓
Data Export
    ↓
AI Asset Intelligence
    ↓
Predictive Risk & Maintenance
    ↓
Anomaly Detection
    ↓
Financial & TCO Intelligence
    ↓
Interactive 3D Asset Visualization
    ↓
Workflow & Approval Automation
    ↓
Testing & Security
    ↓
Production Readiness
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
* Business workflow design
* Asset lifecycle management
* Access control
* Operational analytics
* Reporting
* Data export
* Auditability
* Enterprise application design
* Data-driven decision support
* Artificial intelligence
* Predictive analytics
* Visualization

The long-term goal is to create a structured **Enterprise Asset Intelligence Platform** capable of helping organizations manage assets from acquisition through retirement while providing operational visibility, analytics, predictive insights, and intelligent recommendations.

---

# Project Status

**🚧 Under Active Development**

Asetonix is currently being developed as an **MSc IT portfolio project** focused on building a realistic Enterprise Asset Management and Asset Intelligence Platform.

The project is evolving from core asset lifecycle management toward advanced analytics, artificial intelligence, predictive intelligence, interactive visualization, and enterprise workflow automation.

```

This version fixes the outdated parts of your current README, especially the sections that incorrectly say **Reports** and **Export Data** are still under development. :contentReference[oaicite:0]{index=0}

It also keeps the advanced AI and 3D features clearly marked as **planned/advanced development**, so the README does not falsely claim that we have already built features that we haven't built yet.
```
