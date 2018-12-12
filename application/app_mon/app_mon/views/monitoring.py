from flask import Blueprint
import os

monitoring_api = Blueprint('monitoring_api', __name__)


@monitoring_api.route('/live')
def liveness():
    return "is live"


@monitoring_api.route('/ready')
def readiness():
    return "{} is ready".format(__name__)
