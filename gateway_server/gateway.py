from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Gateway!"

@app.route('/random')
def get_random_number():
    response = requests.get("http://random-number-service:8001/")
    return response.text

@app.route('/message')
def get_message():
    response = requests.get("http://message-service:8002/")
    return response.text


@app.route('/timestamp')
def get_timestamp():
    response = requests.get("http://timestamp-service:8003/")
    return response.text


# Define route for dependant services
routes = {
    '/validate': 'http://input-validation-service:5000/validate',
    '/add': 'http://addition-service:5001/add',
    '/return': 'http://return-service:5002/format',
}

@app.route('/<string:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(path):
    if path in routes:
        target_url = routes[path]
        if path == '/add' or path == '/validate' or path == '/return':
            try:
                response = requests.post(routes['/validate'] , json=request.json)
                if response.status_code != 200:
                    print("Invalid input: {response.text}")
                    return response.text, response.status_code

                response = requests.post(routes['/add'], json=request.json)
                if response.status_code != 200:
                    print("Addition error: {response.text}")
                    return response.text, response.status_code
                result = response.text

                response = requests.post(routes['/return'], json={addition_result: result})
                if response.status_code != 200:
                    print("Return error: {response.text}")
                    return response.text, response.status_code
            except requests.exceptions.RequestException as e:
                return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

