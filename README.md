# docker_flask_homework
This assignment aims to provide hands-on experience in Dockerizing Flask applications, first individually and then using Docker Compose for managing multiple applications.

# Documentation for Part 1: Dockerizing a Single Flask Application
- Create script for flask application, requirements.txt file containing flask, and a Dockerfile
- Dockerfile should follow here: 
```
FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
```

### To dockerize a file
- Build an image using ```docker build -t <name> ```
- Run docker file, using ```docker run -p [host-port]:[container-port] <name>```. For this assignment, I used ```docker run -p 5000:5000 <name>.```
- Stop running docker using ```docker stop <container id>``` 

### Additional  essential docker commands include
- ```docker images``` to list images
- ```docker ps``` to list containers
- ```docker rm <container id>``` to remove a container
- ```docker system prune -a -f``` to clean and remove everything

# Documentation for Part 2: Multi_Container Setup with Docker Compose
- Create 2 folders titled flask1 asnd flask2

### Flask folders should consist of:
- Dockerfile in both folders should be the same:
```
version: '3'                [version of Docker Compose file]
services:                   [services that make application (flask_app_1, flask_app_2)]
  flask_app_1:              [name of service]
    build: ./flask1         [location of dockerfile for building the docker image]
    ports:                  [port the service can be hosted]
      - "5001:5000"
    volumes:                [map directory of application in container]
      - ./flask1:/app
  flask_app_2:
    build: ./flask2
    ports:
      - "5002:5000"
    volumes:
      - ./flask2:/app
```
- Python app.py file
- requirements.txt with flask
- Flask 2 should include a ```docker-compose.yml``` file:

- Build images using ```docker-compose up--build```
- Run containers using ```docker-compose up```
- Stop containers using ```docker-compose down```
- View containers using ```docker-compose ps```

### Role of Docker Compose
- Dockercompose is a tool to run multiple-containers of Docker applications in a single file. This makes it easier to manage multiple containers that work together into a single application. WHen making changes using DOcker alone, you need to specify the individual containers rather than 1 file like ```docker-compose.yml```. 