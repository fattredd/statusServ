#!/usr/bin/env python3

from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def show_status():
    return 'Server Status!\n'

@app.route('/addreport/<servername>')
def add_report(servername):
    name = escape(servername)
    print(f'User {name}')
    return 'OK\n'

@app.route('/getreport/<servername>')
def get_report(servername):
    name = escape(servername)
    print(f'User {name}')
    return 'OK\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)