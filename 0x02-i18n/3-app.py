#!/usr/bin/env python3
""" The main Flask application file"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Configures Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page"""
    return request.accept_languages.best_match(app.config['LANGUAGES']) or 'en'


@app.route('/')
def index():
    """The default route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
