# Football Team Management System ⚽

This is a **Full-Stack Distributed Application** developed as part of the Systems Engineering curriculum at **Universidad Central del Ecuador**. The project demonstrates a containerized architecture using Docker, integrating a Flask backend, a React frontend, and a PostgreSQL database.

---

## 🚀 Architecture Overview

The system is composed of three main services orchestrated by Docker Compose:

- **Frontend**: Built with **React (Vite)** and **Tailwind CSS v4**, providing a responsive and modern UI.
- **Backend**: A **Python Flask** API that handles business logic, database persistence, and external service integration.
- **Database**: A **PostgreSQL** instance for local data storage.
- **External API**: Integration with `football-data.org` to fetch real-time Premier League data.

---

## 🛠️ Technologies Used

| Layer        | Technology                               |
| ------------ | ---------------------------------------- |
| **Frontend** | React 18, Tailwind CSS v4, Vite          |
| **Backend**  | Python 3.11, Flask, SQLAlchemy, Requests |
| **Database** | PostgreSQL 15                            |
| **DevOps**   | Docker, Docker Compose                   |

---

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)
- An API Key from [football-data.org](https://www.football-data.org/)

---

## ⚙️ Setup & Installation

### 1. Environment Configuration

Create a `.env` file in the **root directory** of the project and provide your credentials:

```text
# Database Configuration
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=football_db
DATABASE_URL=postgresql://user:password@db:5432/football_db

# External API Configuration
FOOTBALL_API_KEY=your_api_key_here
```

---

### 2. Run with Docker Compose

From the root directory, execute the following command:

```bash
docker-compose up --build
```

---

### 3. Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5000

---

## 🧪 API Endpoints

### External API Integration

- `GET /api/external-teams` → Fetches Premier League teams from the external provider.

### Local CRUD Operations (PostgreSQL)

- `GET /api/teams` → Retrieves all teams stored in the local database.
- `POST /api/teams` → Adds a new team to the database.
- `DELETE /api/teams/<id>` → Deletes a team by ID.

---

## 📂 Project Structure

```text
.
├── backend/
│   ├── app.py             # Main Flask application & routes
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Backend container definition
├── frontend/
│   ├── src/               # React components and logic
│   ├── vite.config.js     # Vite & Tailwind v4 configuration
│   └── Dockerfile         # Frontend container definition
├── docker-compose.yml     # Service orchestration
└── .env                   # Environment variables (Git ignored)
```

---

## 🔄 Final Step (Git)

```bash
git add README.md
git commit -m "docs: add professional README in English"
git push origin develop
```

---

## 👤 Author

**Jessiel JD**  
_Systems Engineering Student_  
_Universidad Central del Ecuador_
