FROM ubuntu:18.04
RUN apt-get -y update
RUN apt-get install build-essential libssl-dev libffi-dev python3-dev -y
RUN apt-get install python3-venv -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-setuptools -y
RUN apt-get -y install cron
#RUN pip3 install --upgrade pip
#RUN pip3 install setuptools
#RUN pip3 install setuptools_rust
#RUN pip3 install cryptography

RUN adduser fakie

WORKDIR /home/fakie

COPY requirements.txt requirements.txt

RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY fakie.py config.py boot.sh ./
RUN mkdir uploads
COPY uploads/testCEF.txt uploads/testCEF.txt
COPY uploads/testJson.json uploads/testJson.json
RUN chmod +x boot.sh
RUN chmod 770 uploads

COPY hello-cron /etc/cron.d/hello-cron
RUN chmod 0644 /etc/cron.d/hello-cron
RUN touch /var/log/cron.log
ENV FLASK_APP fakie.py

RUN crontab /etc/cron.d/hello-cron

RUN chown -R fakie:fakie ./
#USER fakie

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
