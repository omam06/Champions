from datetime import datetime
valid_priorities = ["Low", "Medium", "High", "Critical"]


def next_ticket_id(ticket_list):
    highest_id = 0
    for each_ticket in ticket_list:
        ticket_id = each_ticket["id"]
        numeric_part = int(ticket_id[1:])
        if numeric_part > highest_id:
            highest_id = numeric_part
    next_id = highest_id + 1
    return f"T{next_id:03d}"
    

def create_ticket(ticket_list, title, description, priority):
    if title == "":
        raise ValueError("Title MUST not be blank")
    if not description:
        raise ValueError("Description MUST be detailed")
    if priority not in valid_priorities:
        raise ValueError("Enter a valid priority from the options.")

    ticket_id = next_ticket_id(ticket_list)

    return {
        "id": ticket_id,
        "Title": title,
        "Description": description,
        "Priority": priority,
        "Status": "open",
        "created at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }