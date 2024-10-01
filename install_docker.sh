#!/usr/bin/sh
sudo yum update -y
sudo yum install docker -y
# sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chmod 666 /var/run/docker.sock
