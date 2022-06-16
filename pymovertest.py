import shutil
import time
import os

menu_options = {
    1: 'Run',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def logo():
    print(""" ________  ___    ___ _____ ______   ________  ___      ___ _______   ________     
|\   __  \|\  \  /  /|\   _ \  _   \|\   __  \|\  \    /  /|\  ___ \ |\   __  \    
\ \  \|\  \ \  \/  / | \  \\\__\ \  \ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \   
 \ \   ____\ \    / / \ \  \\|__| \  \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\  
  \ \  \___|\/  /  /   \ \  \    \ \  \ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \| 
   \ \__\ __/  / /      \ \__\    \ \__\ \_______\ \__/ /     \ \_______\ \__\\ _\ 
    \|__||\___/ /        \|__|     \|__|\|_______|\|__|/       \|_______|\|__|\|__|
         \|___|/                                                                   \n""")

logo()

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    file_source = 'E:\MoviesSource/'
    file_destination = 'E:\Movies/'
    
    path_to_watch = file_source

    time.sleep(1)
    get_source = os.listdir(file_source)
    get_destination = os.listdir(file_destination)

    print("Source: ", get_source)
    print("Local: ", get_destination)

    for g in get_source:
        if os.path.exists(file_destination+g):
            print("Skipped!", g)
        else:
            time.sleep(3)
            shutil.move(file_source + g, file_destination)
            print('Moved:', g)
    print("---------------------------")

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ""
        try:
            option = input('Enter one of the options above: ')
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == "1":
           option1()
        elif option == "2":
            option2()
        elif option == "3":
            option3()
        elif option == "4":
            print('Thanks for using pymover :D')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')