import colorama #for colored output in terminal
from src import artwork
import os, platform

colorama.init() #initialize colorama for colored output
cf = colorama.Fore
print(cf)

version = "2.0.0"
repository = "github.com/robism05/Discord-Security-Bot"

def menu():
    os.system('clear')
    print(cf.CYAN,artwork.ascii_art)
    print("======================================================================")
    print("GitHub repository: "+cf.BLUE+repository)
    print(cf.CYAN+"By rbs5 (alias) et al")
    print("version "+version+"\n\n")
    print("Just a silly program tbh")

    # define list of options
    options = ['1: Start SecBot', 
               '2: Communicate', 
               '3: Exit']
    print(cf.YELLOW + "Please choose an option:")
    print("1: Start SecBot")
    print("2: Communicate")
    print("3: Exit")
    print(colorama.Style.RESET_ALL) 
    # get user input and validate
    while True:
        try:
            choice = int(input("Enter your choice (1-%d): " % len(options)))
            if 1 <= choice <= len(options):
                if choice == 1:
                    from src import bot
                    exit()
                elif choice == 2:
                    print("Coming soon...")
                    break
                elif choice == 3:
                    exit()
            else:
                print(cf.RED+"Invalid input, please enter a number between 1 and %d" % len(options))
        except ValueError:
            print("Invalid input, please enter a number between 1 and %d" % len(options))

menu()
