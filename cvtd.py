from flask import  Flask
from flask_ask import Ask,statement,session,question
import  json
import requests

import time
import unidecode
import directions

import logging







app = Flask(__name__)

ask = Ask(app,"/cvtd_tracker")


log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def getDirections():
    return "hello world"


@app.route('/')
def homepage():
    #return getDirections()
    return "Welcome to CVTD Tracker"


@ask.launch
def start_skill():
    welcome_message  = "Hello,would you like know the directions for bus?"
    return question(welcome_message)

@ask.intent("YesIntent")
def ask_bus_number():
    return question("for which bus?")

@ask.intent("numberIntent")
def readBusNumber(route):
    msg = directions.reverseGeoCodePosition(directions.getBusLocation(route))
    msg = "The bus "+route +" is at " +msg
    return statement(msg)

@ask.intent("sendBusPositionIntent")
def sendBusPositionIntent(route):
    msg = directions.reverseGeoCodePosition(directions.getBusLocation(route))
    msg = "The bus " + route + " is at " + msg
    return statement(msg).simple_card("Bus Number {}".format(route), msg)


@ask.intent("nearestStopIntent")
def getNearestStop(route):
    msg = directions.getMinStopID(directions.getALLStopID(route))
    return statement(msg)



@ask.intent("NoIntent")
def bye():
    return statement("bye bye")

@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("Thanks for using santhosh's transit tracker")





if __name__ == "__main__":

    app.run(debug=True)
    # welcome_message = directions.reverseGeoCodePosition(directions.getBusLocation(4))
    # print(welcome_message)




