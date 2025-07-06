# 🧳 Travel Booking Web Application

A web-based platform to search, book, and manage travel options (Flights, Trains, Buses) built with Django.

---

##  Features

-  User Registration, Login, Logout
-  Profile Update
-  Search Travel Options (by type, source/destination, date)
-  Book Travel Tickets
-  View Bookings
-  Cancel Bookings
-  View Documentation Page

---

##  Tech Stack

- **Backend**: Django (Python)
- **Database**: MySQL (production), SQLite (testing)
- **Frontend**: Django Templates (HTML, Bootstrap)
- **Deployment**: PythonAnywhere
- **Environment Management**: `python-decouple`, `.env`

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Pawar-Tushar/Travel_booking-webapp
cd travel-booking-app
```
### 2. Create Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=3306
```
 Note: Use DEBUG=False and add allowed domains (e.g. yourdomain.com) in production.
### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Create Superuser

```bash
python manage.py createsuperuser
```
### 7. Run the Server

```bash
python manage.py runserver
```
Visit: http://127.0.0.1:8000/

### 8. Run Tests

To run unit tests for `users` and `bookings` apps:

```bash
python manage.py test
```
 To check code coverage:
```bash
coverage run manage.py test
coverage report -m
```

Testing Environment:

```python
if 'test' in sys.argv:
    # SQLite used for testing
else:
    # MySQL used for development/production
```
### 9. 📁 Folder Structure
```bash
travel_booking/
│
├── bookings/              # Booking-related logic
├── users/                 # User authentication and profile
├── travel_booking/        # Core settings and routing
├── staticfiles/           # Static assets for production
├── .env                   # Environment variables (not committed)
├── manage.py              # Django CLI
└── requirements.txt       # Python dependencies
```

## Deployment

This project is deployable on **PythonAnywhere**:

- Upload your files
- Set environment variables in the web app config
- Point WSGI to `travel_booking.wsgi.application`
- Run `python manage.py migrate` and collect static files

---
## License

This project is licensed for educational/demo use. 

## Credits

Built by Tushar for the Travel Booking App Assignment.

