from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import json
import tools.prefix as pfx

Base = declarative_base()

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    encrypted = Column(String(500), nullable=False)
    group_id = Column(Integer, ForeignKey("group.id"))

def __load_data():
		try:
			with open("../config.json") as json_file:
				data = json.load(json_file)
				return data
		except FileNotFoundError:
			return False

def create():
    data = __load_data()
    if data is not False:
        database_name = data["database"]["database_name"]
        engine = create_engine(database_name)

        Base.metadata.create_all(engine)
    else:
        print(pfx.WARNING + "Could not load data from config.json")