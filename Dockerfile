FROM ubuntu:18.04
LABEL maintainer="dohnetwork@gmail.com"
LABEL description="Ubunta"
#RUN apt-get -y update &&  DEBIAN_FRONTEND=noninteractive  apt-get install  -y   python3 python-pip git  libmysqlclient-dev  nano cron python3-pip python-mysqldb \
RUN apt-get -y update &&  DEBIAN_FRONTEND=noninteractive  apt-get install  -y  python3 python3-pip  python-mysqldb python3-pymysql git  libmysqlclient-dev  nano cron   \
            && mkdir /line /Data
#            RUN pip3 install mysql-python
           # RUN pip3 install MySQL-python    
            RUN pip3 install parse
            RUN pip3 install requests
          
RUN chown -R www-data:www-data /line
WORKDIR /line
COPY ./line ./
#COPY ./Data ./Data
RUN chmod 777 -R /line
RUN { crontab -l; echo "*/1 * * * * python3 /line/linenotifychecktwo.py"; } | crontab -
RUN { crontab -l; echo "*/3 * * * * python3 /line/linenotify.py"; } | crontab -
RUN git clone git://github.com/psf/requests.git
RUN cd /line/requests
#RUN python -m pip install .
#RUN python -m pip install requests

# start cron in foreground (don't fork)
ENTRYPOINT [ "cron", "-f" ]
