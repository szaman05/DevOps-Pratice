# Docker Cheat Sheet:

1.  Run vprodb in detach mode with argument map port to 3030 mount
    directory.

```

#with directory binding:

docker container run --name vprodb -d -e MYSQL_ROOT_PASSWORD=secretpass
-p 3030:3306 -v /home/ec2-user/vprodbdata:/var/lib/mysql mysql:5.7

#with volume mount:

docker run --name vprodb -d -e MYSQL_ROOT_PASSWORD=secretpass -p
3030:3306 -v vprodb:/var/lib/mysql mysql:5.7

```

2.  SSH to container:

```

docker exec -it vprodb /bin/bash

```

3.  Show docker image information in json format:

```

docker inspect mysql:5.7

```

4.  Docker Volume:

```

docker volume create vprodb #Create Volume

docker volume ls # show volume

docker volume inspect vprodb # describe volume

```

5.  Dockerfile:

```

FROM ubuntu:latest

LABEL "Author"="Sohel"

LABEL "Project"="Demo"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install git -y

RUN apt install apache2 -y

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80

WORKDIR /var/www/html

VOLUME /var/log/apache2

ADD nano.tar.gz /var/www/html

```
