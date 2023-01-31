#! /bin/bash

# start 
docker-compose build
docker-compose up -d

# check
curl http://localhost

# stop containers
docker-compose down