from .bac_updatearea import AreaUpdatePlugin

def classFactory(iface):
    return AreaUpdatePlugin(iface)
