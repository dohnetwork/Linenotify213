FROM ubuntu:18.04
LABEL maintainer="dohnetwork@gmail.com"
LABEL description="Ubunta"
RUN apt-get -y update &&  DEBIAN_FRONTEND=noninteractive  apt-get install  -y  php python3 python-pip git  libmysqlclient-dev ftp nano cron \
            && mkdir /line /Data
            RUN pip install mysql-python
RUN chown -R www-data:www-data /report
WORKDIR /line
COPY ./line ./
#COPY ./Data ./Data
RUN chmod 777 -R /report
RUN { crontab -l; echo "*/1 * * * * python3 /line/linenotifychecktwo.py"; } | crontab -
RUN { crontab -l; echo "*/3 * * * * python3 /line/linenotify.py"; } | crontab -
RUN git clone git://github.com/psf/requests.git
RUN cd requests
RUN python -m pip install .

# start cron in foreground (don't fork)
ENTRYPOINT [ "cron", "-f" ]
