# pip3 install sqlalchemy
# pip3 install PyMySQL
# pip3 install psycopg2-binary



from sqlalchemy.orm import Session,declarative_base
from sqlalchemy import create_engine,Column,Integer,String
engine=create_engine("postgresql://test:test@0.0.0.0:5432/TestDB")
#sqlite:///Test.db

#docker run -d -it -p 3306:3306  -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=TestDB -e MYSQL_USER=test -e MYSQL_PASSWORD=test mysql
#mysql+pymysql://test:test@0.0.0.0:3306/TestDB

#docker run -d -it -p 5432:5432 -e POSTGRES_USER=test  -e POSTGRES_PASSWORD=test -e POSTGRES_DB=TestDB postgres
#postgresql://test:test@0.0.0.0:5432/TestDB



base = declarative_base()
class Person(base):
    __tablename__="person"
    id:int=Column(Integer,primary_key=True)
    name:str=Column(String(10))

base.metadata.create_all(engine)
session =Session(engine)
person=Person(name="A")

session.add(person)
session.commit()

print(len(session.query(Person).all()))