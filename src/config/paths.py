import json
import os


class Paths:
    paths = dict()

    @classmethod
    def initialize(cls, filename):
        """
        Initialize the class data with the file

        Args:
            filename (str): path to the file data
        """

        cls.paths.clear()
        with open(filename, encoding="utf-8") as f:
            cls.paths.update(json.load(f))

    @classmethod
    def folder(cls, key):
        """
        Return the absolute path of the folder specified by its ``key``.
        The ``key`` should be in the path.json file.

        Args:
            key (str): key associated to a folder

        Returns:
            str: absolute path of a folder
        """

        p = cls.paths["folders"][key]
        return os.path.abspath(os.path.join(*p))

    @classmethod
    def file(cls, key):
        """
        Return the absolute path of the file specified by its ``key``.
        The ``key`` should be in the path.json file.

        Args:
            key (str): key associated to a file

        Returns:
            str: path to the file
        """

        folder, *p = cls.paths["files"][key]
        folder = cls.folder(folder)
        return os.path.abspath(os.path.join(folder, *p))

    @classmethod
    def image(cls, key):
        """
        Return the absolute path of the image specified by its ``key``.
        The ``key`` shoulf be in the path.json file.

        Args:
            key (str): key associated to the image

        Returns:
            str: path to the image
        """

        p = cls.paths["images"][key]
        folder = cls.folder("r_images")
        return os.path.abspath(os.path.join(folder, p))
