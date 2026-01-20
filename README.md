# Kubernetes Microservice Project

## 📋 Overview

A comprehensive, production-ready Kubernetes project demonstrating containerized microservice deployment with CI/CD, Kubernetes manifests, and autoscaling.

## 🎯 Key Features

✅ **Docker Containerization** - Flask microservice packaged in lightweight container  
✅ **Kubernetes Deployments** - Multi-replica deployments with resource management  
✅ **Service Discovery** - ClusterIP service for internal communication  
✅ **Ingress Controller** - External access via Ingress  
✅ **ConfigMaps** - Environment configuration management  
✅ **Horizontal Pod Autoscaler (HPA)** - Auto-scaling based on CPU utilization  
✅ **GitHub Actions CI/CD** - Automated Docker build and deployment pipeline  

## 📁 Project Structure

```
k8s-microservice-project/
├── app/
│   ├── app.py                 # Flask REST API application
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile             # Container image definition
├── k8s/
│   ├── deployment.yaml        # Kubernetes Deployment manifest
│   ├── service.yaml           # Kubernetes Service manifest
│   ├── ingress.yaml           # Kubernetes Ingress manifest
│   ├── configmap.yaml         # Configuration management
│   └── hpa.yaml               # Horizontal Pod Autoscaler
├── .github/workflows/
│   └── deploy.yml             # GitHub Actions CI/CD pipeline
├── Dockerfile                 # Root Dockerfile
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Kubernetes cluster (v1.20+)
- kubectl configured
- Docker (for local testing)
- Minikube (for local development)

### Local Development with Minikube

```bash
# Start Minikube
minikube start

# Build Docker image
cd app
docker build -t flask-k8s:latest .
cd ..

# Deploy to Kubernetes
kubectl apply -f k8s/

# Check deployments
kubectl get pods
kubectl get services
kubectl get hpa

# Port forward to access locally
kubectl port-forward svc/flask-service 8080:80

# Test the API
curl http://localhost:8080/
```

## 📊 API Endpoints

### GET /
Returns microservice information

**Response:**
```json
{
  "message": "Kubernetes Microservice Running",
  "hostname": "flask-app-5d4b9c8f9-xyz",
  "environment": "production"
}
```

## 🔧 Kubernetes Manifests

### Deployment
- **Replicas**: 2 (configurable)
- **Container Port**: 5000
- **Image**: yourdockerhub/flask-k8s:latest
- **Environment Variables**: Injected via ConfigMap

### Service
- **Type**: ClusterIP
- **Port**: 80
- **Target Port**: 5000

### ConfigMap
- Environment configuration
- Application settings

### HPA (Horizontal Pod Autoscaler)
- **Min Replicas**: 2
- **Max Replicas**: 5
- **Target CPU Utilization**: 50%

## 📦 Deployment Instructions

### 1. Build & Push Docker Image

```bash
cd app
docker build -t yourdockerhub/flask-k8s:v1.0 .
docker push yourdockerhub/flask-k8s:v1.0
cd ..
```

### 2. Update Image in Deployment

```bash
kubectl set image deployment/flask-app \
  flask=yourdockerhub/flask-k8s:v1.0
```

### 3. Apply All Manifests

```bash
kubectl apply -f k8s/
```

### 4. Verify Deployment

```bash
kubectl get all
kubectl logs -f deployment/flask-app
```

## 🔄 CI/CD Pipeline

GitHub Actions automatically:
1. Builds Docker image on push to main branch
2. Pushes to Docker registry
3. Can be extended for automatic deployment

## 📈 Monitoring & Debugging

```bash
# View logs
kubectl logs deployment/flask-app

# Get pod details
kubectl describe pod <pod-name>

# Check HPA status
kubectl get hpa flask-hpa --watch

# Test scaling
kubectl run -it --rm debug --image=busybox --restart=Never -- sh
# Inside pod: while sleep 1; do wget -q -O- http://flask-service/; done
```

## 🛠️ Technologies Used

- **Python 3.10** - Application runtime
- **Flask 2.3** - REST API framework
- **Docker** - Containerization
- **Kubernetes 1.20+** - Orchestration
- **GitHub Actions** - CI/CD automation

## 📝 Configuration

### Environment Variables
- `ENV` - Environment (production/development)

### Customization
Edit `k8s/configmap.yaml` to modify application settings.

## 🎓 Learning Outcomes

This project teaches:
- ✅ Kubernetes Deployments & Replicas
- ✅ Service discovery & networking
- ✅ ConfigMaps for configuration management
- ✅ Horizontal Pod Autoscaling
- ✅ CI/CD with GitHub Actions
- ✅ Docker containerization best practices
- ✅ Production-grade microservice architecture

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📄 License

MIT License

## 👨‍💼 Author

Dhanush Gowda

---

**Last Updated**: January 2026  
**Status**: Production Ready ✅
