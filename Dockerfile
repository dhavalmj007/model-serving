FROM python:3.9

WORKDIR /var/model
EXPOSE 4010

# lightgbm dependency
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1

COPY requirements.txt           requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip/ pip install -r requirements.txt

COPY src                            src
COPY tests                          tests
COPY configs                        configs

COPY deploy-to-openshift.yaml       deploy-to-openshift.yaml

COPY runner.py                      runner.py

CMD python runner.py