import subprocess
#com.apple.preferences.users

subprocess.check_output(["osascript",
        "-e", "tell application \"System Events\" to set the visible of every process to true",
        "-e", "set white_list to {\"Finder\"}",    
        "-e", "try",
        "-e", "tell application \"Finder\"",
        "-e", "set process_list to the name of every process whose visible is true",
        "-e", "end tell",
        "-e", "repeat with i from 1 to (number of items in process_list)",
        "-e", "set this_process to item i of the process_list",
        "-e", "if this_process is not in white_list then",
        "-e", "tell application this_process",
        "-e", "quit",
        "-e", "end tell",
        "-e", "end if",
        "-e", "end repeat",
        "-e", "on error",
        "-e", "tell the current application to display dialog \"An error has occurred!\" & return & \"This script will now quit\" buttons {\"Quit\"} default button 1 with icon 0",  
        "-e", "end try"]).strip()


