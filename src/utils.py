from json import load
from os.path import exists

def load_json_file(path):
    """
    Load a Json file.

    Args:
        path (str): Path of Json file.

    Returns:
        dict: Dictionnary with data in Json file.
    """
    with open(path, mode = "r", encoding = "utf8") as f:
        data = load(f)

    return data