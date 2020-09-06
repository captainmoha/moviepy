from flask import Flask

from .site.routes import site
from .api.routes import api

from .services.cache import cache


def create_app():

    app = Flask(__name__)

    # init cache for app
    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app)

    # register site & api blueprints
    app.register_blueprint(site)
    app.register_blueprint(api)

    return app
