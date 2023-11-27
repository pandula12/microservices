from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/format', methods=['POST'])
def format_result():
    # get data from POST request
    data = request.json
    result = data.get('addition_result')

    # format the result into the required JSON format
    jsonString = '{"result": ' + str(result) + '}'

    # any more desired formatting could go here

    # create a response object
    response = Response(
        response=jsonString, 
        status=200, 
        headers={'X-Custom-Header': 'custom-value'},
        content_type='application/json; charset=utf-8'
    )
    
    # return the result
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)