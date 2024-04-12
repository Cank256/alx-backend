#!/usr/bin/env python3
"""
Mock logging in
"""

from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """
    Get user before request
    """
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


def get_user(user_id):
    """
    Get user
    """
    return users.get(int(user_id))


@app.route('/')
def index():
    """
    Route /
    """
    if g.user:
        return render_template('5-index.html', username=g.user['name'])
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
