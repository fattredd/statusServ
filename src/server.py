#!/usr/bin/env python3

from flask import Flask, request
from markupsafe import escape
import os, shutil, yaml
import reporter
app = Flask(__name__)

@app.route('/')
def show_status():
    return 'Server Status!\n'

@app.route('/report/<servername>', methods=['GET', 'POST'])
def report(servername):
    name = escape(servername)
    if request.method == 'POST':
        return report.add(name, request.form['data'])
    else:
        return report.get(name)

if __name__ == '__main__':
    if not os.path.isfile('config/config.yml'):
        shutil.copyfile('config/config.template.yml', 'config/config.yml')
    with open('config/config.yml') as f:
        config = yaml.safe_load(f)
    report = reporter.Reporter(config)
    app.run(host=config['host'], debug=config['debug'])
