# Stock Monitoring and Alert System - Backend

This is the backend of the Stock Monitoring and Alert System, developed using Django. It handles API endpoints, database management, and business logic.

## Real-Time Stock Data with Polygon.io

To obtain real-time stock data, it's necessary to use the Advanced plan of the Polygon.io API. However, for educational and development purposes, we have opted to use the free plan, which updates the stock information database daily. Although requests are made every 60 seconds, the stock quotes may not reflect the current market price in real-time with the free plan.

We chose the Polygon.io API due to its extensive range of easily manipulable data, including detailed historical price records. This data is particularly useful for building charts and applying more complex mathematical models in financial and market analysis. This flexibility and richness of information make the API an excellent choice for developing applications and for learning about financial data analysis.

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

Using a virtual environment, execute the following steps:

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```
3. **Run server**:
   ```bash
   python manage.py runserver
   ```
