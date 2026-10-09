# Job Application Tracker REST API

A REST API built with Python and Django REST Framework to manage and track job applications. The project allows authenticated users to create, view, update, and delete their job application records.

## Features

- **Job Application Management:** Create, retrieve, update, and delete job applications.
- **Application Details:** Store company name, job title, location, application status, applied date, interview date, salary, and notes.
- **RESTful API:** Expose endpoints using Django REST Framework.
- **Data Validation:** Validate application data and restrict application status to predefined values.
- **Authentication:** Restrict API access to authenticated users.
- **User-Specific Records:** Ensure users access their own job applications.
- **Database Management:** Use Django ORM and migrations to manage database models.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite3
- Git and GitHub

## Project Structure

```text
job_tracker/
├── applications/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/achaljogi/Job_tracker.git
cd Job_tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install django djangorestframework
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an admin user (optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 7. Run the development server

```bash
python manage.py runserver
```

The application will be available at:

`http://127.0.0.1:8000/`

## API Endpoints

Base URL: `http://127.0.0.1:8000/api/`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/applications/` | List job applications |
| POST | `/api/applications/` | Create a job application |
| GET | `/api/applications/<id>/` | Retrieve a specific application |
| PUT | `/api/applications/<id>/` | Update an application |
| PATCH | `/api/applications/<id>/` | Partially update an application |
| DELETE | `/api/applications/<id>/` | Delete an application |

### Authentication

API endpoints require authentication. The project is configured with Django REST Framework session and basic authentication.

You can sign in through the browsable API when using session authentication.

### Application Status Values

The API validates application statuses against the following values:

- Applied
- Shortlisted
- Interview
- Selected
- Rejected
- Withdrawn

## Database

The project uses SQLite3 as its database and Django ORM for database operations. Database schema changes are managed using Django migrations.

## Future Improvements

- Add automated unit and API tests.
- Add pagination and search functionality.
- Add filtering by application status and sorting by application date.
- Improve API documentation.
- Add a frontend dashboard for tracking applications.

## Author

**Achal Jogi**

GitHub: https://github.com/achaljogi

## License

This project is available for educational and portfolio purposes.
