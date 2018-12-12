from flask import Blueprint, render_template
from flask.views import View


app_api = Blueprint('app_api', __name__, template_folder='templates')


@app_api.route('/')
def index():
    #app.logger.warning('sample message')
    return render_template('index.html')

@app_api.route('/asd')
def help():
    return "Hello"
