import json
import os

class Config:
    cfg = dict()
    path = str()

    @classmethod
    def initialize(cls, filename):
        """
        Initialize the class data with the file

        Args:
            filename (str): path to the file data
        """

        cls.path = filename
        cls.cfg.clear()
        with open(filename, encoding="utf-8") as f:
            cls.cfg.update(json.load(f))

    @classmethod
    def get(cls, path_param):
        """
        Return the configuration value at path_param

        Args:
            path_param (str): The path to the paramter in the json file

        Returns:
            json: a json stored value
        """

        keys = path_param.split("/")

        c = cls.cfg
        for key in keys:
            c = c[key]

        return c

    @classmethod
    def set(cls, path_param, value):
        """
        Set the configuration value at path_param

        Args:
            path_param (str): The path to the parameter in the json file
            value (json): a json value
        """

        keys = path_param.split("/")

        c = cls.cfg
        for key in keys[:-1]:
            c = c[key]

        c[keys[-1]] = value

        with open(cls.path, "w") as f:
            json.dump(cls.cfg, f, indent=4)
