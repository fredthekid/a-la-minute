from app import db


class RestaurantLoginModel(db.Model):
    __tablename__ = 'restaurant_login'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable= False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<email %r>' % self.email


class RestaurantInfoModel(db.Model):
    __tablename__ = 'restaurant_info'
    id = db.Column(db.Integer, db.ForeignKey('restaurant_login.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(15), unique=True)
    city = db.Column(db.String(50))
    state = db.Column(db.String(20))

    def __init__(self, name, phone_num, city, state):
        self.name = name
        self.phone_num = phone_num
        self.city = city
        self.state = state

    def __repr__(self):
        return '<name %r>' % self.name


class CustomerWaitTimeInfo(db.Model):
    __tablename__ = 'customer_wait_time'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer_info.id'))

    # Talk about the time aspect with Patrick, see how he will implement it, then alter.
    time_entered = db.Column(db.Integer)
    time_served = db.Column(db.Integer)

    def __init__(self, restaurant_id, customer_id, time_entered, time_served):
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.time_entered = time_entered
        self.time_served = time_served

    def __repr__(self):
        return '<RestaurantID %r>' % self.restaurant_id
