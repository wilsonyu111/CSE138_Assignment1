FROM python:2.7.16

WORKDIR /FLASK_SERVER
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["flask_server.py"]