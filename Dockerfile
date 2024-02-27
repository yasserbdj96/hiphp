#   |                                                         |   #
# --+---------------------------------------------------------+-- #
#   |    Code by: yasserbdj96                                 |   #
#   |    Email: yasser.bdj96@gmail.com                        |   #
#   |    GitHub: github.com/yasserbdj96                       |   #
#   |    Sponsor: github.com/sponsors/yasserbdj96             |   #
#   |    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      |   #
#   |                                                         |   #
#   |    All posts with #yasserbdj96                          |   #
#   |    All views are my own.                                |   #
# --+---------------------------------------------------------+-- #
#   |                                                         |   #

######## local build & run:
# docker build -t hiphp:latest .
# Run as CLI:
# docker run -e KEY="<KEY>" -e URL="<URL>" -i -t hiphp:latest
# Run as CLI with PROXIES:
# docker run -e KEY="<KEY>" -e URL="<URL>" -e PROXIES="<FILE_PATH/{'http/https':'IP:port'}>" -i -t hiphp:latest
# Run as GUI:
# docker run --rm -p 127.0.0.1:8080:8080 -e DOCKER=True -e DST=True -i -t hiphp:latest

######## docker.io pull, build & run:
# docker pull docker.io/yasserbdj96/hiphp:latest
# docker build -t docker.io/yasserbdj96/hiphp:latest .
# Run as CLI:
# docker run -e KEY="<KEY>" -e URL="<URL>" -i -t docker.io/yasserbdj96/hiphp:latest
# Run as CLI with PROXIES:
# docker run -e KEY="<KEY>" -e URL="<URL>" -e PROXIES="<FILE_PATH/{'http/https':'IP:port'}>" -i -t docker.io/yasserbdj96/hiphp:latest
# Run as GUI:
# docker run --rm -p 127.0.0.1:8080:8080 -e DOCKER=True -e DST=True -i -t docker.io/yasserbdj96/hiphp:latest

######## ghcr.io pull, build & run:
# docker pull ghcr.io/yasserbdj96/hiphp:latest
# docker build -t ghcr.io/yasserbdj96/hiphp:latest .
# Run as CLI:
# docker run -e KEY="<KEY>" -e URL="<URL>" -i -t ghcr.io/yasserbdj96/hiphp:latest
# Run as CLI with PROXIES:
# docker run -e KEY="<KEY>" -e URL="<URL>" -e PROXIES="<FILE_PATH/{'http/https':'IP:port'}>" -i -t ghcr.io/yasserbdj96/hiphp:latest
# Run as GUI:
# docker run --rm -p 127.0.0.1:8080:8080 -e DOCKER=True -e DST=True -i -t ghcr.io/yasserbdj96/hiphp:latest

#START{
FROM python:3.13.0a3

# start install google-chrome:
# Download the Chrome Driver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# end install google-chrome.

WORKDIR /wrdir

COPY ./main.py /wrdir
COPY ./hiphp /wrdir/hiphp
COPY ./hiphp-desktop /wrdir/hiphp-desktop
COPY ./requirements.txt /wrdir/requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /wrdir/requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
#}END.