
# Welcome to the JSON to TXT Tool!

This tool aids in helping you turn your gobbledygook telegram JSON backup into something readable in a TXT file format!

**NOTE: This program saves ALL of *YOUR* messages from ALL of your chats.** You may need to scroll down to the very bottom of the output file and delete all messages after the point in which you and the other person convorsate. It should look like the following: <br />
> From you: afga <br />
> From them: asfhg <br />
> From them: hdfsdfh <br />
> From you: sdeff <br />
> `from this point on, your chat and the other person ends.` <br />
> From you: asdcasfas <br />
> From you: asfwhr <br />
> From you: asgwhs <br />
> From you: awgfwsd <br />
> From you: eswdhgshd <br />

Here are the features of this program as of 3-11-2025:

- Able to input what messages to save from who

# Requirements?

- Have [python 3](https://www.python.org/downloads/) installed. You can check if you already do by executing `python --version` in your command prompt. If it returns with a version, you have it. If it gives you an error, you don't!
  > Remember to check the box "Install to PATH" during installation, or this won't work!
- This program has only been tested on Windows 10/11 machines.

# How to run?

1. Save your telegram data! Do this by navigating to the following in the desktop app:
> `Navigate to Telegram Desktop` --> `Go to your Telegram settings` --> `Press on the "Advanced" tab` --> `Scroll down till you see "Export Telegram Data" and click on it` --> `Make sure you check the box to download "Machine-readable JSON"` --> `Export it!`
2. Gather the UserIDs of the people you'd like to save the messages from. If it's just for you and one other person's chat, then copy their UserID and your UserID. 
> UserIDs can be found in the JSON code saved by telegram.  Your UserID should look like the following: `"User0123456789"`. You can put these into a temporary text file for now. <br />
>  ![Image](https://github.com/user-attachments/assets/ae24b9ee-4b32-47f4-8edb-a2acfa6b1823) <br />
>  **Useful tip:** You can load the .json file into your the Windows Note Pad app and press `ctrl+f` to show the find prompt. Then, simply type in your Telegram name to find messages sent by you!
3. Create a folder containing the following files: <br />
	> result.json (The file containing telegram message data) <br />
	> JSONtoTXT.py (Python file downloaded from this repository) <br />
4. Open a Command Prompt by right-clicking inside of the folder and selecting "Open in Terminal".
	> **Note:** If that doesn't work, simply open the command prompt via Windows Search and type in the following command: `cd \path\of\your\folder\`.
5. Once you have a terminal open in your folder's directory, double check the result file is named **exactly** "result.json". Finally, run the Python code by typing in the following command: `python '.\JSONtoTXT.py'`.
	> **Note:** When pasting in the UserIDs to your command prompt, make sure you use `ctrl+shift+v` instead of the conventional `ctrl+v`.
6. All done! It should now have the new save file as `filtered_messages.txt`.

# File Cleanup
If there are empty spaces or messages that just look like code, please refer to Notepad++'s replace feature to get rid of the imperfections.

**Questions? DM me @peeksxx on Telegram!**
