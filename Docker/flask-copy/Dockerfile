FROM python

WORKDIR /home

COPY ./ ./

RUN apt-get update
RUN apt-get -y install vim 
RUN pip install -r requirements.txt

CMD ["python","main.py"] 
