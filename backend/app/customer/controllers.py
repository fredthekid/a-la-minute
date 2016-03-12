# THIS IS TEMPORARY
from app.customer.models import CustomerLoginModel
#, CustomerInfoModel
from flask_restful import Resource, reqparse


class CustomerLogin(Resource):
    def get(self):
        return "HI!"


class CustomerInfo(Resource):
    def get(self):
        return "HOLA!"