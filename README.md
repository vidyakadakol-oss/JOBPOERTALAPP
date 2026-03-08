Django Job Portal Backend API

A RESTful backend system for a Job Portal application built using Django and Django REST Framework.

This backend provides APIs for:

- User authentication
- Job posting
- Job search & filtering
- Job applications

The system follows REST API architecture and uses JWT authentication for secure access.

---

🚀 Features

- User Registration
- User Login Authentication
- JWT Token Authentication
- Create Job Posting
- View Job Listings
- Job Search by Title
- Job Filter by Location
- Apply for Jobs
- View Job Applications
- RESTful API Architecture

---

🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite Database
- Git & GitHub

---

📂 Project Structure

jobportal/
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── jobs/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── applications/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── jobportal/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── manage.py
└── requirements.txt

---

🔐 Authentication

This project uses JWT (JSON Web Token) authentication.

Generate Token

POST /api/token/

Example Response:

{
 "refresh": "your_refresh_token",
 "access": "your_access_token"
}

Use Token in Request Header

Authorization: Bearer <access_token>

---

📡 API Endpoints

User APIs

Method| Endpoint| Description
POST| "/api/register/"| Register a new user
POST| "/api/login/"| Login user
POST| "/api/token/"| Get JWT token

---

Job APIs

Method| Endpoint| Description
GET| "/api/jobs/"| View all jobs
POST| "/api/create-job/"| Create a job posting
GET| "/api/jobs/?search=python"| Search jobs by title
GET| "/api/jobs/?location=hyderabad"| Filter jobs by location

---

Application APIs

Method| Endpoint| Description
POST| "/api/apply/"| Apply for a job
GET| "/api/applications/"| View all applications
GET| "/api/my-applications/"| View user applications

---

▶️ How to Run the Project

1️⃣ Clone the Repository

git clone https://github.com/yourusername/job-portal-backend.git

2️⃣ Navigate to Project Folder

cd jobportal

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run Migrations

python manage.py migrate

5️⃣ Start Development Server

python manage.py runserver

---

🌐 Server URL

http://127.0.0.1:8000

---

📌 Future Improvements

- Pagination for job listings
- Email notifications for job applications
- Role-based authentication
- Admin dashboard
- Deployment to cloud platforms (AWS / Render)

---

👩‍💻 Author

Vidya Kadakol

Python | Django | Backend Developer | API Testing

GitHub Profile
https://github.com/vidyakadakol-oss

---

⭐ Contribution

Contributions are welcome.

If you would like to improve the project, feel free to fork the repository and submit a pull request.
