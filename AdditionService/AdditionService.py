from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    # get data from POST request
    data = request.json
    data = data.get('data', [])

    total = 0
    # loop through each number and add it to the total
    for num in data:
        total += num

    # prepare response object
    response = Response(str(total), content_type='text/plain')

    # return resulting number
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)