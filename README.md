![banner](https://i.imgur.com/5boDwK0.png)
# pymover-script

## What is pymover?
Pymover is a Python-based file management tool that monitors a specific directory for new files, moves them to a destination folder, and sends updates via a Discord webhook. It also includes real-time logging of file operations to keep you informed about the status of each action.

# Features

## Menu System
A simple and intuitive menu with the following options:
Run the script: Start the file monitoring and moving process.
Adjust settings: (Not implemented yet).
Exit: Close the application.

(GIF: Navigating the menu and selecting “Run.”)

## File Monitoring and Management
Continuously monitors the specified source directory for new files.
Automatically moves new files to the destination directory.
Skips files that already exist in the destination folder.

(GIF: Watching a new file appear in the source folder and being moved to the destination.)

## Console Logging

Logs the status of each file operation (e.g., skipped or moved) with a timestamp for real-time updates.

(GIF: Console output showing timestamps and file statuses as files are moved.)

## Discord Webhook Integration

Sends notifications to a Discord channel whenever a file is moved. Each message includes:
	•	The name of the moved file.
	•	A timestamp.
	•	A custom embed with author and footer details.

(GIF: A Discord channel receiving notifications as files are moved.)

# How It Works

## Setup

Replace the following placeholders in the script with your specific details:
enter-file-source-path: Path to the folder you want to monitor.
enter-file-destination-path: Path to the folder where files should be moved.
discord-webhook-link: Your Discord webhook URL.

## Execution

Run the script and select the desired option from the menu. Files will be monitored and moved in real-time, with logs displayed in the console and notifications sent to Discord.

## Customization

The script is flexible and can be tailored to suit your specific file management needs or extended with additional features.

## Usage:
More information coming soon!
