defaults = {
    'maxcpu': {'default': 0, 'shown': True},
    'maxdisk': {'default': 0, 'shown': True},
    'maxmem': {'default': 0, 'shown': True},
    'cpu': {'default': 0, 'shown': True},
    'disk': {'default': 0, 'shown': True},
    'mem': {'default': 0, 'shown': True},
    'uptime': {'default': 0, 'shown': True},
    'template': {'default': 0, 'shown': True},
    'pool': {'default': "", 'shown': True},
    'name': {'default': "", 'shown': True},
    'lock': {'default': "", 'shown': True},
    'tags': {'default': "", 'shown': True}
}

class PVEBase:
    columns = []
    def __init__(self, **kwargs):
        for param in self.__class__.columns:
            if isinstance(param, tuple):
                from_name, to_name = param
            else:
                from_name = to_name = param
            default_value = defaults.get(from_name, {}).get('default')
            if param == 'tags':
                setattr(self, to_name, kwargs.get(from_name, default_value).split(";"))
            else:
                setattr(self, to_name, kwargs.get(from_name, default_value))
        self._metadata = {
            param: {k: v for k, v in defaults.get(param, {}).items() if k != 'default'}
            for param in self.__class__.columns
        }
