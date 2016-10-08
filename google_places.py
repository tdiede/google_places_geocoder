# Use Python os.environ to get environmental variables.
# Note: you must run `source secrets.sh` before running
# this file to set required environmental variables.

import os

GOOGLE_PLACES_API_KEY = os.environ['GOOGLE_PLACES_API_KEY']

from googleplaces import GooglePlaces  # external library


def get_google_places(location):
    """Use the Google Places API from the python-google-places library to extract a place object."""

    google_places = GooglePlaces(GOOGLE_PLACES_API_KEY)

    result = google_places.nearby_search(location=location)

    return result.places


def extract_geo(places):
    """Use the Google Places API from the python-google-places library to extract place geo_location, given a place object."""

    for place in places:
        place_id = place.place_id
        lat = place.geo_location['lat']
        lng = place.geo_location['lng']

    return place_id, lat, lng


def extract_names(places):
    """Use the Google Places API from the python-google-places library to extract place names, given a place object."""

    place_names = []

    for place in places:
        place_id = place.place_id
        place_name = place.name
        place_names.append(place_name)

    return place_id, place_names
