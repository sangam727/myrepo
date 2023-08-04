FROM nginx:latest
LABLE version="0.0.1"
LABEL maintainer="shewale.sangam@gmail.com"
WORKDIR /usr/share/nginx/html
COPY index.html index.html


# command for build image from Dockerfile 
# docker build -t customnginx:0.0.1 . 
# Docker file for httpd on centos 7
#FROM centos:centos7
#RUN yum -y update
#RUN yum -y install httpd
#COPY html/* /var/www/html/
#EXPOSE 80
#CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
