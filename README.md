# Event Management API

A RESTful API for managing events and user registrations, built with Django and Django REST Framework.

## Features

- User authentication with JWT
- CRUD operations for events
- Event registration with capacity management
- Waitlist functionality for full events
- Filtering and searching events
- API documentation with Swagger/ReDoc

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- PostgreSQL (optional, SQLite is used by default)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd event-management-api
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- ReDoc: `http://127.0.0.1:8000/api/redoc/`

## API Endpoints

### Authentication

- `POST /api/v1/auth/register/` - Register a new user
- `POST /api/v1/auth/token/` - Obtain JWT token
- `POST /api/v1/auth/token/refresh/` - Refresh JWT token

### Events

- `GET /api/v1/events/` - List all events
- `POST /api/v1/events/` - Create a new event
- `GET /api/v1/events/{id}/` - Retrieve an event
- `PUT /api/v1/events/{id}/` - Update an event
- `DELETE /api/v1/events/{id}/` - Delete an event
- `POST /api/v1/events/{id}/register/` - Register for an event

### User-Specific

- `GET /api/v1/users/me/events/registered/` - Get events the current user is registered for
- `GET /api/v1/users/me/events/organized/` - Get events organized by the current user

## Query Parameters

### Events List

- `upcoming=true` - Show only upcoming events
- `organizer=username` - Filter events by organizer
- `search=term` - Search in event title or location

## Testing

To run the test suite:

```bash
python manage.py test
```

## Deployment

For production deployment, make sure to:

1. Set `DEBUG=False` in your environment variables
2. Set a strong `SECRET_KEY`
3. Configure a production database (PostgreSQL recommended)
4. Set up a proper web server (Nginx + Gunicorn)
5. Configure HTTPS with Let's Encrypt

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
