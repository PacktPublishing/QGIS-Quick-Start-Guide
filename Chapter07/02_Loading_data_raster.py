Hillshade_layer = iface.addRasterLayer('D:/QGIS_quickstart/qgis_sample_data/raster/SR_50M_alaska_nad.tif','Hillshade')
Landcover_layer = iface.addRasterLayer('D:/QGIS_quickstart/qgis_sample_data/raster/landcover.img','Landcover')

## print the layer names
print (Hillshade_layer.name())

print (Landcover_layer.name())

## print the image dimensions
print (Hillshade_layer.width(), Hillshade_layer.height())
print (Landcover_layer.width(), Landcover_layer.height())