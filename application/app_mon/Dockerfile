FROM python:alpine3.7
RUN apk add --no-cache \
        build-base \
        linux-headers \
        python3-dev
ADD . /app
RUN pip install /app
CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "-w", "app_mon.run:application"]
