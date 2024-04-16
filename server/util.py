import json
import pickle
import numpy as np
from datetime import datetime,date
__locations=None
__data_columns=None
__model=None
__airline=None
__class=None
def numOfDays(date1, date2):
    if date2 > date1:
        return (date2 - date1).days
    else:
        return (date1 - date2).days
def get_estimated_price(airline,Class,destination,departure,day,stops=0):
    x=np.zeros(len(__data_columns))
    x[0]=__airline.index(airline)
    x[1]=__class.index(Class)
    x[2]=__locations.index(destination)
    x[3] = __locations.index(departure)
    today = date.today()
    traveling_day = datetime.strptime(day, "%d%m%Y").date()
    x[4]=numOfDays(today,traveling_day)
    x[5]=stops
    return round(__model.predict([x])[0],2)




def get_location_names():
     return __locations

def get_airline_names():
    return __airline

def get_class_names():
    return __class

def get_location_names():
    return __locations
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __airline
    global __class
    global __model
    with open("./artifacts/columns.json","r") as f:
        __data_columns=json.load(f)['data_columns']
    with open("./artifacts/locations.json","r") as f:
        __locations=json.load(f)["location"]
    with open("./artifacts/flight_price_model.pickle","rb") as f:
        __model=pickle.load(f)
    print("loading saved artifacts...done")
    with open("./artifacts/airline.json","r") as f:
        __airline=json.load(f)["airline"]
    with open("./artifacts/Class.json", "r") as f:
        __class = json.load(f)["Class"]
    pass


if __name__== "__main__":
    load_saved_artifacts()
    print(get_estimated_price("SpiceJet","ECONOMY","Mumbai","Delhi","08042024",1))