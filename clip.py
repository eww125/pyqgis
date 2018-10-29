# Assuming that you have a layer called "overlay" and another one called "layer_to_clip" loaded.

# get the overlay layer in the console
overlay_layer = [x for x in iface.legendInterface().layers() if x.name() == 'overlay'][0]

# get the layer to clip in the console
layer_to_clip = [x for x in iface.legendInterface().layers() if x.name() == 'layer_to_clip'][0]

# run the algorithm and output the results in /tmp/output.shp

processing.runalg("qgis:clip", overlay_layer, layer_to_clip, "/tmp/output.shp")
