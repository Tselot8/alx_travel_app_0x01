# ALX Travel App 0x01

Django REST Framework API for managing **Listings** and **Bookings** with full CRUD operations and Swagger documentation.

---

## Setup

```bash
git clone <repo-url>
cd alx_travel_app_0x01
python -m venv venv
# activate venv
pip install -r requirements.txt
# create .env with SECRET_KEY, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## API Endpoints

### Listings

| Method | Endpoint                 | Description          |
|--------|--------------------------|----------------------|
| GET    | /api/listings/           | List all listings    |
| POST   | /api/listings/           | Create a listing     |
| GET    | /api/listings/{id}/      | Retrieve a listing   |
| PUT    | /api/listings/{id}/      | Full update listing  |
| PATCH  | /api/listings/{id}/      | Partial update       |
| DELETE | /api/listings/{id}/      | Delete a listing     |

### Bookings

| Method | Endpoint                 | Description          |
|--------|--------------------------|----------------------|
| GET    | /api/bookings/           | List all bookings    |
| POST   | /api/bookings/           | Create a booking     |
| GET    | /api/bookings/{id}/      | Retrieve a booking   |
| PUT    | /api/bookings/{id}/      | Full update booking  |
| PATCH  | /api/bookings/{id}/      | Partial update       |
| DELETE | /api/bookings/{id}/      | Delete a booking     |

---

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/swagger/`  
- Test endpoints interactively in the browser.

---

## Notes

- Uses **ModelViewSet** for CRUD operations.  
- All endpoints are under `/api/`.  
- Required fields must be included in POST/PUT requests.  
- PATCH can be used for partial updates.