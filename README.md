---

# Online Food Ordering Application Setup Guide

This guide will walk you through the steps to set up and run an online food ordering application using Docker, Flask, and SQLite.

## Prerequisites

Make sure you have Docker installed on your machine.

## 1. Create Dockerfile

Create a `Dockerfile` in the root directory of your project with the following content:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
```

## 2. Create app.py File

Create an `app.py` file in the root directory of your project. This file will contain your Flask application code.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

## 3. Create Templates Directory and index.html Page

Create a `templates` directory in the root of your project. Inside the `templates` directory, create an `index.html` file with your desired HTML content.

## 4. Create requirements.txt File

Create a `requirements.txt` file in the root directory and include the following line:

```
Flask==2.0.1
```

This specifies the Flask framework and its version as a dependency.

## 5. Build Docker Image

Open a terminal and navigate to the root directory of your project. Run the following command to build the Docker image:

```bash
docker build -t mypythonapp .
```

## 6. Run the Docker Container

Once the Docker image is built, you can run it as a container. Use the following command:

```bash
docker run -p 5000:5000 --name myfoodapp mypythonapp
```

This command maps port 5000 on your local machine to port 5000 in the Docker container and gives the container the name `myfoodapp`.

## 7. Access the Application

Visit `http://localhost:5000` in your web browser to access the online food ordering application.

## 8. Cleanup (Optional)

If you want to stop and remove the running container, use the following commands:

```bash
docker stop myfoodapp
docker rm myfoodapp
```

---

This guide provides a basic setup for your online food ordering application. Customize the `index.html` page and extend the functionality as needed. Enjoy exploring and enhancing your application!
