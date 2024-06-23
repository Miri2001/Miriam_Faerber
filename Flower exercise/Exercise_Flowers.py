from math import cos, sin, radians
from pyqgis_scripting_ext.core import *

n = 3
d = 2
iterations = max(n,d)
maxAngle = 360*iterations

# define an angle 
coords = []
canvas = HMapCanvas.new()
for angle in range(0, maxAngle, 1):
    radAngle = radians(angle)
    k = n/d
    r = cos(k*radAngle)
    x = r*cos(radAngle)
    y = r*sin(radAngle)
    coords.append([x,y])
    line = HLineString.fromCoords(coords)
    #point_x = HPoint(x,y)
    #canvas.add_geometry(point_x, "red",1)
    canvas.add_geometry(line, "red", 1)
canvas.set_extent(line.bbox())
canvas.show()
