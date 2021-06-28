#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = ('(hbnb) ')

    def do_quit(self, arg):
        'Use "quit" command to exit'
        return True

    def do_EOF(self, arg):
        'Press "ctrl + D" to EOF'
        print()
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
