#!/usr/bin/env python3
""" The Flask app with Babel locale selection"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ The configuration for Babel set up."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determines the best match for supported languages."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.context_processor
def inject_get_locale():
    """ The get_locale function."""
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    """ The default route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
