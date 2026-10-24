Software Quality Standards HW-2: Flask and Redis with Docker Compose

Project Overview

This project is a small Flask web application that uses Redis to keep track of how many times the /visits page has been opened.

Docker Compose runs the Flask application and Redis together. Redis stores the visit counter in a persistent Docker volume so the data is not lost when the containers are stopped and removed normally.

Requirements

* Docker Desktop or Docker Engine with Docker Compose
* Git

Project Files

* app.py — Flask application and Redis connection
* Dockerfile — Instructions for building the Flask container
* compose.yaml — Starts the Flask and Redis services
* requirements.txt — Python dependencies
* tests/test_app.py — Application tests
* ANSWERS.md — Three short written answers
* .dockerignore — Excludes unnecessary files from the Docker build
* .env.example — Example environment configuration

How to Run the Application

Open a terminal in the project folder.

Build and start both services using one command:

docker compose up -d --build

Docker Compose starts the Flask application and Redis.

Open the following pages in your browser:

* http://localhost:5000/ — Home page
* http://localhost:5000/health — Application health check
* http://localhost:5000/visits — Redis visit counter

Refresh the /visits page to increase the counter.

Check Container Status

Run:

docker compose ps

This displays the running Flask and Redis containers.

Data Persistence

The Redis visit counter is stored in a named Docker volume.

Stop and remove the containers using:

docker compose down

Restart the application:

docker compose up -d

Open /visits again. The counter should continue increasing rather than starting from zero.

Do not use docker compose down -v when you want to preserve the stored data. The -v option removes the project’s named volumes.

Security and Reproducibility

The Flask application runs as a non-root user inside its Docker container.

The Docker configuration uses pinned image versions rather than relying on the latest tag. This helps make builds more predictable.

Running Tests

Activate the project’s Python virtual environment and install the dependencies.

Then run:

python -m unittest discover -s tests -v

Stopping the Application

To stop and remove the running containers while keeping the persistent Redis volume:

docker compose down

Written Answers

The three short written answers are included in ANSWERS.md.