from termcolor import colored

# Bold Yellow [NOTE] that displays at the front of a print statement
# Used in event of an alert where nothing good/bad happens. Like an FYI
NOTE = colored("[NOTE] ", "yellow", attrs=['bold'])

# Bold Red [WARNING] that displays at the front of a print statement
# Used when an error has been caught to alert the user. Like alarms and sirens
WARNING = colored("[WARNING] ", "red", attrs=['bold'])

# Bold Green [SUCCESS] that displays at the front of a print statement
# Used when something notable has finished and nothing went wrong
SUCCESS = colored("[SUCCESS] ", "green", attrs=['bold'])