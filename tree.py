import csv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:A15j27lh!35h@127.0.0.1:3306/employee')
Base = declarative_base()

BASE = '/Users/bruno/Documents/data/test/candidates.csv'
with open(BASE, newline='') as f:
    reader = csv.reader(f, delimiter=';')
    data = list(reader)

class Hire(Base):
    __tablename__ = 'Hire'
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    application_data = Column(String(255))
    country = Column(String(255))
    yoe = Column(String(255))
    seniority = Column(String(255))
    technology = Column(String(255))
    code_challenge = Column(String(255))
    technical_interview = Column(String(256))

Base.metadata.create_all(engine)

session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    hire = []
    for i in data[1::]:
        record = {
            'first_name' : i[0],
            'last_name' : i[1],
            'email' : i[2],
            'application_data' : i[3],
            'country' : i[4],
            'yoe' : i[5],
            'seniority':i[6],
            'technology':i[7],
            'code_challenge':i[8],
            'technical_interview':i[9]
        }
        hire.append(record)

    s.bulk_insert_mappings(Hire, hire)  
    s.commit()
except:
    s.rollback()
finally:
    s.close() 
