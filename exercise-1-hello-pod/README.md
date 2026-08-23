# Zepto K8s Exercise 1: Hello Pod

## Overview
Deployed a lightweight Nginx web application (simulating Zepto's storefront) on a local Kubernetes cluster using Minikube.

## Artifacts
- pod-hello-k8s.yaml: Exported Pod manifest
- service-hello-k8s.yaml: Exported NodePort Service manifest

## Execution Summary
1. minikube start
2. kubectl run hello-k8s --image=nginx --port=80
3. kubectl expose pod hello-k8s --type=NodePort --port=80
4. Verified via minikube service hello-k8s
