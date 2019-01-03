FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install build-essential lsb-release #For bash, lsb_release -a
RUN apt-get -y install python3-pip
RUN apt-get -y install vim 

WORKDIR /home/python-requirements
COPY python-requirements/requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /home

CMD ["bash"] 
