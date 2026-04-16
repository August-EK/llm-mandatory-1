
Here is a minimal Flask to-do list REST API design with just the necessary files and endpoints:
```python
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = {}  # Dictionary to store tasks as JSON objects

@app.route("/")
def hello():
    return 'Hello World!'

@app.route("/tasks")
@app.route("/tasks/<int:task_id>")
def get_task(task_id=None):
    if task_id is None:  # Return all tasks
        return jsonify(list(tasks.values()))
    return jsonify(tasks[task_id])

@app.route("/tasks", methods=["POST"])
def add_task():
    if request.get_json() is not None and 'title' in request.json:  # Validate input JSON
        title = request.json['title']
        task = {"title": title}  # Create new task and add it to tasks dictionary
        tasks[len(tasks)+1] = task
        return status_code(201), jsonify(task)
    else:  # Return 400 Bad Request error if invalid input
        return {'error': 'Invalid request'}, 400

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    if task_id in tasks and request.get_json() is not None and request.json.get('title') is not None:  # Validate input JSON
        tasks[task_id]['title'] = request.json['title']
        return jsonify(tasks[task_id]), 200
    else:  # Return 404 Not Found error if task not found or invalid data format
        return {'error': 'Task not found'}, 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id in tasks:  # Check that task exists before deleting it
        del tasks[task_id]
        return '', 204
    else:  # Return 404 Not Found error if task not found
        return {'error': 'Task not found'}, 404

if __name__ == "__main__":
    app.run(debug=True)
```

`tasks.json` (data file to store tasks as JSON objects, placed in the same directory as app.py):
```json
[
  {
    "title": "Task Title One"
  },
  {
    "title": "Task Title Two"
  }
]
```

Endpoints:

* `GET /` : Returns a welcome message
* `GET /tasks` or `GET /tasks/<int:task_id>` : Returns the current task list or the specific task using its ID. if no ID specified, it returns all tasks
* `POST /tasks` : Adds a new task to the list. The task title must be included in the request body as JSON data. Example: POST request JSON: `{ "title": "New Task" }`. Response includes the added task with a status code of 201, the response will also contain a newly created task with its ID and other information
* `PUT /tasks/<int:task_id>` : Updates an existing task with new title. The task ID must be provided in the URL and the request body must include a JSON payload with a updated 'title' value. Response includes the updated task with a status code of 200, the response will also contain the updated task with its ID
* `DELETE /tasks/<int:task_id>`: Deletes an existing task. The task ID must be provided in the URL and it will remove it from the