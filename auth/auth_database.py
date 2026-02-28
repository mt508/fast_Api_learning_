from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

mysql_user="root"
mysql_pass="13feb2005"
mysql_host="localhost"
mysql_port="3306"
mysql_database="fastapi_"

#mysql+pymysql://username:password@host:port/database

databaseurl=f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_database}"

engine= create_engine(databaseurl)

localsession= sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()

base=declarative_base()