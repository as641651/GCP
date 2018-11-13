FROM python:3.7.1-alpine3.7

RUN pip install flask==1.0.2
RUN pip install redis

WORKDIR /home
COPY ./ ./
 
CMD ["python","main.py"] 
