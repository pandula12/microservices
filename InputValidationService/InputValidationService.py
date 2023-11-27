from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
    # get data from POST request
    data = request.json
    data = data.get('data', [])
    
    # Check if data is a list
    isList = isinstance(data, list)

    # Check if all elements in the list are either int or float
    areNumbers = True
    for num in data:
        # set to false if any do not match
        if not isinstance(num, (int, float)):
            areNumbers = False

    # Combine both conditions
    if not (isList and areNumbers):
        # return error if either condition is not met
        return jsonify({"status": "failed", "error": "Invalid input"}), 400
    
    # Otherwise return True (valid input)
    return jsonify({"status": "success"}), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)