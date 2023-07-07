#!/usr/bin/python3
""""""
import cmd


class HBNBCommand(cmd.Cmd):
    """"""

    prompt = '(hbtn) '

    def do_quit(self, arg):
        """HOla"""
        return True

    def do_EOF(self, arg):
        """Hola"""
        return True

    def emptyline(self):
        """Hola"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()