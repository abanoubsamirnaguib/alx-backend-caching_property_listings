# ALX Backend Caching Property Listings

A Django project for managing property listings with PostgreSQL database and Redis caching.

## Features

- Django web framework
- PostgreSQL database with Docker
- Redis caching with Django-Redis
- Property model with title, description, price, location, and creation timestamp
- Dockerized database and cache services

## Project Structure

```
alx-backend-caching_property_listings/
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── .env.example
├── alx_backend_caching_property_listings/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── properties/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── apps.py
    ├── admin.py
    ├── tests.py
    └── migrations/
        └── __init__.py
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd alx-backend-caching_property_listings
```

### 2. Set Up Environment Variables

Copy the example environment file and modify as needed:

```bash
copy .env.example .env
```

### 3. Start Docker Services

Start PostgreSQL and Redis using Docker Compose:

```bash
docker-compose up -d
```

This will start:
- PostgreSQL on port 5432
- Redis on port 6379

### 4. Install Python Dependencies

Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac

pip install -r requirements.txt
```

### 5. Run Database Migrations

Create and apply migrations for the Property model:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`.

## Property Model

The `Property` model includes the following fields:

- `title` (CharField, max_length=200): Property title
- `description` (TextField): Detailed property description
- `price` (DecimalField, max_digits=10, decimal_places=2): Property price
- `location` (CharField, max_length=100): Property location
- `created_at` (DateTimeField, auto_now_add=True): Creation timestamp

## Database Configuration

The project is configured to use PostgreSQL with the following default settings:

- Database: `property_listings`
- User: `postgres`
- Password: `postgres`
- Host: `localhost`
- Port: `5432`

## Redis Caching

Redis is configured as the default cache backend and session store:

- Host: `localhost`
- Port: `6379`
- Database: `1`

## Docker Services

The `docker-compose.yml` file defines:

- **PostgreSQL**: Official postgres:latest image with health checks
- **Redis**: Official redis:latest image with health checks
- **Volumes**: Persistent storage for both services

## Environment Variables

The following environment variables can be configured:

- `DB_NAME`: Database name (default: property_listings)
- `DB_USER`: Database user (default: postgres)
- `DB_PASSWORD`: Database password (default: postgres)
- `DB_HOST`: Database host (default: localhost)
- `DB_PORT`: Database port (default: 5432)
- `REDIS_HOST`: Redis host (default: localhost)
- `REDIS_PORT`: Redis port (default: 6379)
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (default: True)

## Development

To stop the Docker services:

```bash
docker-compose down
```

To stop and remove volumes:

```bash
docker-compose down -v
```
