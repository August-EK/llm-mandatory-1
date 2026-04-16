To design a minimal Flask To-Do List REST API, we will need the following files:

1. app.py - This file will contain the main application logic and setup for our Flask app.
2. models.py - This file will define the database models used in our app, specifically the To-Do item model.
3. schemas.py - This file will define the serialization/deserialization schema for our To-Do items.
4. routes.py - This file will define the API endpoints and their corresponding handler functions.
5. config.py - This file will contain configuration settings for our app, such as database connection details.

The following is a list of the endpoints needed for a basic To-Do List REST API:

1. GET /todos - Retrieve all To-Do items
2. POST /todos - Create a new To-Do item
3. GET /todos/{id} - Retrieve a specific To-Do item by ID
4. PUT /todos/{id} - Update a specific To-Do item by ID
5. DELETE /todos/{id} - Delete a specific To-Do item by ID

Note that this is just a basic implementation and additional features such as user authentication and authorization may be necessary depending on the requirements of the application.