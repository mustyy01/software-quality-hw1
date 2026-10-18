# Three short written answers

1. **Why did you put the instructions in this order?**  
   The Dockerfile installs dependencies before copying the application source. Since dependency files change less frequently than source code, Docker can reuse the dependency layer when only the source changes. This cache-friendly order reduces unnecessary work and speeds up rebuilds.

2. **What happens to your data when the container is removed, and how would you keep it?**  
   Data stored only in a container's writable filesystem is lost when the container is removed. I would preserve it with a Docker volume or bind mount, or store important application data in an external database with backups. This demo itself does not persist user data.

3. **Why is the `latest` tag a risk?**  
   The `latest` tag can point to different image versions at different times, so a rebuild may unexpectedly use changed software and behave differently. Pinning an explicit version, or a verified image digest for stronger reproducibility, makes builds more predictable.
