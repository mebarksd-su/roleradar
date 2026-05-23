

# =========================
# CITY COORDINATE MAPPING
# Future radar visualization
# =========================

CITY_COORDINATES = {
    "New York City": {
        "lat": 40.7128,
        "lon": -74.0060
    },

    "Boston": {
        "lat": 42.3601,
        "lon": -71.0589
    },

    "Atlanta": {
        "lat": 33.7490,
        "lon": -84.3880
    },

    "Philadelphia": {
        "lat": 39.9526,
        "lon": -75.1652
    },

    "Dallas": {
        "lat": 32.7767,
        "lon": -96.7970
    },

    "Syracuse": {
        "lat": 43.0481,
        "lon": -76.1474
    },

    "California": {
        "lat": 36.7783,
        "lon": -119.4179
    },

    "Texas": {
        "lat": 31.9686,
        "lon": -99.9018
    },

    "Massachusetts": {
        "lat": 42.4072,
        "lon": -71.3824
    },

    "Virginia": {
        "lat": 37.4316,
        "lon": -78.6569
    },

    "Minnesota": {
        "lat": 46.7296,
        "lon": -94.6859
    }
}


# =========================
# GET CITY COORDINATES
# =========================
def get_coordinates(location_name):

    return CITY_COORDINATES.get(location_name)