# code by : yasserbdj96
# email : yasser.bdj96@gmail.com

# docker pull docker.io/yasserbdj96/hiphp:latest
# docker build -t docker.io/yasserbdj96/hiphp:latest .
# docker run -e KEY="<KEY>" -e URL="<URL>" -i -t docker.io/yasserbdj96/hiphp:latest

# docker pull ghcr.io/yasserbdj96/hiphp:latest
# docker build -t ghcr.io/yasserbdj96/hiphp:latest .
# docker run -e KEY="<KEY>" -e URL="<URL>" -i -t ghcr.io/yasserbdj96/hiphp:latest


#START{
FROM python:3.9

WORKDIR /wrdir

COPY ./examples/examples.py /wrdir
COPY ./examples/examples.php /wrdir
COPY ./hiphp /wrdir/hiphp
COPY ./requirements.txt /wrdir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /wrdir/requirements.txt

CMD ["python", "examples.py"]
#}END.