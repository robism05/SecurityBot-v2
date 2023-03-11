import colorama #for colored output in terminal
from src import artwork
import os

colorama.init() #initialize colorama for colored output
cf = colorama.Fore

version = "2.0.0"

def menu():
    os.system('clear')
    print(cf.CYAN,artwork.ascii_art)
    print("By rbs5 (alias) et al")
    print("version "+version+"\n\n")
    print("Just a silly program tbh")
menu()

# define list of options
options = ['1: Start SecBot', '2: Communicate', '3: Exit']
print(cf.YELLOW + "Please choose an option:")

# print each option in orange text
for option in options:
    print(cf.YELLOW + option)
print(colorama.Style.RESET_ALL)

# get user input and validate
while True:
    try:
        choice = int(input("Enter your choice (1-%d): " % len(options)))
        if 1 <= choice <= len(options):
            if choice == 1:
                import main
            elif choice == 2:
                print("Coming soon...")
                break
            elif choice == 3:
                exit()
        else:
            print(cf.RED+"Invalid input, please enter a number between 1 and %d" % len(options))
    except ValueError:
        print("Invalid input, please enter a number between 1 and %d" % len(options))

# return user's selection
print("You chose option %d: %s" % (choice, options[choice-1]))


