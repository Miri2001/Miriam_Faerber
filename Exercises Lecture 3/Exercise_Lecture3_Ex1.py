# Exercise 1: Stations to gpkg

from pyqgis_scripting_ext.core import *

#necessary funcitons
HMap.remove_layers_by_name(["stations"])

def fromLatString(latString):
    sign = latString[0]
    latDegrees = float(latString[1:3])
    latMinutes = float(latString[4:6])
    latSeconds = float(latString[7:9])
    lat = latDegrees + latMinutes/60 + latSeconds/3600
    if sign == '-':
        lat = lat * -1
    return lat
    
def fromLonString(lonString):
    sign = lonString[0]
    lonDegrees = float(lonString[1:4])
    lonMinutes = float(lonString[5:7])
    lonSeconds = float(lonString[8:10])
    lon = lonDegrees + lonMinutes/60 + lonSeconds/3600
    if sign == '-':
        lon = lon * -1
    return lon

folder = r"C:\Users\miria\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics\Miriam_Faerber\data"
tmpFolder = f"{folder}/natural_earth_vector.gpkg/packages/tmp"

stationsPath = f"{folder}/stations.txt"



with open(stationsPath, "r") as file:
    lines = file.readlines()
    
schema = {
    "stationid": "int", #defining name of the fields and type for the new geopackage
    "name": "string",
    "country": "string",
    "height": "double"
}
stationsLayer = HVectorLayer.new("stations", "Point", "EPSG:4326", schema) #type of geometry and projection used
    
for line in lines:
    line = line.strip()
    #let's get the geometry
    if not line.startswith("#"):
        lineSplit = line.split(",")
        latString = lineSplit[3]
        lonString = lineSplit[4]
        lat = fromLatString(latString)
        lon = fromLonString(lonString)
        
        point = HPoint(lon, lat)
        
        attributes = [
            int(lineSplit[0]),
            lineSplit[1],
            lineSplit[2],
            lineSplit[-1]
        ]
        
        stationsLayer.add_feature(point, attributes)

outputPath = f"{tmpFolder}/stations.gpkg"
error = stationsLayer.dump_to_gpkg(outputPath, overwrite=True) #if adding new layer to existing geopackage take False
if error:
    print(error)
    
dumpedStationsLayer = HVectorLayer.open(outputPath, "stations")
HMap.add_layer(dumpedStationsLayer)

#fid = feature id

###############################################################################



    



