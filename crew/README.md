# Flask To-Do List API

A minimal REST API for managing tasks, built with Python and Flask. Tasks are stored in memory and reset on restart.

---

## Prerequisites

- Python 3.11 or newer
- pip

---

## Installation

```bash
# Navigate to the project folder
cd crewai-todo

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install flask pytest
```

---

## Run the API

```bash
python app.py
```

The API starts at `http://localhost:5000`

---

## Endpoints

### Get all tasks
```
GET /tasks
```
**Response:**
```json
[
  {"id": 1, "title": "Buy milk"}
]
```

---

### Get a single task
```
GET /tasks/<id>
```
**Response:**
```json
{"id": 1, "title": "Buy milk"}
```

---

### Create a task
```
POST /tasks
Content-Type: application/json

{"title": "Buy milk"}
```
**Response:**
```json
{"task_id": 1}
```

---

### Update a task
```
PUT /tasks/<id>
Content-Type: application/json

{"title": "Buy bread"}
```
**Response:**
```json
{"id": 1, "title": "Buy bread"}
```

---

### Delete a task
```
DELETE /tasks/<id>
```
**Response:** `204 No Content`

---

## Run Tests

```bash
pytest test_app.py -v
```

Expected output:
```
6 passed in 0.13s
```

---

## Project Structure

```
crewai-todo/
├── app.py          # Flask API
├── test_app.py     # Pytest tests
├── README.md       # This file
└── DEPLOYMENT.md   # Deployment checklist
```

---

## Note

Tasks are stored in memory and will be lost when the server restarts. See DEPLOYMENT.md for guidance on production deployment.