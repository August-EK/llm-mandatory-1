DEPLOYMENT.md checklist for running a Flask API locally
=========================================================

Environment setup
-----------------

* Install Python on `your_system`. You can download Python from the official website: <https://www.python.org/downloads/>.
* Install pip by running the following command in the terminal or command prompt:
```
pip install python
```
* Download the Flask framework by running the following command in the terminal or command prompt:
```
pip install flask
```
Setup environment variables
-------------------------

* Set working directory to your project folder. For example, run the following command in the terminal or command prompt if your "app\_directory" folder is located on the desktop:
```
cd /Users/your_username/Desktop/app_directory/
```
* Set two environment variables: FLASK\_APP and FLASK\_DEBUG. These environment variables will allow you to run your Flask application in development mode without opening the web browser if you don't want to do so. Run the following command in the terminal or command prompt to set these variables:
```
export FLASK_APP=app.py
export FLASK_DEBUG=true
```
Starting the Flask API
----------------------

1. Open two terminal windows/tabs.
2. In one of the terminal windows/tabs, run the following command to start your Flask API:
```
flask run --host 0.0.0.0 --port 5000
```
3. The Flask API will start on the port `5000`. You can use any IP address and port in this step but it should not be equal to `127.0.0.1` as its localhost and not accessible.
4. Run the following command in the other terminal window/tab, to test your Flask API by accessing the endpoints:
```
curl http://your_system:5000 -X GET http://your_system/tasks -H "Content-Type: application/json"
```
This will use the GET method and send a request to `http://your_system:5000/tasks`, which is your Flask API endpoint. The response will be displayed in the terminal window.

Three things to change before production
--------------------------------------------

1. Install a package like `requests` or `flasgger` that can help you test your Flask API endpoints using Python script, this package allows you to make requests from server to test the response.
2. Use an environment variables manager, like `python-dotenv`, to store and manage your environment variables for production. This way you have separate configuration for development and production environments.
3. Use a containerization tool, like Docker, to package your Flask API with all its dependencies into a single deployable unit: this way you can easily deploy your Flask API on different cloud providers or server hosting services.

To get started with Docker, you'll need to create a `Dockerfile` and then run the following command in the terminal window/tab containing your Flask API:
```bash
docker-compose up -d
```
This will start a new container running your Flask API on `5001`, `localhost` and you can access it by using `http://localhost:5001`. The same command also starts a new container with the environment variables set to production.