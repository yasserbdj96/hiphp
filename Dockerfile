#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

######## local build & run:
# docker build -t hiphp:latest .
# docker run -e KEY="<KEY>" -e URL="<URL>" -i -t hiphp:latest

######## docker.io pull, build & run:
# docker pull docker.io/yasserbdj96/hiphp:latest
# docker build -t docker.io/yasserbdj96/hiphp:latest .
# docker run -e KEY="<KEY>" -e URL="<URL>" -i -t docker.io/yasserbdj96/hiphp:latest

######## ghcr.io pull, build & run:
# docker pull ghcr.io/yasserbdj96/hiphp:latest
# docker build -t ghcr.io/yasserbdj96/hiphp:latest .
# docker run -e KEY="<KEY>" -e URL="<URL>" -i -t ghcr.io/yasserbdj96/hiphp:latest


#START{
FROM python:3.10

WORKDIR /wrdir

COPY ./run.py /wrdir
COPY ./hiphp /wrdir/hiphp
COPY ./requirements.txt /wrdir/requirements.txt
#COPY ./config_file.json /wrdir/config_file.json

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /wrdir/requirements.txt

CMD ["python", "run.py"]
#}END.