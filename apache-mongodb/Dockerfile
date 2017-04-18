# Base image
FROM centos:centos6
MAINTAINER The CentOS Project <cloud-ops@centos.org>

#update packages on base image
RUN yum -y update; yum clean all
# install httpd rpm
RUN yum -y install httpd python-2.7* mongodb; yum clean all
RUN echo "Apache HTTPD" >> /var/www/html/index.html

# install mongodb
RUN yum -y install epel-release; yum clean all
RUN yum -y install mongodb-server; yum clean al

# expose port 8080
EXPOSE 8080

# Start the service
CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/httpd"]

# run following command to build this image : docker build -t <username>/centos-apache1 .
# run following command to run this container:  docker run -d -p <host_ip>:7080:8080 <image_id>
