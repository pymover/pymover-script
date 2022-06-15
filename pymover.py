import shutil
import time
import os

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


menu()
option =int(input("Enter your option: "))

running = True

while option != 2:
    if option == 1:

        file_source = 'E:\Download_movies/'
        file_destination = 'E:\Movies/'

        time.sleep(3)
        get_source = os.listdir(file_source)
        get_destination = os.listdir(file_destination)

        print("Source: ", get_source)
        print("Local: ", get_destination)




        for g in get_source:
            for x in get_destination:
                print(x)
            if g == x:
                print("Skipped!", g)
                pass
            else:
                time.sleep(3)
                shutil.move(file_source + g, file_destination)
                print('Moved:', g)

    elif option == 2:
        exit

    else:
        print("Invalid option.")