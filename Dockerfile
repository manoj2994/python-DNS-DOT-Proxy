FROM python:3.8.2-alpine3.10


WORKDIR /usr/local/bin
COPY dotproxy.py .

EXPOSE 53/tcp
EXPOSE 53/udp

CMD ["python","dot_proxy.py"]