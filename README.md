![banner](https://i.imgur.com/5boDwK0.png)
# pymover-script

## What is pymover?
Pymover is a file management tool that monitors a specific directory for new files, moves them to a destination folder, and sends updates via a Discord webhook. And real-time logging of file operations. Below is a breakdown of its features:

## Features
	1.	Menu System
Simple and intuitive menu with options to:
	•	Run the script.
	•	Adjust settings (not implemented yet).
	•	Exit.
(GIF: Navigating the menu and selecting “Run.”)
	3.	File Monitoring and Management
	•	Continuously monitors the specified source directory for new files.
	•	Automatically moves new files to the destination directory.
	•	Skips files that already exist in the destination folder.
(GIF: Watching a new file appear in the source folder and being moved to the destination.)
	4.	Console Logging
Logs the status of each file operation (e.g., skipped or moved) with a timestamp.
(GIF: Console output showing timestamps and file statuses as files are moved.)
	5.	Discord Webhook Integration
Sends notifications to a Discord channel whenever a file is moved. The message includes:
	•	The name of the moved file.
	•	A timestamp.
	•	A custom embed with author and footer details.
(GIF: A Discord channel receiving notifications as files are moved.)

## How It Works
	1.	Setup
Replace the following placeholders with your specific paths and webhook URL:
	•	enter-file-source-path (source directory).
	•	enter-file-destination-path (destination directory).
	•	discord-webhook-link (Discord webhook URL).
	2.	Execution
Run the script and select the desired option from the menu.
Files are processed in real-time, with updates logged to the console and sent to Discord.
	3.	Customization
The script can be modified to fit different file management needs or expanded with additional menu options.


## Usage:
More information coming soon!
