import json
import os

from django.conf import settings


def get_coords(travels: list):
    coords = []
    with open(os.path.join(settings.BASE_DIR, "travels/json/countries_coord.json"), "r") as f:
        data = json.loads(f.read())
    for travel in travels:
        coords.append(data[travel.country.code][::-1])
    return coords
