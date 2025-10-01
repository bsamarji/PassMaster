import json
import os


def load_data():
    """
    Load all data from the password vault and return it.
    """
    vault = "./vault.json"
    if os.path.isfile(vault) is False:
        return []
    elif os.stat(vault).st_size == 0:
        return []
    else:
        with open(vault, "r") as f:
            data = json.load(f)
            return data
