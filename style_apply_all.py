from qgis.core import *

import os
home_dir =  os.path.expanduser('~')
directory_path = home_dir + "/qml/"
print directory_path

print "applying style files..."
registry = QgsMapLayerRegistry.instance()
layers = iface.legendInterface().layers()
for layer in layers:
    layer.loadNamedStyle(directory_path + layer.name() + ".qml")
    layer.triggerRepaint()
print "complete!"
