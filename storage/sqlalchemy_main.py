from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from storage.sqlalchemy_delcare import Account, Group, Base
import tools.prefix as pfx

class DatabaseHandler:

    def __init__(self):
        self.data = self.__load_data()
        self.insertion_ready = False

    # TODO - Change the exception to return to the main program
    # Either tell the user to fix the configuration file or automatically 
    # reinstall all of the required information
    def __load_data(self):
            try:
                with open("../config.json") as json_file:
                    data = json.load(json_file)
                    return data
            except FileNotFoundError:
                return False

    def setup_insertion(self):
        database_name = self.data["database"]["database_name"]
        engine = create_engine(database_name)

        Base.metadata.bind = engine

        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
