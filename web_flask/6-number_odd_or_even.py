#!/usr/bin/python3
"""Script that start we application and display "Hello HBNB"
"""

from flask import Flask, render_template

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
    """
    Displays C followed by the value of the text variable
    Replaces any underscores in <text> with a space
    """
    text_display = text.replace("_", " ")
    return "C {}".format(text_display)


@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/<text>")
def python(text):
    """
    Displays Python followed by the value of text variable
    Replaces any underscores in <text> with a space
    """

    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """Displays a HTML page only if n is an integer"""

    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_even_or_odd(n):
    """
    Displays a HTML page only if n is an integer
    And checks if it is an even or odd number
    """
    even_odd = "even" if n % 2 == 0 else "odd"
    values = {
            "number": n,
            "even_odd": even_odd
            }
    return render_template("6-number_odd_or_even.html", values=values)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
