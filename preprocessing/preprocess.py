from typing import Dict, List, Any, Tuple, Optional
import pandas as pd
from utils.utils import json_abort


def _check_required(data: Dict) -> bool:
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


def _check_types(data: Dict,
                 fields: List,
                 fields_type: Any) -> Tuple[bool, Optional[List]]:
    invalid_fields = []
    for field in fields:
        if data.get(field, None):
            if type(data[field]) is not fields_type:
                invalid_fields.append(field)
    if invalid_fields:
        return False, invalid_fields
    return True, None


def _validate_types(data: Dict) -> bool:
    invalid_fields = []
    int_fields = [
        "zip-code",
        "rooms-number",
        "area",
        "terrace_area",
        "garden_area",
        "land_surface",
        "garden_area",
        "facades_count"
    ]
    bool_fields = [
        "equipped-kitchen",
        "furnished",
        "open-fire",
        "terrace",
        "garden",
        "swimming-pool",
    ]
    if data.get("property-type", None) not in ["HOUSE", "APARTMENT"]:
        invalid_fields.append("property-type")
    int_check = _check_types(data, int_fields, int)
    if not int_check[0]:
        invalid_fields.extend(int_check[1])
    bool_check = _check_types(data, bool_fields, bool)
    if not bool_check[0]:
        invalid_fields.extend(int_check[1])
    if invalid_fields:
        json_abort(400, f"Invalid type"
                        f" for field{'s' if len(invalid_fields) > 1 else ''}:"
                        f" {','.join(invalid_fields)}")

    return True


def preprocess(data: Dict) -> pd.DataFrame:
    _check_required(data)
    _validate_types(data)
    df_dict: Dict = {
        "location": [data["zip-code"]],
        "type": [data["property-type"]],
        "subtype": [data.get("property-subtype", data["property-type"])],
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
        "facade_count": [data.get("facades-number", None)],
        "swimming_pool": [data.get("swimming-pool", False)],
        "building_condition": [data.get("building-state", None)]
    }
    print(df_dict)
    return pd.DataFrame.from_dict(df_dict)
