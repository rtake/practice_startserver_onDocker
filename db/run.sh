#! /bin/bash

# build image from Dockerfile
docker build . -t database

# start db
docker run --name db -e MYSQL_ROOT_PASSWORD=my-secret-pw -d db
