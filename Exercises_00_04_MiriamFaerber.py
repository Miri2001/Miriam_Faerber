# Exercise 00

# Write a scrip that reads geometries from the file and draws them on a new map canvas 

# always import the library first!
from pyqgis_scripting_ext.core import *

#Then define the path for the file
folder = r"C:\Users\miria\OneDrive\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics"
path = f"{folder}\\02_exe0_geometries.csv"

#Open the file
with open(path, 'r') as file:
    lines = file.readlines()
#print(lines)

mylines =[]
polygon_coords = []

for line in lines:
    line= line.strip().split(";")
    shape = line[0]
    coordinates = line[1]
    #print(shape)
    #print(coordinates)
    if shape == "point":
        latitude = float(coordinates[0:3])
        longitude = float(coordinates[5:])
        point1 = HPoint(latitude, longitude)

    if shape == "line":
        myline = coordinates.split(" ")
        #print(myline)
        for item in myline:
            splitted_myline = item.split(",")
            latitude = float(splitted_myline[0])
            
            longitude = float(splitted_myline[1])
            mylines.append([latitude, longitude])
        linie = HLineString.fromCoords(mylines)

    if shape == "polygon":
        pairs = coordinates.split(" ")
        #print(pairs)
        for item in pairs:
            lat_lon = item.split(",")
            #print(lat_lon)
            lat = float(lat_lon[0])
            long = float(lat_lon[1])
            polygon_coords.append([lat, long])
        
    polygon1 = polygon_coords[0:5]
    polygon2 = polygon_coords[5:10]
print(polygon1)
print(polygon2)

poly1 = HPolygon.fromCoords(polygon1)
poly2 = HPolygon.fromCoords(polygon2)

#print on canvas
    
canvas = HMapCanvas.new()
canvas.add_geometry(point1, "red", 1)
canvas.add_geometry(linie, "red", 1)
canvas.add_geometry(poly1, "violet", 1)
canvas.add_geometry(poly2, "blue", 2)
canvas.set_extent([0,0,50,50])
canvas.show()


################################################################################

# Exercise 01
all_coords = []
coords_prototype = [[0,0],[6,0], [6,90], [0,90], [0,0]]

prototype = HPolygon.fromCoords(coords_prototype)

for i in range(60):
    new_coords = []
    for coord in coords_prototype:
        new_coords.append((coord[0] + i * 6, coord[1]))
    all_coords.append(new_coords)
#print(all_coords)
UTM = HMultiPolygon.fromCoords(all_coords)
canvas = HMapCanvas.new()
canvas.add_geometry(UTM, "red", 2)
canvas.set_extent([0,0,400,100])
#canvas.show()
    


# canvas = HMapCanvas.new()
# canvas.add_geometry(UTM, "red", 2)
# canvas.set_extent([0,0,400,100])
# canvas.show()

##############################################################################################

# Exercise 02
from pyqgis_scripting_ext.core import *
folder = r"C:\Users\miria\OneDrive\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics"
path = f"{folder}\\stations.txt"

#Open the file
with open(path, 'r') as file:
    lines = file.readlines()

stations = []

for line in lines:
    #print(line)
    line = line.strip()
    if line.startswith("#")or len(line) == 0:
        continue
    splitted = line.split(",")
    latitude = splitted[3].replace("+", "")
    lat_split = latitude.split(":")
    #print(lat_split)
    longitude = splitted[4].replace("+", "")
    long_split = longitude.split(":")
    #print(long_split)
    lat_0 = float(lat_split[0])
    lat_1 = float(lat_split[1]) / 60
    lat_2 = float(lat_split [2]) / 3600
    
    long_0 = float(long_split[0])
    long_1 = float(long_split[1]) / 60
    long_2 = float(long_split[2]) / 3600
    lat_new = float(lat_0+lat_1+lat_2)
    long_new = float(long_0+long_1+long_2)
    
    # print(lat_new)
    # print(long_new)
    station_points = HPoint(long_new,lat_new)
    #print(station_points)
    stations.append(station_points)

#Transformation of Geometries

crsHelper = HCrs()
crsHelper.from_srid(4326) #lat, long system 
crsHelper.to_srid(3857)


canvas = HMapCanvas.new()
osm= HMap.get_osm_layer()
canvas.set_layers([osm])
for item in stations: 
    stations_3857 = crsHelper.transform(item)
    canvas.add_geometry(stations_3857, "red", 2)
