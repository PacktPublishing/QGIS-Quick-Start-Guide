## Buffering
Airport_layer = iface.addVectorLayer('D:/QGIS_quickstart/qgis_sample_data/shapefiles/airports.shp','airports','ogr')

param = { 'INPUT' : Airport_layer, 'DISTANCE' : 15000, 'SEGMENTS' : 5, 'END_CAP_STYLE' : 0, 'JOIN_STYLE' : 0, 'MITER_LIMIT' : 2, 'DISSOLVE' : False, 'OUTPUT' : 'memory:' }
algoOutput = processing.run("qgis:buffer", param)

Airport_buffer = QgsProject.instance().addMapLayer(algoOutput['OUTPUT'])