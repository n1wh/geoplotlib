from geoplotlib.core import BaseApp
from geoplotlib.layers import ScatterLayer, HistogramLayer, GraphLayer, PolyLayer, VoronoiLayer, MarkersLayer, \
    DelaunayLayer, KDELayer


class AppConfig:

    def __init__(self):
        self.reset()


    def reset(self):
        self.layers = []
        self.bbox = None
        self.savefig = None
        self.tiles_provider = 'toner'
        self.smoothing = True


_global_config = AppConfig()


def _runapp(app_config):
    try:
        app = BaseApp(app_config)
        app.start()
    finally:
        app.close()
        _global_config.reset()



def show():
    _runapp(_global_config)


def savefig(fname):
    _global_config.savefig = fname
    _runapp(_global_config)


def scatter(data, color=None, point_size=6, f_tooltip=None):
    _global_config.layers.append(ScatterLayer(data, color=color, point_size=point_size, f_tooltip=f_tooltip))


def hist(data, cmap='Blues', alpha=220, logscale=False, binsize=16, show_tooltip=False, vmin=0, f_group=None,
         binscaling=False):
    _global_config.layers.append(HistogramLayer(data, cmap=cmap, alpha=alpha, binsize=binsize,
            show_tooltip=show_tooltip, vmin=vmin, f_group=f_group, logscale=logscale, binscaling=binscaling))


def graph(data, src_lat, src_lon, dest_lat, dest_lon, **kwargs):
    _global_config.layers.append(GraphLayer(data, src_lat, src_lon, dest_lat, dest_lon, **kwargs))


def clear():
    _global_config.layers = []


def tiles_provider(tiles_provider):
    _global_config.tiles_provider = tiles_provider


def add_layer(layer):
    _global_config.layers.append(layer)


def shapefiles(fname, **kwargs):
    _global_config.layers.append(PolyLayer(fname, **kwargs))


def voronoi(data, **kwargs):
    _global_config.layers.append(VoronoiLayer(data, **kwargs))


def delaunay(data, **kwargs):
    _global_config.layers.append(DelaunayLayer(data, **kwargs))


def kde(data, **kwargs):
    _global_config.layers.append(KDELayer(data, **kwargs))


def markers(data, marker, **kwargs):
    _global_config.layers.append(MarkersLayer(data, marker, **kwargs))


def set_bbox(bbox):
    _global_config.bbox = bbox


def set_smoothing(smoothing):
    _global_config.smoothing = smoothing
