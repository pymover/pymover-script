import shutil
import time
import os
import datetime
import json
from discord_webhook import DiscordWebhook, DiscordEmbed

# Path to the configuration file
CONFIG_FILE = 'config.json'

def print_logo():
    """Displays an ASCII art logo."""
    logo_art = """
       ▄███████▄ ▄██   ▄     ▄▄▄▄███▄▄▄▄    ▄██████▄   ▄█    █▄     ▄████████    ▄████████ 
      ███    ███ ███   ██▄ ▄██▀▀▀███▀▀▀██▄ ███    ███ ███    ███   ███    ███   ███    ███ 
      ███    ███ ███▄▄▄███ ███   ███   ███ ███    ███ ███    ███   ███    █▀    ███    ███ 
      ███    ███ ▀▀▀▀▀▀███ ███   ███   ███ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
    ▀█████████▀  ▄██   ███ ███   ███   ███ ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
      ███        ███   ███ ███   ███   ███ ███    ███ ███    ███   ███    █▄  ▀███████████ 
      ███        ███   ███ ███   ███   ███ ███    ███ ███    ███   ███    ███   ███    ███ 
     ▄████▀       ▀█████▀   ▀█   ███   █▀   ▀██████▀   ▀██████▀    ██████████   ███    ███ 
    """
    print(logo_art)

def display_menu():
    """Displays the main menu options."""
    print("[1] Run File Mover")
    print("[2] Configure Paths")
    print("[3] Configure Discord Webhook")
    print("[4] Exit\n")

def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_config():
    """Loads the configuration from a file."""
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as config_file:
        return json.load(config_file)

def save_config(config):
    """Saves the configuration to a file."""
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file, indent=4)

def configure_paths():
    """Prompts the user to set the source and destination paths."""
    source_path = input("Enter the source folder path: ").strip()
    destination_path = input("Enter the destination folder path: ").strip()

    if not (os.path.exists(source_path) and os.path.exists(destination_path)):
        print("Error: One or both paths do not exist. Please try again.")
        return

    config = load_config()
    config["source"] = source_path
    config["destination"] = destination_path
    save_config(config)
    print("Paths have been successfully configured!")

def configure_webhook():
    """Prompts the user to set the Discord webhook URL."""
    webhook_url = input("Enter the Discord webhook URL: ").strip()

    if not webhook_url.startswith("https://"):
        print("Error: Invalid webhook URL. Please enter a valid URL.")
        return

    config = load_config()
    config["webhook"] = webhook_url
    save_config(config)
    print("Discord webhook URL has been successfully configured!")

def move_files_continuously(file_source, file_destination, webhook_url):
    """Continuously monitors and moves files from the source to the destination folder."""
    webhook = DiscordWebhook(url=webhook_url)
    print(f"Monitoring '{file_source}' for new files. Press Ctrl+C to stop.\n")
    try:
        while True:
            files_in_source = os.listdir(file_source)

            for file_name in files_in_source:
                source_file = os.path.join(file_source, file_name)
                destination_file = os.path.join(file_destination, file_name)

                if os.path.exists(destination_file):
                    print(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"), f"Skipped!: {file_name}")
                else:
                    shutil.move(source_file, destination_file)
                    print(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"), f"Moved: {file_name}")

                    # Send a Discord notification
                    embed = DiscordEmbed(color='000000')
                    embed.set_author(
                        name='Pymover',
                        url='https://github.com/MathiasKiwi',
                        icon_url='https://avatars.githubusercontent.com/u/107579533?s=200&v=4'
                    )
                    embed.add_embed_field(name='Moved File:', value=file_name)
                    embed.set_footer(text='Pymover')
                    embed.set_timestamp()

                    webhook.add_embed(embed)
                    webhook.execute()

            # Small delay to prevent excessive CPU usage
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopping file mover. Returning to the main menu.")

def main():
    """Main function to run the application."""
    print_logo()

    while True:
        display_menu()

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        clear_console()
        print_logo()

        if option == 1:
            config = load_config()
            if "source" not in config or "destination" not in config or "webhook" not in config:
                print("Error: Source, destination paths, or webhook URL are not configured. Please configure them first.")
                continue

            file_source = config["source"]
            file_destination = config["destination"]
            webhook_url = config["webhook"]
            move_files_continuously(file_source, file_destination, webhook_url)
        elif option == 2:
            configure_paths()
        elif option == 3:
            configure_webhook()
        elif option == 4:
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()