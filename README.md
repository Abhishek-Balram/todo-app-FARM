# Todo app
A todo list web app I made using the FARM stack: FastAPI + React + MongoDB. 
I used Docker and Docker-compose to define services for frontend, backend, and mongoDB. These services work together to make a full-stack web application


#  Setup Guide

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Terminal or command prompt access.

## Starting the Application

1. **Open Terminal:**
   - Open a terminal window on your machine.

2. **Navigate to Directory:**
   - Change to the directory containing your `docker-compose.yml` file.
   - Use the command `cd /path/to/your/directory`.

3. **Run Docker Compose:**
   - Execute the following command to start the application:
     ```
     docker-compose up
     ```
   - This will start all services defined in the `docker-compose.yml`  (MongoDB, backend, frontend).
   - If you made any changes to the code, use the following command to rebuild the Docker images:
     ```
     docker-compose up --build
     ```

4. **Viewing Container Startup:**
   - Docker Compose will build and start the containers for each service.
   - Monitor the terminal output to see the progress.

5. **Accessing the Application:**
   - Once containers are up and running, access the frontend at: [http://localhost:3000](http://localhost:3000).
   - Access the backend at: [http://localhost:8000](http://localhost:8000).
   - MongoDB will be running in the background.

## Stopping the Application

- To stop the services and containers:
  - Press `Ctrl + C` in the terminal where Docker Compose is running.
  - This will gracefully stop all containers and services.
