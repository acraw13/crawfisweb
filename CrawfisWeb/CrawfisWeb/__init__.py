"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
wsgi_app = app.wsgi_app


import CrawfisWeb.views