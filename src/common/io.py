import json


def json_load(path:str):
    """
    Load the json data in the path

    Args:
        path (str): path to the file data

    Returns:
        dict or list: json data
    """

    with open(path) as f:
        return json.load(f)


def json_save(data, path:str):
    """
    Save the data to json at the given path

    Args:
        data (dict or list): data to save
        path (str): path to file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
