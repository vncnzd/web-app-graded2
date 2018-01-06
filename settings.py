from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.secret_key = "mysecretkey"
db = SQLAlchemy(app)
