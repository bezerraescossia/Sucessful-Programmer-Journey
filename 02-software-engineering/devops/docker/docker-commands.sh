#!/bin/bash

# Run node docker, if docker don't find it locally
# it will download from docker hub.
docker run node

# Expose only running processes
docker ps

# Expose all processes, even the ones already finished.
docker ps -a

# Run the docker image in iterative mode, meaning that
# it will open the container on terminal.
docker run -it node

# Build a Dockerfile contained in current directory.
docker build .

# Stop a running container
docker stop container_name

# Run exposing a port to localhost
docker run -p 3000:80 image_name

# Run on dettach mode
docker run -d image_name

# Start a container on dettach mode
docker start container_name

# Attach um container em execução
docker attach container_name

# Visualize o log de um container
docker logs container_name

# Visualize o log e mantenha-se ouvindo o log (attach mode)
docker logs -f container_name

# Run an image on iteractive and tty mode
docker run -i -t image_name

# Start a container on iteractive and attach mode
docker start -i -a

# Remove multiple containers at once
docker rm container_name1 container_name2 ...

# Remove multiple images at once
docker rmi image_name1 image_2 ...

# Remove all images without associated containers
docker image prune

# Run an image that is automatically removed after stopped
docker run -p 3000:80 -d --rm image_name

# 
docker image inspect image_name