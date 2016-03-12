from celery import Celery
# import MySQLdb

# Celery Configs
app = Celery('alaminute_workers', backend='amqp', broker='amqp://fred:006677996@198.199.84.106//')

# Database Configs
# db = MySQLdb.connect(host='198.199.84.106', user='fred', passwd='006677996', db='alaminute')
# cur = db.cursor()

@app.task
def test_add(x, y):
    pass
    # return x + y

@app.task
def store_customer_wait_info(phone, r_id, time_entered, time_served):
    pass
    # try:
    #     customer_id_query = "SELECT id FROM customer_login WHERE phone=" + str(phone)
    #     cur.execute(customer_id_query)
    #     c_id = cur.fetchone()
    #     insert_query = "INSERT INTO customer_wait_time (restaurant_id, customer_id, time_entered, time_served) VALUES (%d, %d, %d, %d)"%(r_id,c_id,time_entered, time_served)
    #
    #     cur.execute(insert_query)
    #     db.commit()
    # except:
    #     return "FAILED"
    # return "SUCCESS"
