from app_mon import FLASK_REQUEST_LATENCY, FLASK_REQUEST_COUNT
from functools import wraps
from flask import request
import time


def before_request():
    request.start_time = time.time()


def after_request(response):
    request_latency = time.time() - request.start_time
    FLASK_REQUEST_LATENCY.labels(request.method, request.path).observe(request_latency)
    FLASK_REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    return response


def monitor_request(app):
    app.before_request(before_request)

    @wraps(app)
    def func_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    app.after_request(after_request)
    return func_wrapper
