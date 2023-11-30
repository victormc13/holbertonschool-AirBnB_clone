#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
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
	try:
	    new_instance = eval(arg)()
	    new_instance.save()
	    print(new_instance.id)
	except NameError:
	    print( "** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
