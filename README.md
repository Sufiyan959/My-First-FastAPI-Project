# 🚀 My First FastAPI Project

A modern, production-ready REST API built with **FastAPI** and **PostgreSQL**, featuring user management and task tracking with database migrations.

---

## ✨ Features

- 🔐 **User Management** - Create and manage users with password security
- ✅ **Task Tracking** - Create, read, update, and delete tasks
- 🔄 **Database Migrations** - Automated schema management with Alembic
- 📝 **API Documentation** - Auto-generated interactive API docs (Swagger UI)
- 🛡️ **Type Safety** - Full type hints with Pydantic validation
- 🐘 **PostgreSQL** - Robust relational database support

---

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Migrations](#database-migrations)
- [Project Architecture](#project-architecture)

---

## 📁 Project Structure

```
My First FastAPI Project/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── alembic.ini            # Alembic configuration
├── env/                   # Python virtual environment
├── migrations/            # Database migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions/          # Migration files
└── src/
    ├── user/              # User module
    │   ├── model.py       # User database model
    │   ├── dtos.py        # Data transfer objects
    │   ├── controller.py  # Business logic
    │   └── router.py      # API endpoints
    ├── tasks/             # Tasks module
    │   ├── model.py       # Task database model
    │   ├── dtos.py        # Data transfer objects
    │   ├── controller.py  # Business logic
    │   └── router.py      # API endpoints
    └── utils/
        ├── db.py          # Database configuration
        ├── settings.py    # Application settings
        └── helper.py      # Helper functions
```

---

## 📦 Prerequisites

- **Python** 3.8 or higher
- **PostgreSQL** 12 or higher
- **pip** (Python package manager)

---

## 🔧 Setup & Installation

### 1. Clone or Navigate to Project

```bash
cd "My First FastAPI Project"
```

### 2. Create Virtual Environment

**On Windows:**
```bash
python -m venv env
.\env\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Create a `.env` file in the project root with the following variables:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/your_database

# Application Settings
DEBUG=True
ENVIRONMENT=development

# Security
SECRET_KEY=your-secret-key-here
```

Update `src/utils/settings.py` if needed with your specific configuration values.

---

## 🚀 Running the Application

### Development Server

```bash
uvicorn main:app --reload
```

The API will be available at: **http://localhost:8000**

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📡 API Endpoints

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/users` | Get all users |
| `GET` | `/users/{id}` | Get user by ID |
| `POST` | `/users` | Create new user |
| `PUT` | `/users/{id}` | Update user |
| `DELETE` | `/users/{id}` | Delete user |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | Get all tasks |
| `GET` | `/tasks/{id}` | Get task by ID |
| `POST` | `/tasks` | Create new task |
| `PUT` | `/tasks/{id}` | Update task |
| `DELETE` | `/tasks/{id}` | Delete task |

---

## 🗄️ Database Migrations

### Initialize Database

```bash
alembic upgrade head
```

### Create Migration

```bash
alembic revision --autogenerate -m "description of changes"
```

### View Migration History

```bash
alembic history
```

### Rollback Migration

```bash
alembic downgrade -1
```

---

## 🏗️ Project Architecture

### Modular Design

The project follows a **modular architecture** with separated concerns:

- **Models** (`model.py`) - Database schema definitions
- **DTOs** (`dtos.py`) - Request/response validation schemas
- **Controllers** (`controller.py`) - Business logic and database operations
- **Routers** (`router.py`) - API endpoint definitions

### Database Layer

- Uses **SQLAlchemy** ORM for type-safe database queries
- **Alembic** for version-controlled schema migrations
- **PostgreSQL** for reliable data persistence

---

## 🔒 Security Considerations

- ✅ Use environment variables for sensitive data (never commit `.env` files)
- ✅ Implement authentication/authorization for protected endpoints
- ✅ Hash passwords using secure algorithms (e.g., Argon2)
- ✅ Validate all user inputs through Pydantic models
- ✅ Use HTTPS in production

---

## 📚 Dependencies

Main packages used in this project:

- **FastAPI** - Modern web framework
- **SQLAlchemy** - Object-relational mapper
- **Alembic** - Database migration tool
- **Pydantic** - Data validation and settings management
- **psycopg2** - PostgreSQL adapter
- **Uvicorn** - ASGI server

See `requirements.txt` for complete list with versions.

---

## 🛠️ Development Tips

### Enable Auto-reload
The `--reload` flag automatically restarts the server when you save changes:

```bash
uvicorn main:app --reload
```

### Debug Mode
Set `DEBUG=True` in your `.env` file for detailed error messages.

### Database Debugging
Use Alembic's revision history to track all schema changes:

```bash
alembic history --indicate-current
```

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

---

## 📧 Support

For questions or issues, please open an issue in the repository or contact the development team.

---

**Made with ❤️ using FastAPI**
