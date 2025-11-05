_# STEP 1
## Flask Hello World 
This is a simple P Flask application that returns "Hello, World!" when accessed.
## How to Run with Docker
## 1. Build the Docker image
docker-compose build
## 2.Check the app work online 
docker-compose up  
## 3.Check the images name because docker generate automaticly if not given
docker images    
## 4.Tag and push the image to docker HUB
docker tag project-flask-app thepankrat/flask-hello
docker push thepankrat/flask-hello 

# STEP 2
## 1.run the image in the background and checking local host : http://localhost:5000/
docker run -d -p 5000:5000 flask-hello

## volumes manggment for my simple app not needed but if needed need to add in docker compose 
volumes:
      - ./my_host_folder:/my_container_folder_

