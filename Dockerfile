# Pin the Python version and Debian release for more predictable builds.
FROM python:3.12.8-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

WORKDIR /app

# Install pinned dependencies before copying source so this layer can be cached.
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip==24.3.1 \
    && pip install --no-cache-dir -r requirements.txt

# Copy only the application code after dependencies have been installed.
COPY app.py .

# Run the application as an unprivileged user.
RUN useradd --system --no-create-home --uid 10001 appuser \
    && chown -R appuser:appuser /app
USER 10001:10001

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health', timeout=2)" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
