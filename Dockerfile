FROM python:alpine3.16

WORKDIR /app

RUN apk add --no-cache rsync bash openssh

COPY entrypoint.sh .
COPY main.py .

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]