# Exercise 3 - Countries centroids
folder = r"C:\Users\miria\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics\Miriam_Faerber\data"
geopackagePath = folder + "/natural_earth_vector.gpkg/packages/miniGPKG.gpkg"
countriesName = "ne_50m_admin_0_countries"

schema = {
    "name":"string"
}

centroidsLayer = HVectorLayer.new("centroids", "Point", \
                            "EPSG: 4326", schema)
                            
countryLayer = HVectorLayer.open(geopackagePath, countriesName)

notInCountryList = []

nameIndex = countryLayer.field_index("NAME")
for country in countryLayer.features():
    countryGeom = country.geometry
    name = country.attributes[nameIndex]
    
    centroid = countryGeom.centroid()
    
    centroidsLayer.add_feature(centroid, [name])
    
    if not centroid.intersects(countryGeom):
        notInCountryList.append(name)
    
simpleStyle = HMarker("circle", 10) + HLabel("name") + HHalo()
centroidsLayer.set_style(simpleStyle)
HMap.add_layer(centroidsLayer)

print("Countries with centroids not inside the main polygon:")
for c in notInCountryList: 
    print(c)
    
