from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv('PORT'))


@app.route('/')
def hello_world():
    return f"Hello World ! I am running on port {port}"


if __name__ == '__main__':
    app.run(port=port)
