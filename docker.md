```Bash
docker version # check your version and docker that is running
docker info # most config values
docker container run image_name
docker container stop [container_name]
docker container rm [container_name]
docker container logs [container_name]
docker container ls
docker container top [container_name] # process list in one container
docker container inspect [container_name] # details of one container
docker container stats # performance stats for all containers
docker network create [net_name] # create a virtual network
docker image inspect/history [image_name] # show the spec of the image
docker image tag [source_image] [target_image] # create a tag target_image that refers to source_image
docker volume ls # show all the volume
docker-compose up
```

## example
```Bash
# run Apache on host port 80, forward to port 80 on docker
docker container run -d --name websever -p 80:80 httpd

# use bash in an interactive way to run container
# docker container stop when you leave bash
docker container run -it --name webserver -p 80:80 bash

# start a new container interactively
docker container run -ai webserver 

# run additional command in an existing container
docker container exec -it websever bash

# create a virtual network "my_net"
docker network create my_net

# create a elasticsearch container, and attach this to "my_net" virtual network, and have a DNS alias name "search"
docker container run --net my_net --net-alias search elasticsearch:2

# create a mysql container, and named volume
docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v mysql-db:/var/lib/mysql mysql

# create a mysql container, and have a bind mount(bind the current directory to /var/lib/mysql in the container)
docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v $(pwd):/var/lib/mysql mysql
```

## Dockerfile
1. `FROM`:import an image 
2. `ENV`: set environment variable
3. `RUN`: execute shell command
4. `CMD`: run the command when container is launched
