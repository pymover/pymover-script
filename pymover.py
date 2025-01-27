import shutil
import time
import os
import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='discord-webhook-link')

def logo(path=''):
    print('                                                                                       ')
    print('   ▄███████▄ ▄██   ▄     ▄▄▄▄███▄▄▄▄    ▄██████▄   ▄█    █▄     ▄████████    ▄████████ ')
    print('  ███    ███ ███   ██▄ ▄██▀▀▀███▀▀▀██▄ ███    ███ ███    ███   ███    ███   ███    ███ ')
    print('  ███    ███ ███▄▄▄███ ███   ███   ███ ███    ███ ███    ███   ███    █▀    ███    ███ ')
    print('  ███    ███ ▀▀▀▀▀▀███ ███   ███   ███ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ')
    print('▀█████████▀  ▄██   ███ ███   ███   ███ ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ')
    print('  ███        ███   ███ ███   ███   ███ ███    ███ ███    ███   ███    █▄  ▀███████████ ')
    print('  ███        ███   ███ ███   ███   ███ ███    ███ ███    ███   ███    ███   ███    ███ ')
    print(' ▄████▀       ▀█████▀   ▀█   ███   █▀   ▀██████▀   ▀██████▀    ██████████   ███    ███ ')
    print('                                                                                       ')
logo()
def menu():
    print("[1] Run")
    print("[2] Settings")
    print("[3] Exit\n")

def clear(): 
    os.system('cls')

def main_app(r):
    
    file_source = 'enter-file-source-path'
    file_destination = 'enter-file-destination-path'
    path_to_watch = file_source
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
            #if file in file_destination exists skippes file
            if os.path.exists(file_destination+g):
                time.sleep(40)
                #console oupout if file is skipped
                print(now.strftime("[%Y-%m-%d %H:%M:%S]"), "Skipped!: ", g)
            else:
                #moves file to file_destination
                time.sleep(3)
                shutil.move(file_source + g, file_destination)
                #console output if file is moved
                print(now.strftime("[%Y-%m-%d %H:%M:%S]"), "Moved:", g)

                #discord message if file is moved
                embed = DiscordEmbed(color='000000')
                embed.set_author(name='Pymover', url='https://github.com/MathiasKiwi', icon_url='https://avatars.githubusercontent.com/u/107579533?s=200&v=4')
                embed.add_embed_field(name='Moved movie:', value=g)
                embed.set_footer(text='Pymover')
                embed.set_timestamp()

                webhook.add_embed(embed)
                response = webhook.execute()

        r = False
menu()

option = int(input("Enter your option: "))

clear()

logo()
print("Type 'exit' to return to the main menu.\n")



ans = True

f_r = True

while ans:
    if option == 1:
        main_app(f_r)
    elif option == 2:
        exit()
    else:
        print("Invalid option.")