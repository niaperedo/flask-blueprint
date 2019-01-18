from flask import Flask

app = Flask(__name__)

from blueprints.api.routes import mod_api
from blueprints.web.routes import mod_web

app.register_blueprint(mod_api, url_prefix='/api')
app.register_blueprint(mod_web)


