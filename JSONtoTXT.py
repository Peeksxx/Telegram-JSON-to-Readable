import json

# Load the JSON file
with open("result.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Prompt user for target user IDs
target_user_ids = []
while True:
    user_input = input("Enter a user ID or type 'done' to finish: ").strip()
    if user_input.lower() == "done":
        break
    target_user_ids.append(user_input)

# Open a text file in write mode to save messages
with open("filtered_messages.txt", "w", encoding="utf-8") as output_file:
    # Navigate to the messages list
    for chat in data["chats"]["list"]:
        for msg in chat["messages"]:
            if isinstance(msg, dict):  # Ensure it's a dictionary
                if msg.get("type") == "message" and "text" in msg:
                    # Check if the message is from one of the target users
                    if msg.get("from_id") in target_user_ids:
                        output_file.write(f"From {msg.get('from')}: {msg['text']}\n")

print("Filtered messages have been saved to filtered_messages.txt.")