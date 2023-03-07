# model-serving
Base code for ML model serving in FastAPI

## To run in Local

1. Open this project in IDE of your choice(VS Code, PyCharm(Recommended))
2. Create virtual environment either through Conda or Venv
3. Activate the Venv
4. Run `pip install -r requirement.txt`
5. To run the code `python runner.py`
6. Open any browser and goto [localhost](http://localhost:4010/model/docs)
7. Try out any API
   1. To test <*/predict*> use data from `src/data/input_samples.json`
   2. To test <*/predict_on_file*> use file from `src/data/test.csv`

## To run in Docker

1. Install docker by following the guide from [here](https://docs.docker.com/engine/install/)
2. Build docker image `docker build -t model-serving:v1`
3. Run the image `docker run -p 4010:4010 -name model-serving model-serving:v1`
4. Open any browser and goto [localhost](http://localhost:4010/model/docs)
5. Try out any API
   1. To test <*/predict*> use data from `src/data/input_samples.json`
   2. To test <*/predict_on_file*> use file from `src/data/test.csv`


## To run in local Kubernetes server (k8s)

1. Install docker by following the guide from [here](https://docs.docker.com/engine/install/)
2. Install KinD (Kubernetes in Docker) from [here](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
3. Run below command to create KinD cluster with ingress enabled(refer [here](https://kind.sigs.k8s.io/docs/user/ingress/) if any issues)
```
cat <<EOF | kind create cluster --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
EOF
```

4. Get the k8s context `kubectl cluster-info --context kind-kind`
5. Deploy Nginx `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml`
6. Wait for the successful deployment. Run below
```commandline
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s
```
7. Deploy the app `kubectl apply -f deploy-to-kind.yaml`
8. Open any browser and goto [localhost](http://localhost/model/docs)
9. Try out any API
   1. To test <*/predict*> use data from `src/data/input_samples.json`
   2. To test <*/predict_on_file*> use file from `src/data/test.csv`