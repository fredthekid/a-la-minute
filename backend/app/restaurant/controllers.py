#
# from werkzeug.security import check_password_hash, generate_password_hash
from app.restaurant.models import RestaurantLoginModel
from flask_restful import Resource, reqparse
from alaminuteWorker import store_customer_wait_info
from app.restaurant.customerpager import CustomerPager


class RestaurantLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        print args
        restaurant = RestaurantLoginModel.query.all()
        print restaurant

# class RestaurantSignup(Resource):
#     def post(self):
#         args =


class TableReady(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('phone', type=str, help='customer phone number')
        self.parser.add_argument('r_id', type=int, help='restaurant_id')
        self.parser.add_argument('r_name', type=str, help='name of restaurant')
        self.parser.add_argument('time_entered', type=int, help='time when customer made reservation')
        self.parser.add_argument('time_served', type=int, help='time when customers table was made ready')
        self.Pager = CustomerPager()

    def post(self):
        try:
            args = self.parser.parse_args()
            phone = args['phone']
            r_id = args['r_id']
            r_name = args['r_name']
            time_served = args['time_served']
            time_entered = args['time_entered']

            # add a check to see if the above are valid, skip for now

            info = self.Pager.AlertCustomer(phone, r_name)
            # store_customer_wait_info.delay(phone, args['r_id'], args['time_entered'], args['time_served'])
            return info
        except:
            return "FAILED"

# class TableCancel(Resource):