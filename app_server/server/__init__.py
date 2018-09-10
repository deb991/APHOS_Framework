#!/usr/bin/env python
import os
import sys
from flask import Flask

server = Flask(__name__)


@server.route("D://DE635273_JSOZZIUS//My_Projects//app_server//")
def index():
    return "Hello World!!!"

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0')

