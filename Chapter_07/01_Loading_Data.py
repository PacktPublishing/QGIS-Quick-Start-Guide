Airport_layer = iface.addVectorLayer('D:/QGIS_quickstart/qgis_sample_data/shapefiles/airports.shp','airports','ogr')
Alaska_layer = iface.addVectorLayer('D:/QGIS_quickstart/qgis_sample_data/shapefiles/alaska.shp','alaska','ogr')

print (Airport_layer.name())

print (Airport_layer.featureCount())

## print the attribute table
airportFeatures = Airport_layer.getFeatures()
for feature in airportFeatures:
	print (feature.attributes())
