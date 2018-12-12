from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.wsgi import DispatcherMiddleware
from app_mon.views import app_api, monitoring_api
from app_mon.monitoring import monitor_request

app = Flask(__name__)
app.register_blueprint(app_api)
app.register_blueprint(monitoring_api)


monitor_request(app)
metrics_app = make_wsgi_app()
application = DispatcherMiddleware(app, {"/app": app, "/metrics": metrics_app})
