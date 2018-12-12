import os
import time
from flask import Flask, request
from prometheus_client import make_wsgi_app
from werkzeug.wsgi import DispatcherMiddleware
from functools import wraps
from app_mon.views import app_api, monitoring_api
from prometheus_client import Counter, Histogram

FLASK_REQUEST_LATENCY = Histogram('flask_request_latency_seconds', 'Flask Request Latency', ['method', 'endpoint'])
FLASK_REQUEST_COUNT = Counter('flask_request_count', 'Flask Request Count', ['method', 'endpoint', 'http_status'])


app = Flask(__name__)
app.register_blueprint(app_api)
app.register_blueprint(monitoring_api)


def monitor_request(func):
    app.before_request(before_request)

    @wraps(func)
    def func_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    app.after_request(after_request)
    return func_wrapper


def before_request():
    request.start_time = time.time()


def after_request(response):
    request_latency = time.time() - request.start_time
    FLASK_REQUEST_LATENCY.labels(request.method, request.path).observe(request_latency)
    FLASK_REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    return response


monitor_request(app)
metrics_app = make_wsgi_app()
application = DispatcherMiddleware(app, {
    '/app': app,
    '/metrics': metrics_app
})


if __name__ == '__main__':
    pass
