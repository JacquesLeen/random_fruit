from flask import Flask
from flask import render_template
from random import choices

app = Flask(__name__)


def random_fruit():
    """
    Returns Random Fruit
    """

    fruits = ["Apple", "Cherry", "Orange"]
    return choices(fruits)


@app.route("/")  # route is the homepage of a web application
def fruit():
    """
    Returns Random Fruit
    """

    my_fruit = random_fruit()
    return render_template("index.html", title="Random Fruit", fruit=my_fruit)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
