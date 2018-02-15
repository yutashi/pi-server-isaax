from flask import Flask
import os
app = Flask(__name__)
MESSAGE = os.getenv('MESSAGE', 'Cannot load the env')

@app.route("/")
def hello():
    msg = "Your message running on the device: {}".format(MESSAGE)
    return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0')
