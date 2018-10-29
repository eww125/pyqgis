for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    layer_name = str(layer.name())
    res = layer.dataProvider().deleteAttributes([2,3,4,5,6,7,8,9,10])
    layer.updateFields()
