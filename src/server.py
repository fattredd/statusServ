#!/usr/bin/env python3

from flask import Flask, request, abort
from werkzeug.exceptions import HTTPException
from markupsafe import escape
import os, shutil, yaml, hashlib
import reporter
app = Flask(__name__)

@app.route('/')
def show_status():
    return 'Server Status!\n'

@app.route('/report/<username>', methods=['GET', 'POST'])
def report(username):
    name = escape(username)
    if not check_user(name, request):
        abort(401)
    if request.method == 'POST':
        return report.add(name, request.form['data'])
    else:
        return report.get(name)

@app.errorhandler(HTTPException)
def internal_error(error):
    return {"status": error.code}

def check_user(name, req):
    if not 'password' in req.form:
        return False
    if not name in config['users'].keys():
        return False
    user = config['users'][name]
    needed_perms = 'w' if req.method == "POST" else 'r'
    if needed_perms not in user['perms']:
        return False
    salted_pass = req.form['password']+config['salt']
    hashed_pass = hashlib.md5(salted_pass.encode()).hexdigest()
    return user['pass'] == hashed_pass

if __name__ == '__main__':
    if not os.path.isfile('config/config.yml'):
        shutil.copyfile('config/config.template.yml', 'config/config.yml')
    with open('config/config.yml') as f:
        config = yaml.safe_load(f)
    report = reporter.Reporter(config)
    app.run(host=config['host'], debug=config['debug'])
