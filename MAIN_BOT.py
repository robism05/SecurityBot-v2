import subprocess, os, time
import discord
from discord.ext import commands
from subprocess import call
from time import gmtime, strftime
import socket
import platform

client = discord.Client()


# -- functions --

# screenshot
def take_screen_shot():
  # save screen shots where
  call(["screencapture", "Screenshot" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".jpg"])

# checks if app is open
def is_runnning(app):
  count = int(subprocess.check_output(["osascript",
              "-e", "tell application \"System Events\"",
              "-e", "count (every process whose name is \"" + app + "\")",
              "-e", "end tell"]).strip())
  return count > 0


# gets ip address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'     
    finally:
        s.close()
    return IP



# discord bot
@client.event
async def on_ready():
  print("Program has logged in as {0.user}".format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if client.user.mentioned_in(message):
    if platform.system=="Darwin":
      await message.channel.send('You mentioned me! (macOS)')
    if platform.system=="Windows":
      await message.channel.send('You mentioned me! (windows)')
    else:
      await message.channel.send('You mentioned me! (other)')


  elif message.content.startswith("!quitMac"):
    await message.channel.send('Goodbye!')
    exit()


  # System Preferences
  SysPref=(is_runnning("System Preferences"))
  process = subprocess.Popen(["sleep","0.5"])
  if SysPref == True:
    while process.poll() == None:
      print("polling")
      time.sleep(0.05)
    await message.channel.send('Someone has opened System Preferences!')
    print("process finished") 
    

  # bot commands   
  if message.content.startswith("!close SysPref") and SysPref==True:
    os.system("pkill System Preferences")
    await message.channel.send("System Preferences closed!")
  elif message.content.startswith("!close SysPref") and SysPref==False:
    await message.channel.send("System Preferences is not open")
  elif message.content.startswith("!open SysPref"):
    os.system("""osascript -e 'tell app "System Preferences" to open'""")
    await message.channel.send("System Preferences opened")



  elif message.content.startswith("!screenshot"):
    take_screen_shot()
    for file in os.listdir("/Users/iamfire297/Desktop/PythonDev/SecurityBot"):
      if file.endswith(".jpg"):
        await message.channel.send(file=discord.File(file))
        time.sleep(2)
        os.remove(file)

    '''''
    if platform.system=="Windows":
      import PIL.ImageGrab
      screenshot = PIL.ImageGrab.grab()
      screenshot.save("Windows_screenshot.jpg")
      screenshot.close()
      for file in os.listdir("SecurityBot"):
        if file.endswith(".jpg"):
          await message.channel.send(file=discord.File(file))
          time.sleep(2)
          os.remove(file)
    '''


  elif message.content.startswith("!sleep"):
    await message.channel.send("Putting your mac to sleep in 5 seconds...")
    os.system('osascript sleep.scpt {} "{}"')
  
  elif message.content.startswith("!record"):
    await message.channel.send("Recording your webcam... ")
    os.system('osascript record.scpt {} "{}"')
    for file in os.listdir("/Users/iamfire297/Desktop/PythonDev/SecurityBot"):
      if file.endswith(".mov"): 
        await message.channel.send(file=discord.File(file))
        time.sleep(2)
        os.remove(file)

  elif message.content.startswith("!info"):
    h_name = socket.gethostname()
    IP_addres = socket.gethostbyname(h_name)
    await message.channel.send("**Operating System:** "+platform.system())
    await message.channel.send("**Host Name is:** " + h_name)
    await message.channel.send("**Computer IP Address (localhost) is:** " + IP_addres)
    await message.channel.send(get_ip()+"\n")
      
  elif message.content.startswith("!rickroll"):
    os.system('osascript rickroll.scpt {} "{}"')
    

    

client.run('OTM5NTM4NzY3NjU0NTUxNjUy.Yf6TqQ.f3YXDH57TjNKvHjn-wwm5DusOBM')
