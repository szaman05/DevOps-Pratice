# Docker Cheat Sheet:

1.  Run vprodb in detach mode with argument map port to 3030 mount
    directory.

```

docker container run --name vprodb -d -e MYSQL_ROOT_PASSWORD=secretpass
-p 3030:3306 -v /home/ec2-user/vprodbdata:/var/lib/mysql mysql:5.7

```

2.  SSH to container:

```

docker exec -it vprodb /bin/bash

```