canvas.set_extent([-100000,4000000,5000000,10000000])
canvas.show()

country_dict = {}
country = []
for line in lines:
    line = line.strip()
    if line.startswith("#")or len(line) == 0:
        continue
    splitted = line.split(",")
    countries = splitted[2]
    country.append(countries)
for character in country:
    count = country_dict.get(character, 0)
    count += 1
    country_dict[character] = count
 
for key, value in country_dict.items():
    print(f" {key}: {value}")

################################################################################

# Exercise 03
#distance function #minimum distance in degrees
distances = []
university = HPoint(11.34999, 46.49809)
print(university)


for item in stations:
    distance = university.distance(item)
    distances.append(distance)
min_distance = min(distances)

names = []
for line in lines:
    line = line.strip()
    if line.startswith("#")or len(line) == 0:
        continue
    splitted = line.split(",")
    name = splitted[1]
    names.append(name)
    
for n,s,d in zip(names, stations,distances):
    if d == min_distance:
        print(f"{n}->{s}")
        
################################################################################

#Exercise 03 in class
def fromLatString(latString):
    latDegrees = float(latString[0:3])
    latMinutes = float(latString[4:6])
    latSeconds = float(latString[7:9])
    lat = latDegrees + latMinutes/60 + latSeconds/3600
    return lat 
    
def fromLonString(lonString):
    lonDegrees = float(lonString[0:4])
    lonMinutes = float(lonString[5:7])
    lonSeconds = float(lonString[8:10])
    lon = lonDegrees + lonMinutes/60 + lonSeconds/3600
    return lon 
lon = 11.34999
lat = 46.49809
stationsFile = r"C:\Users\miria\OneDrive\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics\stations.txt"
centerPoint = HPoint(lon, lat)

with open(stationsFile, "r") as file:
    lines = file.readlines()

minDistance = 9999
nearestStationName = "None"
nearestDistancePoint = None

for line in lines[1:10]:
    line = line.strip()
    
    lineSplit = line.split(",")
    name = lineSplit[1].strip()
    latString = lineSplit[3]
    lonString = lineSplit[4]
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    point = HPoint(lonDec, latDec)
    
    distance = point.distance(centerPoint)
    if distance < minDistance: 
        minDistance = distance
        nearestStationName = name
        nearestDistancePoint = point

print(nearestStationName, "->", nearestDistancePoint)
    
################################################################################

# Exercise 04
radius = 20000
university = HPoint(11.34999, 46.49809)
crsHelper = HCrs()
crsHelper.from_srid(4326) #lat, long system 
crsHelper.to_srid(3857)
check_point = crsHelper.transform(university)
buffered = check_point.buffer(radius)

canvas = HMapCanvas.new()
osm= HMap.get_osm_layer()
canvas.set_layers([osm])
canvas.add_geometry(check_point, "black", 2)
#canvas.add_geometry(buffered)
canvas.set_extent([-100000,4000000,5000000,10000000])
canvas.show()

intersected_stations = []
stations_3857 = []
for item in stations: 
    station_3857 = crsHelper.transform(item)
    stations_3857.append(station_3857)
for n,s,d in zip(names, stations_3857, distances):
    if s.intersects(buffered):
        canvas.add_geometry(s, "red", 2)
        print(f"{n}({d})-> {s}")
canvas.show()

################################################################################

# Exercise 04 in class

lon = 11.34999
lat = 46.49809
radiusKm = 20.0

stationsFile = r"C:\Users\miria\OneDrive\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics\stations.txt"
centerPoint = HPoint(lon, lat)

with open(stationsFile, "r") as file:
    lines = file.readlines() 

crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(32632)

centerPoint32632 = crsHelper.transform(centerPoint)

buffer = centerPoint32632.buffer(radiusKm*1000)

for line in lines[1:]:
    line = line.strip()
    
    lineSplit = line.split(",")
    name = lineSplit[1].strip()
    latString = lineSplit[3]
    lonString = lineSplit[4]
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    
    point = HPoint(lonDec, latDec)
    point32632 = crsHelper.transform(point)
    
    if buffer.intersects(point32632):
        distance = point32632.distance(centerPoint32632)
        print(name, distance/1000, point)




       
        

        

        
