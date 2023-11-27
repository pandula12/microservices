Docker Network
docker network create microservices_network

/////////////////////////////////////////////////
Gateway
/////////////////////////////////////////////////
Gateway Server
docker build -t gateway-server ./gateway_server
docker run --network microservices_network -p 8000:8000 --name gateway-server -d gateway-server

/////////////////////////////////////////////////
Independant Services
/////////////////////////////////////////////////
Random number service
docker build -t random-number-service ./random_number_service
docker run --network microservices_network -p 8001:8001 --name random-number-service -d random-number-service

Message service
docker build -t message-service ./message_service
docker run --network microservices_network -p 8002:8002 --name message-service -d message-service

Timestamp service
docker build -t timestamp-service ./timestamp_service
docker run --network microservices_network -p 8003:8003 --name timestamp-service -d timestamp-service

/////////////////////////////////////////////////
Dependant Services
/////////////////////////////////////////////////
Input Validation service
docker build -t input-validation-service ./inputvalidationservice
docker run --network microservices_network -p 5000:5000 --name input-validation-service -d input-validation-service

Addition Service
docker build -t addition-service ./additionservice
docker run --network microservices_network -p 5001:5001 --name addition-service -d addition-service

Return Service
docker build -t return-service ./returnservice
docker run --network microservices_network -p 5002:5002 --name return-service -d return-service

Testing using curl
curl -X POST -H "Content-Type: application/json" -d '{"data":[1,2,3]}' http://localhost:8000/validate

/////////////////////////////////////////////////
Kubernetes Deployment
/////////////////////////////////////////////////
kubectl apply -f gateway.yaml
kubectl apply -f timestamp_service.yaml
kubectl apply -f random_number.yaml
kubectl apply -f message_service.yaml