#!/usr/bin/env python3
""" The Flask app with Babel set up"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ The configuration for class for Babel set up"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """ The default route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
