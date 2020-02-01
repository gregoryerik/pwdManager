from sqlalchemy import Table, Column, ForeignKey, Integer, String, MetaData, create_engine
import tools.prefix as pfx
from tools import configuration
import os

#Base = declarative_base()
"""
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

"""
def log(note):
    print(pfx.NOTE + note, end=" ")

def log_OK():
    print("OK")

def log_FAIL():
    print("FAILED")

def make_group(meta):
    group = Table("group", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String)
    )

    #return group ## Dont need 

def make_account(meta):
    account = Table("account", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("encrypted", String),
    Column("group_id", Integer, ForeignKey("group.id"))
    )

    # return account ## Doesnt seem like I need this just yet

def create():
    data = configuration.load_data()
    log("Reading data from CONFIG.JSON:")
    if data is not False:
        log_OK()
        log("Creating database engine:")

        file_name = data["database"]["database_name"]
        absolute_path = os.path.abspath(os.path.join(__file__, "../"))
        database_name = f"sqlite:///{absolute_path}/{file_name}" # Using three /'s because the fourth is added with the absolute file
        engine = create_engine(database_name, echo=False)

        log_OK()
        log("Creating database metadata:")
        meta = MetaData()
        log_OK()

        make_group(meta)
        make_account(meta)

        log("Creating database:")
        meta.create_all(engine)
        log_OK()
        
        print(pfx.SUCCESS + "Finished creating the database!")
    else:
        log_FAIL()
        print(pfx.WARNING + "Could not load data from config.json")