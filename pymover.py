import shutil
import time
import os
from datetime import datetime


file_source = 'E:\MoviesSource/'
file_destination = 'E:\Movies/'

def logo():
    print(""" ________  ___    ___ _____ ______   ________  ___      ___ _______   ________     
|\   __  \|\  \  /  /|\   _ \  _   \|\   __  \|\  \    /  /|\  ___ \ |\   __  \    
\ \  \|\  \ \  \/  / | \  \\\__\ \  \ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \   
 \ \   ____\ \    / / \ \  \\|__| \  \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\  
  \ \  \___|\/  /  /   \ \  \    \ \  \ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \| 
   \ \__\ __/  / /      \ \__\    \ \__\ \_______\ \__/ /     \ \_______\ \__\\ _\ 
    \|__||\___/ /        \|__|     \|__|\|_______|\|__|/       \|_______|\|__|\|__|
         \|___|/                                                                   \n""")

def clearConsole():
    os.system("cls")

def menu():
    print("[1] Run")
    print("[2] Exit\n")

def option1():
    path_to_watch = file_source



    time.sleep(1)
    get_source = os.listdir(file_source)
    get_destination = os.listdir(file_destination)

    #print("Source: ", get_source)
    #print("Local: ", get_destination)

    for g in get_source:
        if os.path.exists(file_destination+g):
            print("Skipped!", g)
        else:
            time.sleep(3)
            shutil.move(file_source + g, file_destination)
            print('Moved:', g)

def option2():
    exit()

def drawMainmenu():
    logo()
    menu()



drawMainmenu()
option = ""
try:
    option = input('Enter one of the options above: ')
except:
    print('Wrong input. Please enter a number ...')

while option != "null":
    # break the cycle --V
    if option == "0":
        option = "null"
    # program --V
    elif option == "1":
        option1()
    # break the exit --V
    elif option == "2":
        option2()
