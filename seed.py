"""Utility file to geocode data by place name to lat/lon."""

import google_places as geocoder  # my google places api file
import geojson


def import_placenames():
    """Load place names from .csv file."""

    geocoded_places = []

    # Read data file and insert data.
    for row in open("data/locations.csv"):
        row = row.rstrip()
        city, state, country = row.split(",")

        if not state:
            location = city + ", " + country
        else:
            location = city + ", " + state + ", " + country

        # Make Google Places API request!
        places = geocoder.get_google_places(location)

        if places:
            place_id, lat, lng = geocoder.extract_geo(places)
            print place_id, lat, lng

        else:
            place_id = 0
            lat = 0
            lng = 0

        geocoded_places.append((place_id, lat, lng))

    return geocoded_places


def write_geojson():
#     """Save geocoder results as geojson file."""

    features = []

    format_geojson = geojson.FeatureCollection(features)

    geocoded_places = import_placenames()

    for geocoded in geocoded_places:
        place_id = geocoded[0]
        lat = float(geocoded[1])
        lng = float(geocoded[2])
        feature = geojson.Feature(geometry=geojson.Point((lng, lat)), properties={"name": place_id})
        features.append(feature)

    f = open("locations.geojson", "w")
    geojson.dump(format_geojson, f)
    f.close()

write_geojson()
