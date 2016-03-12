from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app.restaurant.controllers import RestaurantLogin, TableReady
from app.customer.controllers import CustomerInfo, CustomerLogin

# Database Setup
db.create_all()
db.session.commit()

# RESTful API Setup
api = Api(app)

api.add_resource(RestaurantLogin, '/restaurantlogin')
api.add_resource(TableReady, '/tableready')
# api.add_resource(TableCancel, '/tablecancel')

# Routes for handling default or error views
@app.route("/test")
def index():
    return "Hello World"

