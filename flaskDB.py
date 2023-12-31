

from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///Test.sqlite3"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://test:test@0.0.0.0:3306/TestDB"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://test:test@0.0.0.0:5432/TestDB"

db=SQLAlchemy(app)

class Person(db.Model):
    id:int=db.Column(db.Integer,primary_key=True)
    name:str=db.Column(db.String(10))
    def __init__(self,name):
        self.name=name


if(__name__=="__main__"):
    app.app_context().push()
    db.create_all()


