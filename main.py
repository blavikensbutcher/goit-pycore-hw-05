from typing import Dict

from colorama import Fore, Back

from decorators import input_error

type Contacts = Dict[str, str]


@input_error
def show_contacts(contacts: Contacts) -> str:
    return ", \n".join(f"{name}: {phone}" for name, phone in contacts.items())


@input_error
def show_number(contacts: Contacts, name: str) -> str:
    return contacts[name]


@input_error
def change_contact(args, contacts: Contacts) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


@input_error
def parse_input(user_input: str):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts: Contacts) -> str:
    name, phone = args
    capitalized = name.capitalize()
    contacts[capitalized] = phone
    return "Contact added."


def main():
    contacts: Contacts = {}
    print(Fore.CYAN + "Welcome to the assistant bot!")
    try:
        while True:
            user_input = input(Fore.GREEN + "Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(Fore.WHITE + Back.BLACK + "Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "all":
                print(show_contacts(contacts))
            elif command == "phone":
                print(Fore.BLUE + show_number(contacts, args[0]))
            else:
                print(Fore.RED + "Invalid command.")
    except KeyboardInterrupt:
        print("\n" + Fore.WHITE + Back.BLACK + "Good bye!")
        exit()


if __name__ == "__main__":
    main()
