import json
from pathlib import Path

json_path = Path(__file__).parent.parent / "test_data" / "users.json"


def load_users():
    """Load user information from the JSON file and return it as a dictionary."""
    with open(json_path, encoding="utf-8") as f:
        test_data = json.load(f)
    return test_data
