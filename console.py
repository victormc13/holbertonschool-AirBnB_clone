#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn't execute anything"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        else:
            try:
                obj = eval(arg)()
                obj.save()
                print(obj.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        objects = storage.all()
        # class_name_list = []

        # for element in storage.all().keys():
        # class_name = element.split('.')[0]
        # class_name_list.append(class_name)

        if args[0] in storage.classes():
            if len(args) == 2:
                key = f"{args[0]}.{args[1]}"
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        if arg:
            try:
                eval(arg)
            except NameError:
                print("** class doesn't exist **")
                return
        objects = storage.all()
        result = []
        for key in objects:
            if not arg or arg == key.split(".")[0]:
                result.append(str(objects[key]))
        print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        objects = storage.all()
        key = f"{args[0]}.{args[1]}"

        if key not in objects:
            print("** no instance found **")
            return
        if args[2] not in ['id', 'created_at', 'updated_at']:
            setattr(objects[key], args[2], args[3].strip("\""))
            objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
