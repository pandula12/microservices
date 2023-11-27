from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_message():
    return "I love Software Engineering in Industry"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)