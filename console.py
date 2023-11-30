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

	def do_show(self, arg):
		"""Print the string representation of an instance."""
		if not arg:
			print("** class name missing **")
		else:
            args = arg.split()
            if args[0] not in storage.all():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all()[args[0]]:
                    print("** no instance found **")
                else:
                    print(storage.all()[args[0]][key])

	def do_destroy(self, arg):
		"""Deletes an instance based on the class name and id."""
		if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.all():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all()[args[0]]:
                    print("** no instance found **")
                else:
                    del storage.all()[args[0]][key]
                    storage.save()

	def do_all(self, arg):
		"""Prints all string representation of all instances."""
    	args = arg.split()
   		if not arg or args[0] not in storage.all():
        	print("** class doesn't exist **")
    	else:
        	instances = []
        	for key in storage.all()[args[0]]:
            	instances.append(str(storage.all()[args[0]][key]))
        	print(instances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
