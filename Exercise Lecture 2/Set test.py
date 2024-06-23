# Set test
from pyqgis_scripting_ext.core import *
coords_g1 = [[0,0], [5,0], [5,5], [0,5], [0,0]]
coords_g2 = [[5,0], [7,0], [7,2], [5,2], [5,0]]
g3 = HPoint(4,1)
g4 = HPoint(5,4)
coords_g5 = [[1,0], [1,6]]
coords_g6 = [[3,3], [3,6], [6,6], [6,3], [3,3]]

g1 = HPolygon.fromCoords(coords_g1)
g2 = HPolygon.fromCoords(coords_g2)
print(g3.asWkt())
print(g4.asWkt())
g5 = HLineString.fromCoords(coords_g5)
print(g5)
g6 = HPolygon.fromCoords(coords_g6)


canvas = HMapCanvas.new()
canvas.add_geometry(g1, "black", 2)
# canvas.add_geometry(g2, "magenta", 2)
# canvas.add_geometry(g3, "blue", 2)
# canvas.add_geometry(g4, "red", 2)
# canvas.add_geometry(g5, "green", 2)
canvas.add_geometry(g6, "orange", 2)
# canvas.set_extent([0,0,7,7])
# canvas.show()

print("polygon boundingbox.", g1.bbox())
print("polygon length:", g1.length())
print("polygon area:", g1.area())

print("line length:", g5.length())
print("line area:", g5.area())

print("point length:", g3.length())
print("line area:", g3.area())

print("distance between line and point:", g5.distance(g4))

#PREDICATES
print("intersects")
print(g1.intersects(g2))
print(g1.intersects(g3))
print(g1.intersects(g4))
print(g1.intersects(g5))
print(g1.intersects(g6))

#the intersection funciton also contains touches!

print("touches")
#at least one point in common, but do not any interior (it needs to be the border)
print(g1.touches(g2))
print(g1.touches(g3))
print(g1.touches(g4))
print(g1.touches(g5))
print(g1.touches(g6))

print("contains")
print(g1.contains(g2))
print(g1.contains(g3))
print(g1.contains(g4))
print(g1.contains(g5))
print(g1.contains(g6))
#--> only the blue dot

#FUNCTIONS
print("intersection")
print(g1.intersection(g2))
print(g1.intersection(g3))
print(g1.intersection(g4))
print(g1.intersection(g5))
print(g1.intersection(g6))
newGeom = g1.intersection(g6)

print("symdifference")
print(g1.symdifference(g2))
print(g1.symdifference(g3))
print(g1.symdifference(g4))
print(g1.symdifference(g5))
print(g1.symdifference(g6))
newGeom = g1.symdifference(g6)

#symdifference is the inverse of intersection --> not common portions of  polygons

print("union")
print(g1.union(g2))
print(g1.union(g3))
print(g1.union(g4))
print(g1.union(g5))
print(g1.union(g6))
newGeom = g1.union(g6)
# = merge of the 2 polygons

print("difference")
print(g6.difference(g1))
print(g1.difference(g5))
newGeom = g6.difference(g1)

print("buffers")
b1 = g3.buffer(1.0)
b2 = g3.buffer(1.0,8) #Zahl nach dem Komma beschreibt die Annäherung an einen Kreis
#Wenn ,1 --> Rechteck, normalerweise wird ,8 benutzt
b3 = g5.buffer(1)
b4 = g5.buffer(1,2)
b5 = g5.buffer(1, -1, JOINSTYLE_ROUND, ENDCAPSTYLE_SQUARE)

collection = HGeometryCollection([g1, g2, g3, g4, g5, g6])
hull = collection.convex_hull()

canvas = HMapCanvas.new()
canvas.add_geometry(collection, "grey", 2)
canvas.add_geometry(hull, "black", 2)
canvas.add_geometry(g5, "green", 2)
canvas.add_geometry(b1, "orange", 2)
canvas.add_geometry(b2, "red", 2)
canvas.add_geometry(b3, "green", 2)
canvas.add_geometry(b4, "blue", 2)
canvas.add_geometry(b5, "violet", 2)
canvas.add_geometry(newGeom, "magenta", 3)
canvas.set_extent([-1,-1,8,8])
canvas.set_extent(hull.bbox())
canvas.show()




