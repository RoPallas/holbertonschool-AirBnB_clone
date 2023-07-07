#!/usr/bin/python3
"""Console for AirBnB project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console"""

    prompt = '(hbtn) '

    def do_quit(self, arg):
        """Exit to the console
        """
        return True

    def do_EOF(self, arg):
        """Exit to the console
        """
        return True

    def emptyline(self):
        """Pass an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
