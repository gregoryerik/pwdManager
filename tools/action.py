
class Command:

    def __init__(self, command=None):
        self.command = command
    
    def set_command(self, command):
        self.command = command

    def get_commands(self):
        commands = {"quit": self.quit, "help": self.help}
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
  ## return back to the original TODO

class SingleAction:
    pass

class Run:
    pass