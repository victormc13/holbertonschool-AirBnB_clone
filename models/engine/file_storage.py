#!/usr/bin/python3

"""
Defines the FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json


class FileStorage:
    """
    FileStorage class for serializing instances to a JSON file
    and deserializing JSON file to instances.

    Private class attributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all objects by <class name>.id
                            (ex: to store a BaseModel object with id=12121212,
                            the key will be BaseModel.12121212)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: Dictionary containing all objects by <class name>.id.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: Instance to be set in __objects.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        save_dict = {}
        for key, obj in self.__object.items():
            save_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as the_file:
            json.dump(save_dict, the_file)

    def reload(self):
        try:
            with open(self.__file_path, enconding='utf-8') as the_file:
                objs = json.load(the_file)
                for k, v in objs.items():
                    class_name = v['__class__']
                    del v['__class__']
                    self.new(eval(class_name)(**v))
        except FileNotFoundError:
            pass
