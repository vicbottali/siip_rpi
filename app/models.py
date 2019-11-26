from app import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)
    creditCard = db.Column(db.String(120))
    rfid = db.Column(db.String(128))

    def __repr__(self):
        return 'User: {}'.format(self.name)  