![banner](https://i.imgur.com/5boDwK0.png)
# pymover-script

## What is pymover?
Pymover is a Python-based file management tool that monitors a specific directory for new files, moves them to a destination folder, and sends updates via a Discord webhook. It also logs file operations in real time to keep you informed about the status of each action.

# Features

## Menu System
A simple and intuitive menu with the following options:
Run the script: Start the file monitoring and moving process.
Adjust settings: (Not implemented yet).
Exit: Close the application.

## File Monitoring and Management
Continuously monitors the specified source directory for new files.
Automatically moves new files to the destination directory.
Skips files that already exist in the destination folder.

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
Enter-file-source-path: Path to the folder you want to monitor.
Enter-file-destination-path: Path to the folder where files should be moved.
Discord-webhook-link: Your Discord webhook URL.

## Execution

Run the script and select the desired option from the menu. Files will be monitored and moved in real-time, with logs displayed in the console and notifications sent to Discord.

## Customization

The script is flexible and can be tailored to suit your file management needs or extended with additional features.

## Context
Pymover is a side project. I'm making this script for my use case and thought maybe someone else wanted to use it, too :)
