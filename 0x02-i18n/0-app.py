#!/usr/bin/env python3
" The basic Flask app with a single route"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ The route for the index page with a title and header."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
