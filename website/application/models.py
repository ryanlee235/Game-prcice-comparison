from .extensions import db

class InstantGaming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    link = db.Column(db.String)
    picture = db.Column(db.String)



class CdKeys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    link = db.Column(db.String)
    picture = db.Column(db.String)




class G2A(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    link = db.Column(db.String)
    picture = db.Column(db.String)
