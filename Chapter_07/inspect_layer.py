Airport_layer.name()
Airport_layer.featureCount()
airportFeatures = Airport_layer.getFeatures()
for feature in airportFeatures:
    print (feature.attributes())
