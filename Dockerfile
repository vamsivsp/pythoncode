FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y
RUN pip3 install flask
COPY ./app.py /app.py
ENTRYPOINT python3 app.py