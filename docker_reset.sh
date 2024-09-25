#!/bin/sh

docker-compose down
docker rmi $(docker images -aq)
