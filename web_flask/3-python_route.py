#!/usr/bin/python3
"""Script that start we application and display "Hello HBNB"
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """Display Hello HBNB"""

    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Display HBNB"""

    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Displays C followed by the value of the text variable"""
    text_display = text.replace("_", " ")
    return "C {}".format(text_display)


@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/<text>")
def python(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
