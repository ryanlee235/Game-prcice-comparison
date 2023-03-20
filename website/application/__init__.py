import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extensions import db
from .views import bp
from .data import cdkeys, g2a, instant_gaming

def create_app():
    #our directory to this file
    basedir = os.path.abspath(os.path.dirname(__file__))
    #telling flask this is the application we want to initialize everything in
    app = Flask(__name__)
    #a passcode so its hard to get in
    app.config['SECRET_KEY'] = "sweetprices"
    #telling the app where to connect to our database from 
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
    
    db.init_app(app)
    app.register_blueprint(bp)
    
    
    with app.app_context():
        db.create_all()

    return app

