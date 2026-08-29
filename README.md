# Asetonix

**Asetonix** is a web-based Enterprise Asset Management System designed to help organizations manage the complete lifecycle of their physical and digital assets from acquisition to retirement.

The system focuses on centralized asset tracking, ownership, assignment, maintenance, history, and operational visibility.

## Vision

Asetonix aims to provide organizations with a structured way to answer:

* What assets does the organization own?
* Where is each asset currently located?
* Who is responsible for an assigned asset?
* What is the current condition and status of an asset?
* What happened to an asset throughout its lifecycle?
* Which assets require maintenance?
* Which assets are available, assigned, under maintenance, or retired?

## Core Modules

### 1. Asset Management

Centralized management of organizational assets with information such as:

* Asset name
* Unique asset tag
* Category
* Brand and model
* Serial number
* Purchase information
* Current status
* Physical condition
* Location
* Additional notes

### 2. Employee Management

Maintain employee information required for asset ownership and assignment.

* Employee ID
* Name
* Email
* Department
* Designation
* Contact information
* Employee status

### 3. Asset Assignment

Track the relationship between employees and organizational assets.

Asetonix records:

* Assigned asset
* Assigned employee
* Assignment date
* Return date
* Assignment notes
* Current assignment state

The system is designed to automatically reflect the asset's current availability when an asset is assigned or returned.

### 4. Asset Lifecycle & History

Asetonix will maintain an auditable history of important asset events throughout its lifecycle.

Example lifecycle:

```text
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
Retired
```

### 5. Maintenance Management

Track assets that require inspection, repair, servicing, or maintenance.

Planned capabilities include:

* Maintenance records
* Maintenance status
* Service dates
* Maintenance costs
* Service history
* Maintenance notes

### 6. Location & Department Tracking

Track where organizational assets are located and which organizational unit is responsible for them.

This will support better visibility across departments, offices, and operational locations.

### 7. Dashboard & Analytics

Asetonix will provide an operational dashboard with insights such as:

* Total assets
* Available assets
* Assigned assets
* Assets under maintenance
* Retired assets
* Asset distribution by category
* Asset distribution by department
* Maintenance trends
* Assignment statistics

### 8. Role-Based Access

The system is planned to support different levels of access for organizational users.

Possible roles include:

* Administrator
* Asset Manager
* Department Manager
* Employee

Each role will have appropriate permissions for viewing, creating, updating, assigning, and managing assets.

## Technology Stack

### Backend

* Python
* Django

### Database

* SQLite during development
* Database architecture designed to support migration to a production database

### Frontend

* HTML
* CSS
* JavaScript
* Django Templates

### Development Tools

* Visual Studio Code
* Git
* GitHub

## Current Project Structure

```text
Asetonix/
│
├── assets/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
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

## Current Development Status

### Completed

* Django project setup
* Virtual environment setup
* Git and GitHub integration
* Asset model
* Employee model
* Asset assignment model
* Asset assignment and return workflow
* Automatic asset status update
* Django Admin configuration
* Initial GitHub repository setup

### In Progress

* Asset lifecycle history
* Maintenance management
* Location and department management
* Dashboard and analytics
* Authentication and role-based access
* Custom Asetonix interface

## Development Roadmap

```text
Foundation
    ↓
Asset Management
    ↓
Employee & Assignment Management
    ↓
Asset Lifecycle History
    ↓
Maintenance Management
    ↓
Departments & Locations
    ↓
Authentication & Role-Based Access
    ↓
Dashboard & Analytics
    ↓
Reports
    ↓
Testing & Security
    ↓
Production-Ready Asetonix
```

## Project Goal

Asetonix is being developed as a realistic enterprise software project rather than a simple CRUD application.

The long-term goal is to create a structured asset management platform with lifecycle tracking, operational workflows, historical records, analytics, and role-based access.

## Status

**🚧 Under Active Development**

Asetonix is currently being developed as an MSc IT portfolio project.
