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
