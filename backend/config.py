DEBUG = True
PORT = "8080"
SECRET = "DAOTINGC" # modify this by yourself
TRAP_HTTP_EXCEPTIONS = True
# justify database uri for ur machine
SQLALCHEMY_DATABASE_URI= "mysql+pymysql://root:iampassword@localhost:3306/book-recommend" # modify this by yourself
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "SECRETKEY" # modify this by yourself
SESSION_TYPE = "redis"
SESSION_REDIS = "redis://localhost:6379" # modify this by yourself
SESSION_PERMANENT = False
