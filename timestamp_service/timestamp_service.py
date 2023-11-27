from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_timestamp():
    return str(datetime.now())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)