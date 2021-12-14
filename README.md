# MNIST - Kubernetes
This code base is part of the final project for the NYU graduate course CSCI-GA 3033 Cloud and Machine Learning

# Quickstart
```bash
# deploy server
kubectl apply -f server/deployment-cloud.yaml

# wait till the server is running
# check the status with `kubectl get pods`
# then run the requests job
kubectl apply client/client-job.yaml

# Watch the request pod until finish
watch kubectl get pods

# export logs of requesting latency
kubectl log <request pod name; get by `kubectl get pods`> > client_log
```

# Folders and files
## client: 
Folder for requesting client:
- contain python source code, Dockerfile and kubernetes deployment yaml

## server:
Folder for the running server:
- contain python source code, Dockerfile
- contain two versions of kubernetes deployment yaml (one for CPU and one for GPU (not tested))

## cpu_data:
Collected latency data from the client  
Run a simple analyze program
```bash
cd cpu_data
# output [number of replicas, mean, and standard deviations]
python3 analyze.py
```

## delete_service.sh
Clear the launched server Deployment and client Job

## gpu.yaml
Instantiate a standard GPU instance on Kubernetes

