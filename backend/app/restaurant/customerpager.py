from twilio.rest import TwilioRestClient


class CustomerPager(object):
    def __init__(self):
        self.account_id = "AC547c2d3de8fa8e309761a0a5d4e406fb"
        self.auth_token = "2b1ef55f5002d3b32f58c85902dd4f23"
        self.client = TwilioRestClient(self.account_id, self.auth_token)
        self.clientNumber = "+14083260838"

    def AlertCustomer(self, customer_phone_number, restaurant_name):
        msg = "Your table at %s is ready! Please head to the front!" % restaurant_name
        try:
            alert = self.client.messages.create(to="+" + str(customer_phone_number), from_=self.clientNumber, body=msg)
        except:
            return "FKED"
        return "DONEZO"