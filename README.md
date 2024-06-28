# Microservices Project

This project demonstrates a simple microservice architecture using the Flask framework in Python. The architecture includes a gateway and multiple independent and dependent services, all deployed using Docker and Kubernetes.

## Author
Pandula Gajadeera

## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Services](#services)
- [Setup](#setup)
- [Docker Deployment](#docker-deployment)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Testing](#testing)

## Introduction
This project is a demonstration of a microservice architecture implemented using Flask. It includes a gateway and several microservices, showcasing how microservices can be built, deployed, and managed using Docker and Kubernetes.

## Architecture
The architecture consists of the following components:
- **Gateway**: Acts as the entry point to the microservices.
- **Independent Services**:
  - Random Number Service
  - Message Service
  - Timestamp Service
- **Dependent Services**:
  - Input Validation Service
  - Addition Service
  - Return Service

## Services
### Independent Services
- **Random Number Service**: Provides random numbers.
- **Message Service**: Handles messaging functionality.
- **Timestamp Service**: Provides timestamp data.

### Dependent Services
- **Input Validation Service**: Validates input data.
- **Addition Service**: Performs addition operations.
- **Return Service**: Returns processed data.

## Setup
### Docker Network
Create a Docker network for the microservices:
  ```sh
  docker network create microservices_network
  ```

## Docker Deployment
### Gateway
Build and run the Gateway Server:
  ```sh
  docker build -t gateway-server ./gateway_server
  docker run --network microservices_network -p 8000:8000 --name gateway-server -d gateway-server
  ```

### Independent Services
#### Random Number Service
Build and run the Random Number Service:
  ```sh
  docker build -t random-number-service ./random_number_service
  docker run --network microservices_network -p 8001:8001 --name random-number-service -d random-number-service
  ```

#### Message Service
Build and run the Message Service:
  ```sh
  docker build -t message-service ./message_service
  docker run --network microservices_network -p 8002:8002 --name message-service -d message-service
  ```

#### Timestamp Service
Build and run the Timestamp Service:
  ```sh
  docker build -t timestamp-service ./timestamp_service
  docker run --network microservices_network -p 8003:8003 --name timestamp-service -d timestamp-service
  ```

### Dependent Services
#### Input Validation Service
Build and run the Input Validation Service:
  ```sh
  docker build -t input-validation-service ./inputvalidationservice
  docker run --network microservices_network -p 5000:5000 --name input-validation-service -d input-validation-service
  ```

#### Addition Service
Build and run the Addition Service:
  ```sh
  docker build -t addition-service ./additionservice
  docker run --network microservices_network -p 5001:5001 --name addition-service -d addition-service
  ```

#### Return Service
Build and run the Return Service:
  ```sh
  docker build -t return-service ./returnservice
  docker run --network microservices_network -p 5002:5002 --name return-service -d return-service
  ```

## Kubernetes Deployment
Deploy the services using Kubernetes:
  ```sh
  kubectl apply -f gateway.yaml
  kubectl apply -f timestamp_service.yaml
  kubectl apply -f random_number.yaml
  kubectl apply -f message_service.yaml
  ```

## Testing
You can test the setup using curl:
  ```sh
  curl -X POST -H "Content-Type: application/json" -d '{"data":[1,2,3]}' http://localhost:8000/validate
  ```
