# docker_emporium_sdv7
## sdv701 project ready for docker

### Requirements
- Visual Studio Code
- Docker Desktop

### Instructions on how to deploy to Docker locally
0. Clone repo to your machine
```git clone https://github.com/Phillip-D-Shields/docker_emporium_sdv7.git```

1. Open directory with VS Code
```cd docker_emporium_sdv7 && code .```

2. Build and start Docker containers
```docker-compose up```

> ### OPTIONAL - IF THE FIRST DEPLOYMENT ONLY SUCCESSFULLY LAUNCHES 1 of 2 CONTAINERS
4. Stop and exit Docker containers (press CTRL + C)

5. Relaunch Docker containers
```docker-compose up```

Not sure why this occurs, but a successful message should appear after the relaunch

### Access the live project

Shop Clinet can be accessed via: ```http://localhost:8000```

Admin UI can be accessed via: ```http://localhost:8000/admin```

API can be accessed via: ```http://localhost:8000/api```

#### Default Admin Credentials
*** change after launching the project ***

name: admin
password: P@ssw0rd1

*** this is a bad way to implement a default admin, i know.  ***