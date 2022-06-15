import shutil
import time
import os
import datetime
from discord_webhook import DiscordWebhook

print(""" ________  ___    ___ _____ ______   ________  ___      ___ _______   ________     
|\   __  \|\  \  /  /|\   _ \  _   \|\   __  \|\  \    /  /|\  ___ \ |\   __  \    
\ \  \|\  \ \  \/  / | \  \\\__\ \  \ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \   
 \ \   ____\ \    / / \ \  \\|__| \  \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\  
  \ \  \___|\/  /  /   \ \  \    \ \  \ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \| 
   \ \__\ __/  / /      \ \__\    \ \__\ \_______\ \__/ /     \ \_______\ \__\\ _\ 
    \|__||\___/ /        \|__|     \|__|\|_______|\|__|/       \|_______|\|__|\|__|
         \|___|/                                                                   \n""")

def menu():
    print("[1] Run")
    print("[2] Exit\n")

def main_app(r):
    
    file_source = 'E:\MoviesSource/'
    file_destination = 'E:\Movies/'
    path_to_watch = file_source
    #discordwebhookid = ''
    now = datetime.datetime.now()

    time.sleep(1)
    get_source = os.listdir(file_source)
    get_destination = os.listdir(file_destination)

    #print("Source: ", get_source)
    #print("Local: ", get_destination)

    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    if added or r:
        for g in get_source:
            if os.path.exists(file_destination+g):
                print(now.strftime("[%Y-%m-%d %H:%M:%S]"), "Skipped!: ", g)
            else:
                time.sleep(3)
                shutil.move(file_source + g, file_destination)
                print(now.strftime("[%Y-%m-%d %H:%M:%S]"), "Moved:", g)

                #webhook = DiscordWebhook(url=(discordwebhookid), content='Moved: ' + g)
                #response = webhook.execute()
    

        r = False

menu()


option = int(input("Enter your option: "))
ans = True

f_r = True

while ans:
    if option == 1:
        main_app(f_r)
    elif option == 2:
        exit()
    else:
        print("Invalid option.")