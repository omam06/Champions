from ticket import create_ticket
from storage import load_ticket, save_ticket
from ai_suggestions import get_ai_suggestion

def main():
    loaded_tickets = load_ticket()
    while True:
        print()
        print("=======Campus Ticket Creator=======")
        print("1. Create ticket")
        print("2. Get AI suggestions")
        print("3. Exit")
        choice = input("Enter an option: ").strip()

        if choice == "1":
            title = input("Enter title: ").strip()
            description = input("Enter a detailed description: ").strip()
            priority = input("Enter priority(Low/Medium/High/Critical): ").strip().title()
            try:
                new_ticket = create_ticket(loaded_tickets, title, description, priority)
                loaded_tickets.append(new_ticket)
                save_ticket(loaded_tickets)
                print(f"Ticket {new_ticket['id']} created and saved successfully")
            except ValueError as e:
                print(f"Ticket creation failed! {e}")

        elif choice == "2":
            id = input("Enter ticket ID: ").strip().upper()
            print("Getting AI suggestions.........\n")
        
            found_ticket = False
            for any_ticket in loaded_tickets:
                if any_ticket["id"] == id:
                    found_ticket = True

                    description = any_ticket["Description"]

                    try:
                        suggestions = get_ai_suggestion(description)
                        print(suggestions)
                    except Exception as e:
                        print(f"Sorry, it failed; {e}")
                    break
            print("--------------Done------------------")
            if not found_ticket:
                print("Ticket not found.")


        elif choice == "3":
            print("Thank you for using Campus Ticket creation. Goodbye.")
            break
        
        else:
            print("Invalid Option. Try again.")

if __name__ == "__main__":
    main()


