route_data = {}

def set_route_data(key, value):
    route_data[key] = value

def get_route_data(key):
    return route_data.get(key)