import argparse
import os
from functions.load_data import load_data
from functions.save_data import save_data
from functions.find_entry import find_entry
from functions.add_entry import add_entry

def main():
    parser = argparse.ArgumentParser(
        description="PassMaster: A secure password manager CLI application"
    )
    parser.add_argument(
        "--add",
        action="store_true",
        help="Add new entry to be saved in the vault.",
    )
    parser.add_argument(
        "--find",
        action="store_true",
        help="Find an entry by searching on the entry name in the vault.",
    )
    parser.add_argument(
        "--list", action="store_true", help="Lists all entries stored in the vault."
    )
    parser.add_argument("--quit", action="store_true", help="Quit PassMaster.")

    args = parser.parse_args()

    if args.add:
        existing_data = load_data()
        data_to_save = add_entry(data=existing_data)
        successful_save = save_data(entries=data_to_save)
        if successful_save is True:
            print("Vault locked...")


    if args.find:
        data = load_data()
        entry_name = input("What is the name of the entry you want to view?\n").strip()
        matching_entry = find_entry(data=data, entry_name=entry_name)
        print(matching_entry)
        

    if args.list:
        print("Listing all entry names...")

    if args.quit:
        print("Quitting PassMaster\nVault locked...")


if __name__ == "__main__":
    main()
