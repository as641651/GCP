#Add camera device to docker
#To find out where the camera is located
#sudo apt-get install v4l-utils
#v4l2-ctl --list-devices
docker run -it -p 0.0.0.0:8000:8888 -p 0.0.0.0:6005:6006 -v ${1:-$PWD}:/home  --device /dev/video0 --runtime=nvidia senesence/docker-webcam
