#encoding: utf-8

from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.conf')
#db = SQLAlchemy(app)

from flask4 import views,models