Homework 2 — Written Answers

1. Your app calls the second service by name. How does that work, and why does the same name not work between two containers on the default Docker bridge network?

My Flask app connects to Redis using the name redis because Docker Compose puts both services on the same network. Docker automatically helps the app find Redis using that name instead of an IP address. On the default Docker bridge network, containers cannot automatically find each other by name like this unless extra configuration is used.

2. Which of your services is stateless and which is not? Show the evidence: what did you do, and what happened to your data?

My Flask app is stateless because it does not save the visit counter inside its own container. Redis is stateful because it stores the counter. I tested this by increasing the counter, stopping the containers with docker compose down, and starting them again. The counter continued from its previous value because Redis uses a named Docker volume. When the volume is removed using docker compose down -v, the saved counter is deleted.

3. Where should a database password come from, and why is it a problem to commit it to Git, even in a private repository?

A database password should come from an environment variable or a secret management system instead of being written directly in the code. It is not safe to commit passwords to Git because someone could access them through the repository or its history. Even if the repository is private, the password could still be exposed if access is shared or the repository becomes public.

How I Used AI Assistance

I used ChatGPT to help me understand the Docker Compose requirements and guide me through the setup and testing process. I also used it to help explain some concepts, while checking the application and its results myself.