FROM ubuntu:18.04
LABEL maintainer="dohnetwork@gmail.com"
LABEL description="Ubunta"
RUN apt-get -y update &&  DEBIAN_FRONTEND=noninteractive  apt-get install  -y  php python python-pip libmysqlclient-dev ftp nano cron \
            && mkdir /line /Data
            RUN pip install mysql-python
RUN chown -R www-data:www-data /report
WORKDIR /line
COPY ./line ./
#COPY ./Data ./Data
RUN chmod 777 -R /report
#RUN { crontab -l; echo "1 23 * * * /report/all203.sh"; } | crontab -
#RUN { crontab -l; echo "7 23 * * * php /report/c.php"; } | crontab -
#RUN { crontab -l; echo "10 23 * * * python /report/r.py"; } | crontab -
# start cron in foreground (don't fork)
ENTRYPOINT [ "cron", "-f" ]
