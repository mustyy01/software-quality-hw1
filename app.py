import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Containerized Flask App</title>
  <style>
    :root { color-scheme: light; }
    body { font-family: system-ui, sans-serif; margin: 0; background: #f3f6fb; color: #172033; }
    main { max-width: 720px; margin: 10vh auto; padding: 2rem; }
    section { background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 8px 28px #17203312; }
    h1 { margin-top: 0; }
    .status { display: inline-block; padding: .35rem .7rem; border-radius: 999px; background: #e1f8e8; color: #176b35; font-weight: 700; }
    code { background: #edf0f6; padding: .15rem .35rem; border-radius: 4px; }
  </style>
</head>
<body>
  <main><section>
    <p class="status">Application is running</p>
    <h1>My Software Quality Project</h1>
    <p>This project demonstrates how to package a Flask web application in a Docker container and verify that it runs correctly.</p>
       pinned Python dependencies, and a non-root runtime user.</p>
    <p>Health check: <code>/health</code></p>
  </section></main>
</body>
</html>
"""

@app.get("/")
def index():
    return render_template_string(HTML)

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    # Useful for local development. Production container uses Gunicorn.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)
