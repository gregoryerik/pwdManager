import sys
import tools.prefix as pfx

class Command:

    def __init__(self, command=None):
        self.command = command
        self.attachment = None
        self.exit_condition = False
    
    def attach_secondary(self, attachment):
        self.attachment = attachment
    
    def set_command(self, command):
        self.command = command

    def get_commands(self):
        commands = {"quit": self.quit, "help": self.help, "password": self.password}
        return commands

    def handle_command(self):
        commands = self.get_commands()
        if self.command in commands.keys():
            commands[self.command]()
    
    """
    THE COMMANDS 
    """

    def help(self):
        messages = ["Help messages"]
        for message in messages:
            print(message)

    def quit(self):
        self.exit_condition = True

    def password(self):
        if self.attachment is None:
            print(pfx.WARNING + "Not enough arguments: pwdmn <password> <name>")
            self.quit()
        else:
            """
            
            check if the password is in the database
            if is in the database:
                try get the key
                use key to decrypt pwd
            else:
                print -> cant find the key in the database



            """
            pass

class SingleAction:

    def __init__(self):
        self.commands = sys.argv[1:]
        self.root_command = self.commands[0]
        self.secondary = self.get_secondary()

        self.handle_command()

    def get_secondary(self):
        if len(self.commands) > 1:
            return self.commands[1]
        else:
            return None
    
    def handle_command(self):
        commandHandler = Command(self.root_command)

        if self.secondary is not None:
            commandHandler.attach_secondary(self.secondary)

        commandHandler.handle_command()