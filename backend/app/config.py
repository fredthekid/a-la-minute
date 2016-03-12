# FLASK DEBUG MODE
DEBUG = True

# DATABASE INFO
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://fred:006677996@198.199.84.106:3306/alaminute'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SECURITY
CSRF_ENABLED = True
CSRF_SESSION_KEY = "thisismysecretkeyyoucantguessitbecauseitslongwellkindalongkindanotreally"
SECRET_KEY = "thisisAnOtHErKeYuCaNtGueEssThiSbEcuseItypeLykEDiS"