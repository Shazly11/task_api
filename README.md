# ask Manager API – Computer Science Graduate Edition

This project is a simple RESTful API built using FastAPI.  
It helps a Computer Science graduate organize personal learning goals and track technical tasks effectively.

---

## Technologies Used

- Python 3.11
- FastAPI
- SQLModel
- Uvicorn

---

## Quick Start

### Installation

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Run the Application

To start the FastAPI application, run:

```bash
python main.py
```

# Access API documentation

http://127.0.0.1:8000/docs

## Example API Call (cURL)

You can test the API by creating a sample task using this cURL command:

```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Task", "priority": "high"}'
```

---

## Core Endpoints

| Method | Endpoint                          | Description                  |
|--------|-----------------------------------|------------------------------|
| POST   | `/tasks`                          | Create a new task            |
| GET    | `/tasks`                          | Get all tasks                |
| GET    | `/tasks/{id}`                     | Get a task by ID             |
| PUT    | `/tasks/{id}`                     | Update a task                |
| DELETE | `/tasks/{id}`                     | Delete a task                |
| GET    | `/tasks/status/{status}`          | Filter tasks by status       |
| GET    | `/tasks/priority/{priority}`      | Filter tasks by priority     |

---

## Sample Task Example

```json
{
  "title": "Build portfolio website",
  "description": "Create personal website with projects and contact info",
  "status": "pending",
  "priority": "high",
  "due_date": "2025-06-30:00:00",
  "assigned_to": "Shazli - CS Graduate"
}
```

---

## Project Purpose

This system helps a CS graduate:

- Track self-learning tasks  
- Prepare for technical interviews  
- Manage progress in small projects  
- Stay organized and consistent  

---

## Notes

- Data is stored in-memory (not persistent)  
- The goal is to demonstrate FastAPI fundamentals  
- All validation and business logic is clean and beginner-friendly  

---

## Developer

**Shazli**  
Computer Science Graduate