# Object Detection Project with YOLOv5

A Docker and Kubernetes project for deploying object detection applications, featuring prediction, storage, and a Streamlit interface.

## Applications

1. **Prediction App**: Handles object detection using YOLOv5.
2. **Storage App**: Manages image storage and retrieval.
3. **Streamlit App**: Provides a user interface for uploading images and viewing results.

## APIs

The applications communicate via RESTful APIs:

- **Prediction API**: Accepts image uploads and returns detected objects.
- **Storage API**: Handles image storage and retrieval.

## Docker

Docker is used to containerize each application. Build and push commands:

```bash
docker build -t [DOCKER_HUB_USERNAME]/streamlit_yolo:yolov5-storage -f Dockerfile_storage .
docker push [DOCKER_HUB_USERNAME]/streamlit_yolo:yolov5-storage

docker build -t [DOCKER_HUB_USERNAME]/streamlit_yolo:yolov5-streamlit -f Dockerfile_streamlit .
docker push [DOCKER_HUB_USERNAME]/streamlit_yolo:yolov5-streamlit

docker build -t [DOCKER_HUB_USERNAME]/streamlit_yolo:yolov5-prediction -f Dockerfile_prediction .
docker push [DOCKER_HUB_USERNAME]/streamlit_yolo:yolov5-prediction
```

## Kubernetes

Kubernetes is used to deploy and manage the containerized applications.

* **Deploy the applications:**

```bash
kubectl apply -f prediction-deployment.yaml
kubectl apply -f storage-deployment.yaml
kubectl apply -f streamlit-deployment.yaml
```

## Minikube and kubectl

Minikube is used to run a local Kubernetes cluster for development and testing. kubectl is the command-line tool for interacting with the Kubernetes cluster, allowing you to deploy applications, inspect and manage cluster resources, and view logs.

These tools facilitate the management and deployment of containerized applications in a Kubernetes environment, making it easier to develop, test, and scale the object detection system.

```bash
minikube start

minikube service streamlite-service
```
