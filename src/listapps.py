import subprocess, os, platform
from subprocess import call

def listapps():
  apps = str(subprocess.check_output(["osascript",
            "-e", "tell application \"Finder\"",
            "-e", "get the name of every process whose visible is true",                          
            "-e", "end tell"]).strip())
  b = "b'"
  for char in b:
      apps = apps.replace(char, "")
  apps = apps.replace("Electron", "VS-Code")
  print(apps)

listapps()

#   osascript -e 'set text item delimiters to "\n"' \
#   -e 'tell application "System Events" to ¬
#   (name of every application process whose background only is false) as string' | sort

