# Stock Monitoring and Alert System - Backend

This is the backend of the Stock Monitoring and Alert System, developed using Django. It handles API endpoints, database management, and business logic.

## Table of Contents

1. [Folder Structure](#folder-structure)
2. [Main Technologies Used](#main-technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Email Notifications](#email-notifications)
5. [Deployment](#deployment)
6. [Contributing](#contributing)
7. [License](#license)

## Folder Structure

The project is organized into the following main directories:

- **inoa_tracking**: Contains the Django backend responsible for API endpoints, database management, and business logic.

  - **settings.py**: Django settings, including database, middleware, and installed apps configurations.
  - **urls.py**: URL routing for the Django project.
  - **wsgi.py** and **asgi.py**: Entry points for WSGI and ASGI servers.

- **stocks**: A Django app for managing stock-related data and functionalities.
  - **models.py**: Defines the data models for stock entities.
  - **views.py**: Handles HTTP requests and responses for stock data.
  - **serializers.py**: Serializes data between Django models and JSON.
  - **tasks.py**: Contains background tasks.

## Main Technologies Used

- **Django**: A high-level Python web framework used for the backend, handling API management and database interactions.
- **Polygon API**: Used for fetching real-time stock data and conducting historical data analysis.

## Setup Instructions

### Backend (Django)

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
