FROM python:3.5.1
MAINTAINER Yusuke Miyazaki <miyazaki.dev@gmail.com>

COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt \
        && rm -rf /root/.cache

EXPOSE 8888
CMD ["jupyter", "notebook"]
