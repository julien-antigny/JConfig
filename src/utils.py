from json import load
from os.path import exists

def load_json_file(path, utf8 = True):
    """
    Load a Json file.

    Args:
        path (str): Path of Json file.
        utf8 (bool, optional): Indicate if Json file is encoded in UTF8. Defaults to True.

    Returns:
        dict: Dictionnary with data in Json file.
    """
    assert type(path) == str, "Type of path is not correct"
    assert exists(path), "Path doesn't exist"
    assert type(utf8) == bool, "Type of utf8 is not correct"

    encoding = "utf8" if utf8 else None

    with open(path, mode = "r", encoding = encoding) as f:
        data = load(f)

    return data