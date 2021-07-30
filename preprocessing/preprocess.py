from typing import Dict
import pandas as pd
from utils.utils import json_abort


def _validate(data: dict) -> bool:
    required = [
        "zip-code",
        "property-type",
        "rooms-number",
        "area"
    ]
    for i in required:
        if i not in data:
            json_abort(400, {"error": f"Missing required field {i}"})
    return True


def preprocess(data: Dict) -> pd.DataFrame:
    if not _validate(data):
        raise Exception()
    df_dict: Dict = {
        "location": [data["zip-code"]],
        "type": [data["property-type"]],
        "subtype": [data.get("property-subtype", None)],
        "room_number": [data["rooms-number"]],
        "area": [data["area"]],
        "kitchen_equipped": [data.get("equipped-kitchen", False)],
        "furnished": [data.get("furnished", False)],
        "fireplace": [data.get("open-fire", False)],
        "terrace": [data.get("terrace", False)],
        "terrace_area": [data.get("terrace-area", 0)],
        "garden": [data.get("garden", False)],
        "garden_area": [data.get("garden-area", 0)],
        "land_surface": [data.get("land-area", 0)],
        "facades_count": [data.get("facades-number", None)],
        "swimming_pool": [data.get("swimming-pool", False)],
        "building_condition": [data.get("building-state", None)]
    }
    return pd.DataFrame.from_dict(df_dict)
