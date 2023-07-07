#!/usr/bin/python3
"""Console for AirBnB project"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Console"""

    prompt = '(hbnb) '
    class_dict = {
        'BaseModel': BaseModel,
        'User': User
    }

    def do_quit(self, arg):
        """Exit to the console
        """
        return True

    def do_EOF(self, arg):
        """Exit to the console
        """
        print()
        return True

    def emptyline(self):
        """Pass an empty line
        """
        pass

    def do_create(self, arg):
        """Create an instance of a class
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            new_obj = self.class_dict[arg]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        """
        arguments = arg.split()
        if not arguments:
            print("** class name missing **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif arguments[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            class_name = arguments[0]
            id_obj = arguments[1]
            key_obj = f"{class_name}.{id_obj}"
            all_objects = models.storage.all()
            if key_obj not in all_objects.keys():
                print("** no instance found **")
            else:
                print(all_objects[key_obj])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        arguments = arg.split()
        if not arguments:
            print("** class name missing **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif arguments[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            class_name = arguments[0]
            id_obj = arguments[1]
            key_obj = f"{class_name}.{id_obj}"
            all_objects = models.storage.all()
            if key_obj not in all_objects.keys():
                print("** no instance found **")
            else:
                del all_objects[key_obj]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        """
        all_objects = models.storage.all()
        if arg:
            if arg not in self.class_dict.keys():
                print("** class doesn't exist **")
            else:
                list_obj = []
                for k in all_objects:
                    if str(k).startswith(arg):
                        list_obj.append(str(all_objects[k]))
                print(list_obj)
        else:
            print([str(all_objects[k]) for k in all_objects])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        arguments = arg.split()
        if not arguments:
            print("** class name missing **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif len(arguments) < 3:
            print("** attribute name missing **")
        elif len(arguments) < 4:
            print("** value missing **")
        elif arguments[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            class_name = arguments[0]
            id_obj = arguments[1]
            attr = arguments[2]
            value = arguments[3]
            type_value = type(getattr(self.class_dict[class_name], attr, ""))
            key_obj = f"{class_name}.{id_obj}"
            all_objects = models.storage.all()
            if key_obj not in all_objects.keys():
                print("** no instance found **")
            else:
                setattr(all_objects[key_obj], attr, type_value(value))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
