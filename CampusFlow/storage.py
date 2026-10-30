import json
import os

FILENAME = "tickets.json"

def load_ticket():
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return "Failed to load tickets, file is corrupt."

def save_ticket(ticket_list):
    try:
        with open(FILENAME, "w") as file:
            json.dump(ticket_list, file, indent=4)
    except Exception as e:
        return f"Failed to save ticket: {e}"

