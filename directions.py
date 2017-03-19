import requests
import json
import googlemaps
import math

# place your cvtd api key in the following line between the quotes
CVTD_KEY = ""
BUS_LOCATION_URL = 'http://cvtd.info:8080/json/BusLocations/V100/system.php?key='

STOP_ORDER = 'http://cvtd.info:8080/CVTDfeed/V200/JSON/DBStopOrder.php?key='

STOPS = 'http://cvtd.info:8080/CVTDfeed/V200/JSON/DBStops.php?key='

# place your google maps/directions api key in the following line between the quotes
DIRECTION_API_KEY = ''

# enter your latitude and longitude in the following lines in place of 0.0
MYlOCATION_LATITUDE = 0.0
MYlOCATION_LONGITUDE = 0.0



gmaps = googlemaps.Client(key=DIRECTION_API_KEY)




def deg2rad(deg):
  return deg * (math.pi/180)


def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2):
   R = 6371 # Radius of the earth in km
   dLat = math.radians(lat2-lat1) # deg2rad below
   dLon = math.radians(lon2-lon1)
   a =    math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
   d = R * c # Distance in km
   return d



# use the cvtd api to get the position of the different buses


# return the latitude and longitude as a tuple
def getBusLocation(busNumber):
    data = requests.get(BUS_LOCATION_URL + CVTD_KEY).content.decode("utf-8")
    # print("type is",type(data))
    data = json.loads(data)
    BusDetails = (data["CVTD_Bus_Route_v100"])

    # Now iterate over the list of bus details to find the required bus number details
    # process the details to return the position of latitude and longitude as a tuple

    for bus in BusDetails:
        #print(bus)
        if data["CVTD_Bus_Route_v100"][bus][0]["RouteNumber"] == str(busNumber):
            myBusDetails = data["CVTD_Bus_Route_v100"][bus][0]
            # print("my bus details ",myBusDetails)

            latitude =  myBusDetails["GPSinfo"]["datetime"][0]["latitude"]
            longitude = myBusDetails["GPSinfo"]["datetime"][0]["longitude"]

            # print("latitude: ",latitude)
            # print("longitude: ", longitude)
            if (latitude != "0.0"):
                break

    return (latitude,longitude)


def reverseGeoCodePosition(locationTuple):
    result = gmaps.reverse_geocode(locationTuple)
    #result = gmaps.reverse_geocode((MYlOCATION_LATITUDE,MYlOCATION_LONGITUDE))
    #print("result is ",result)

    # we can modify the formatted address to give explicit directions
    #print("formatted address is ",result[0]["formatted_address"])
    return result[0]["formatted_address"]


def getALLStopID(busNumber):
    stopIDForBus = []
    allBusStops = requests.get(STOP_ORDER+CVTD_KEY).content.decode('utf-8')
    allBusStops = json.loads(allBusStops)

    allBusStops = allBusStops['CVTD_StopOrder_v200']['StopOrder']

    for stop in allBusStops:
        if stop['RouteID'] == str(busNumber):
            stopIDForBus.append(stop['StopID'])

    print("list of id's are",stopIDForBus)

    return  stopIDForBus

def getMinStopID(stopIDForBus):
    # use the stops api to get details about the stop
    # len of stopIDForBus is 26
    stopDetails = requests.get(STOPS+CVTD_KEY).content.decode('utf-8')
    stopDetails = json.loads(stopDetails)

    stopDetails = stopDetails['CVTD_Stops_v200']['stop']

    # length is 362
    print("stop details are",stopDetails)

    minIndex = 0
    minDist  = 945239475987487

    for i in range(len(stopDetails)):
        if stopDetails[i]['-id'] in stopIDForBus:
            if getDistanceFromLatLonInKm(float(stopDetails[i]['Latitude']),float(stopDetails[i]['Longitude']),MYlOCATION_LATITUDE,MYlOCATION_LONGITUDE) < minDist:
                minIndex = i
                minDist = getDistanceFromLatLonInKm(float(stopDetails[i]['Latitude']),float(stopDetails[i]['Longitude']),MYlOCATION_LATITUDE,MYlOCATION_LONGITUDE)
    #print("min distance is ",minDist)
    #print("nearest location is ",stopDetails[minIndex])

    return "The nearest stop is at {}".format(stopDetails[minIndex]['Address'])




if __name__ == "__main__":
    busNumber = 1

    locationTuple =  getBusLocation(busNumber)

    print(locationTuple[0])
    print(locationTuple[1])

    reverseGeoCodePosition(locationTuple)

    stopIDForBus =  getALLStopID(busNumber)

    minStopID = getMinStopID(stopIDForBus)

    print(minStopID)




