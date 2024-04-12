#!/usr/bin/env python3
"""
Force locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, get_locale

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    if 'locale' in request.args and request.args['locale'] in app.config[
        'LANGUAGES'
    ]:
        return request.args['locale']
    return get_locale()


@app.route('/')
def index():
    """
    Route /
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
