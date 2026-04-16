# To-Do List API with Flask

A simple To-Do List API using Flask. This project demonstrates how to create an API with basic CRUD (Create, Read, Update, Delete) operations for a To-Do list.

## Installation
First, you need to install Flask and Flask-SQLAlchemy if you haven't already:
```bash
pip install flask flask-sqlalchemy
```
Then clone this repository:
```bash
git clone https://github.com/yourusername/todo_list_api.git
cd todo_list_api
```

## Running the Application
To run the application, execute the following command in your terminal:
```bash
python app.py
```
Now open your browser and navigate to http://127.0.0.1:5000/ to see your To-Do List API in action.

## Endpoints
The API has the following endpoints:

- GET /todos: Retrieve all todos.
- POST /todos: Create a new todo.
- GET /todos/:id: Retrieve a specific todo by its ID.
- PUT /todos/:id: Update a specific todo by its ID.
- DELETE /todos/:id: Delete a specific todo by its ID.