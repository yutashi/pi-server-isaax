from flask import Flask
import os
app = Flask(__name__)
MESSAGE = os.getenv('MESSAGE', None)

@app.route("/")
def hello():
    if MESSAGE:
        msg = "Your message running on the device: {}".format(MESSAGE)
    else:
        msg = "MESSAGE env isn't set"

    return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0')
