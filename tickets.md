
Implementation Ticket 1: Implement the API endpoint for getting all tasks.
Title: Get All Tasks API Endpoint
Scope:

* Create an HTTP GET endpoint at `/tasks`
* Handle requests with no task ID in the URL path and return a JSON response containing all tasks from `tasks.json` file
* Return a status code of 200 for successful requests and a JSON error response with an appropriate "error" message for errors

1-line Definition of Done: The API endpoint is functional, returning a JSON response containing all tasks when called.

Implementation Ticket 2: Implement the API endpoint for deleting a task.
Title: Delete Task API Endpoint
Scope:

* Create an HTTP DELETE endpoint at `/tasks/<int:task_id>`
* Handle requests with the correct task ID included in the URL path and remove the corresponding task from the `tasks.json` file
* Return a status code of 204 for successful requests and a JSON error response with an appropriate "error" message if the task is not found

1-line Definition of Done: The API endpoint is functional, removing tasks from the data file when called with the correct ID.

Implementation Ticket 3: Implement the API endpoint for updating a task.
Title: Update Task API Endpoint
Scope:

* Create an HTTP PUT endpoint at `/tasks/<int:task_id>`
* Handle requests with the correct task ID included in the URL path and process the JSON payload data in request to update the title of the corresponding task in `tasks.json` file
* Return a status code of 200 for successful requests and a JSON error response with an appropriate "error" message if the task is not found or the request payload does not contain 'title' key

1-line Definition of Done: The API endpoint is functional, updating the title of tasks when called with the correct ID and 'title' key in request payload.

Implementation Ticket 4: Implement the API endpoint for adding a task.
Title: Add Task API Endpoint
Scope:

* Create an HTTP POST endpoint at `/tasks`
* Handle requests with a JSON payload containing 'title