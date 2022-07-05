# Shiritor.io 

## Development Instructions
The development environment is setup using two docker containers, one for the frontend and one for the backend, which are linked together using `docker-compose`. The frontend is hosted on port 7000, and the backend is hosted on port 5000. 

## Starting the container
```bash
docker-compose build
docker-compose up
```

After you've built the container once, it will auto-refresh with any changes that are made to the code, and you will only need to run `docker-compose up`. 

If you want to install any new backend packages, you will have to rebuild the environment using `docker-compose build`. 

If you want to install any new frontend packages, you can either install the packages within the container using `docker-compose exec frontend npm install`, or you can rebuild the environment without a cache using `docker-compose rm -f; docker-compose build --no-cache`. 
