from flask import Flask
from controller.list_de_controller import app_list_de

app = Flask(__name__)

app.register_blueprint(app_list_de)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
