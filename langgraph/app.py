```
from flask import Flask, jsonify, request
from models import TodoItem
from schemas import todo_item_schema, todos_schema

app = Flask(__name__)

# In-memory storage for To-Do items
todo_items = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(todos_schema.dump(todo_items))

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = TodoItem(request.json)
    todo_items.append(new_task)
    return jsonify(todo_item_schema.dump(new_task)), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in todo_items if task.id == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(todo_item_schema.dump(task))

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in todo_items if task.id == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task.update(request.json)
    return jsonify(todo_item_schema.dump(task))

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    todo_items = [task for task in todo_items if task.id != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)