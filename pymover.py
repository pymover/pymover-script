import shutil
import time
import os
import datetime
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from tqdm import tqdm

CONFIG_FILE = 'config.json'


def print_logo():
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


def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as config_file:
        return json.load(config_file)


def save_config(config):
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file, indent=4)


def configure_paths():
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
    webhook_url = input("Enter the Discord webhook URL: ").strip()
    if not webhook_url.startswith("https://"):
        print("Error: Invalid webhook URL. Please enter a valid URL.")
        return
    config = load_config()
    config["webhook"] = webhook_url
    save_config(config)
    print("Discord webhook URL has been successfully configured!")


def move_files(file_source, file_destination, webhook_url):
    """Monitors and moves files from the source to the destination folder."""
    webhook = DiscordWebhook(url=webhook_url)
    move_log = []  # Stores log entries for display

    try:
        while True:
            # Clear only the "Monitoring" line (preserves move log)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_logo()
            print("Monitoring '{}' for new files. Press Ctrl+C to stop.\n".format(file_source))

            # Display the log
            for log_entry in move_log:
                print(log_entry)

            files_in_source = os.listdir(file_source)

            if not files_in_source:
                print("\nNo files found. Waiting...\n")
                time.sleep(5)
                continue

            print(f"\nFound {len(files_in_source)} file(s) to move. Starting transfer...\n")

            # Use tqdm to show the progress bar for file movement
            for file_name in tqdm(files_in_source, desc="Moving Files", unit="file"):
                source_file = os.path.join(file_source, file_name)
                destination_file = os.path.join(file_destination, file_name)

                if os.path.exists(destination_file):
                    log_entry = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]") + f" Skipped: {file_name}"
                    move_log.append(log_entry)
                else:
                    # Move the file
                    shutil.move(source_file, destination_file)
                    log_entry = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]") + f" Moved: {file_name}"
                    move_log.append(log_entry)

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

            # Limit the log size to the last 50 entries
            if len(move_log) > 50:
                move_log = move_log[-50:]

            # Small delay after processing all files
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nGracefully exiting... No files are being moved anymore.")
        return


def main():
    print_logo()

    while True:
        print("[1] Run File Mover")
        print("[2] Configure Paths")
        print("[3] Configure Discord Webhook")
        print("[4] Exit\n")

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if option == 1:
            config = load_config()
            if "source" not in config or "destination" not in config or "webhook" not in config:
                print("Error: Source, destination paths, or webhook URL are not configured. Please configure them first.")
                continue

            file_source = config["source"]
            file_destination = config["destination"]
            webhook_url = config["webhook"]

            move_files(file_source, file_destination, webhook_url)
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