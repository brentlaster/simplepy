# simplepy
This is a simple Python Flask application that can run in a container.
It has a home page, a login page where a user can login, a user welcome page, and a generic error page.

### Build application
You can build the container image manually by cloning the Git repo.
```
$ git clone https://github.com/brentlaster/simplepy.git
$ docker build -t simplepy:1.0 .
```

### Download precreated image
You can download an existing image from [DockerHub](https://hub.docker.com/r/brentlaster/simplepy/).
```
docker pull brentlaster/simplepy
```

### Run the container
First, create a container from the image.
```
$ docker run --name your-container-name -d -p 8080:8080 brentlaster/simplepy
```

Now visit http://localhost:8081


