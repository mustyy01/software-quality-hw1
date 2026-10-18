# Software Quality Standards HW-2: Containerize a Small App

A small Flask web application packaged with Docker. It demonstrates pinned dependency versions, a cache-friendly Dockerfile, a non-root runtime user, a health check, and a documented clean build/run workflow.

## Requirements

- Git
- Docker Engine or Docker Desktop
- Python 3.12+ (only needed to run tests outside Docker)

## Project structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env.example
├── README.md
└── tests/
    └── test_app.py
```

## Build the image

From the repository root:

```bash
docker build --no-cache -t software-quality-flask:1.0.0 .
```

The Python base image and Python packages are version-pinned. The Dockerfile installs dependencies before copying the application source so source-only changes can reuse the dependency layer.

## Run the container

```bash
docker run --detach --name software-quality-flask --publish 5000:5000 software-quality-flask:1.0.0
```

Open <http://localhost:5000> in a browser. The health endpoint is <http://localhost:5000/health> and should return:

```json
{"status":"ok"}
```

Check container status and health:

```bash
docker ps
docker inspect --format='{{.State.Health.Status}}' software-quality-flask
docker logs software-quality-flask
```

Stop and remove the container:

```bash
docker stop software-quality-flask
docker rm software-quality-flask
```

## Run tests locally

Create and activate a virtual environment, then install the pinned requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Verify the security requirements

Confirm the container uses a non-root user:

```bash
docker exec software-quality-flask id
```

The output should show UID `10001`, not UID `0`. (Run this before stopping/removing the container.)

Check the image configuration:

```bash
docker image inspect software-quality-flask:1.0.0 --format='User={{.Config.User}}'
```

Expected output: `User=10001:10001`.

No credentials or API keys are needed. Do not commit real `.env` files, private keys, access tokens, or passwords.

## Clean-clone verification

To test the repository as a marker might:

```bash
git clone <YOUR_REPOSITORY_URL> clean-check
cd clean-check
docker build --no-cache -t software-quality-flask:1.0.0 .
docker run --detach --name software-quality-flask --publish 5000:5000 software-quality-flask:1.0.0
```

Then visit `http://localhost:5000` and `http://localhost:5000/health`. Replace `<YOUR_REPOSITORY_URL>` with your actual Git repository URL.

## Notes on data persistence

This demo does not store user data. In a stateful application, data that must survive container removal should be stored in a Docker volume, a host bind mount, or an external database with suitable backups.

## Reproducibility note

Image tags and package versions are pinned to explicit versions rather than `latest`. For stronger supply-chain reproducibility, a deployment can pin the base image by its verified digest and use a generated, audited dependency lock file.
