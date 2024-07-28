#!/usr/bin/python3
"""Script that start we application and display "Hello HBNB"
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Display Hello HBNB"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
idef hbnb():
    """Display HBNB"""

    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
