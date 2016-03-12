from app import db


class CustomerLoginModel(db.Model):
    __tablename__ = 'customer_login'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    has_signed_up = db.Column(db.Boolean, default=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Customer Email %r>' % self.email


class CustomerInfoModel(db.Model):
    __tablename__ = 'customer_info'
    id = db.Column(db.Integer, db.ForeignKey('customer_login.id'), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))

    def __init__(self, first_name, last_name, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state

    def __repr__(self):
        return '<Name %r %r>' % (self.first_name, self.last_name)
