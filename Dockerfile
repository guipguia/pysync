FROM python:alpine3.16

WORKDIR /app

RUN apk add --no-cache rsync bash openssh

COPY main.py .

CMD [ "python", "/app/main.py" ]