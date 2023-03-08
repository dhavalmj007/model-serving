# model-serving
Base code for ML model serving in FastAPI

## To run in Local

1. Open this project in IDE of your choice PyCharm(Recommended) or VSCode
   1. Follow [this](https://www.youtube.com/watch?v=GTtpypvLoeY) video to set up PyCharm
2. Create virtual environment either through Conda or Venv (Follow the video)
3. Activate the Venv
4. Run `pip install -r requirement.txt`
5. To run the code `python runner.py`
6. Open any browser and goto [localhost](http://localhost:4010/model/docs)
7. Try out any API
   1. To test <*/predict*> use data from `src/data/input_samples.json`
   2. To test <*/predict_on_file*> use file from `src/data/test.csv`

## To run in Docker

1. Install docker by following the guide from [here](https://docs.docker.com/engine/install/)
2. Build docker image `docker build -t model-serving:v1 .`
3. Run the image `docker run -p 4010:4010 --name model-serving model-serving:v1`
4. Open any browser and goto [localhost](http://localhost:4010/model/docs)
5. Try out any API
   1. To test <*/predict*> use data from `src/data/input_samples.json`
   2. To test <*/predict_on_file*> use file from `src/data/test.csv`


## To run in local Kubernetes server (k8s)

1. Install docker by following the guide from [here](https://docs.docker.com/engine/install/)
2. Install KinD (Kubernetes in Docker) from [here](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
3. Run below command to create KinD cluster with ingress enabled(refer [here](https://kind.sigs.k8s.io/docs/user/ingress/) if any issues)
   ```
   kind create cluster --config=kind_config.yaml
   ```
   1. If you run into issues similar to port 80 or 443 is already in use try below steps if you are in Windows machine
      1. Run in cmd `netstat -aon | findstr <replace_with_port>|find /i "listening"`
      2. Note down the Process ID(PID) which the last column.
      3. If PID is not 4 then run `Taskkill /F /IM <PID>`
      4. If PID is 4 then
          1. Right-click on My Computer.
          2. Select Manage.
          3. Double click Services and Applications.
          4. Then double click Services.
          5. Right click on "World Wide Web Publishing Service".
          6. Select Stop.

4. Get the k8s context `kubectl cluster-info --context kind-kind`
5. Deploy Nginx `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml`
6. Wait for the successful deployment. Run below
```commandline
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=90s
```
7. Deploy the app `kubectl apply -f deploy-to-kind.yaml`
8. Run `kubectl get pods` and wait for its status of READY 1/1. Something like below
```commandline
NAME                        READY   STATUS    RESTARTS   AGE
ml-model-79ff8b48f7-zsltg   1/1     Running   0          16m
```
8. Open any browser and goto [localhost](http://localhost/model/docs)
9. Try out any API
   1. To test <*/predict*> use data from `src/data/input_samples.json`
   2. To test <*/predict_on_file*> use file from `src/data/test.csv`