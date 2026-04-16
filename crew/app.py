from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = {}

@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    return jsonify(list(tasks.values())), 200

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(tasks[task_id]), 200

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Invalid request"}), 400
    task_id = len(tasks) + 1
    tasks[task_id] = {"id": task_id, "title": data["title"]}
    return jsonify({"task_id": task_id}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Invalid request"}), 400
    tasks[task_id]["title"] = data["title"]
    return jsonify(tasks[task_id]), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    del tasks[task_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
