FROM python:3.6-slim
MAINTAINER Taya

WORKDIR /usr/project

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["/usr/project/entrypoint.sh"]
