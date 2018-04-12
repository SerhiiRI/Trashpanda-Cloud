FROM ubuntu
MAINTAINER Serhii Riznychuk sergiy19981@gmail.com
RUN apt update
RUN apt -y upgrade
RUN apt -y install python3
RUN apt -y install python3-pip
RUN pip3 install --upgrade pip
RUN apt-get -y install python-virtualenv
RUN apt-get -y install build-essential libssl-dev libffi-dev python3-dev
RUN apt -y install git
RUN pip3 install Flask
RUN mkdir /server
RUN mkdir /scripts
ADD startup.sh /scripts/startup.sh
EXPOSE 5000

ENTRYPOINT /scripts/startup.sh
