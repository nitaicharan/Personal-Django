from sqlalchemy import create_engine

DATABASE_URL = "mysql://"

engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

connection = engine.connect()
