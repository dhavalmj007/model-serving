FROM python:3.9

WORKDIR /var/model
EXPOSE 4010

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src
COPY tests tests
COPY configs configs

COPY runner.py runner.py

CMD python runner.py