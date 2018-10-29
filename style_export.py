from qgis.core import *

target_dir = "/usr/local/google/home/ewappel/qml/"
# qml cloudtop -> mac, run on mac:
# scp ewappel@eww125.c.googlers.com:~/qml/*.* ~/qml/


layer_list = []

layers = iface.legendInterface().layers()
for layer in layers:
    #print layer.name()
    layer_list.append(layer.name())
    
registry = QgsMapLayerRegistry.instance()
print layer_list
for x in range(0,len(layer_list)):
    target_file = target_dir + layer_list[x] + ".qml"
    print target_file
    layer = registry.mapLayersByName(layer_list[x])[0]
    layer.saveNamedStyle(target_file)

# zoom to
vl.selectAll()
mCanvas = iface.mapCanvas()
mCanvas.zoomToSelected()
vl.removeSelection()
mCanvas.zoomByFactor(1.1)
    
