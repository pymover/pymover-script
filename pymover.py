from calendar import c
import shutil
import time
import os
import datetime
from configparser import ConfigParser


file = "config.ini"
config = ConfigParser()

config.read(file)

if not config.has_section("SETTINGS"):
    config.add_section("SETTINGS")
    config.set("SETTINGS", "source", "E:\MoviesSource/")
    config.set("SETTINGS", "destination", "E:\Movies/")
    config.set("SETTINGS", "sleep_timer", "5")
    config.set("SETTINGS", "discord_webhook_id", "id_here")

with open(file, 'w') as configfile:
    config.write(configfile)

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
    print("[2] Exit\n")

def clear(): 
    os.system('cls')

def settings_menu():

    source_inp = int(input("Enter your option: "))
    dest_inp = int(input("Enter your option: "))

    config.set("SETTINGS", "sleep_timer", "5")


    with open(file, 'w') as configfile:
        config.write(configfile)
        
def main_app(r):

    p_timer = int(config["settings"]["sleep_timer"])
    print(p_timer)
    file_source = config["settings"]["source"]
    file_destination = config["settings"]["destination"]
    path_to_watch = file_source
    now = datetime.datetime.now()

    get_source = os.listdir(file_source)
    get_destination = os.listdir(file_destination)

    print("Source: ", get_source)
    print("Local: ", get_destination)

    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]

    time.sleep(p_timer)

    if added or r:
        for g in get_source:
            if os.path.exists(file_destination+g):
                print(now.strftime("[%Y-%m-%d %H:%M:%S]"), "Skipped!: ", g)
            else:
                time.sleep(3)
                shutil.move(file_source + g, file_destination)
                print(now.strftime("[%Y-%m-%d %H:%M:%S]"), "Moved:", g)
    
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
        settings_menu()
    elif option == 3:
        exit()
    else:
        print("Invalid option.")