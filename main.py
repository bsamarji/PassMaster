import argparse
import sys
from functions.load_data import load_data
from functions.save_data import save_data
from functions.find_entry import find_entry
from functions.add_entry import add_entry
from functions.display_entries import display_entries


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
        help="Find an entry/entries by searching on the entry name in the vault.",
    )
    parser.add_argument(
        "--list", action="store_true", help="Lists all the names of the entries stored in the vault."
    )

    args = parser.parse_args()

    print("\n========== PassMaster ==========\n")

    if args.add:
        print("Vault unlocked...")
        existing_data = load_data()
        data_to_save = add_entry(data=existing_data)
        save_data(entries=data_to_save)
        print("\nVault locked...")

    if args.find:
        print("Vault unlocked...")
        data = load_data()
        search_term = input(
            "\nWhat is the name of the entry you want to view?\n"
        ).strip()
        matches = find_entry(data=data, search_term=search_term)
        display_entries(entries=matches)
        print("\nVault locked...")

    if args.list:
        print("Vault unlocked...")
        print("Listing all entry names...")
        print("\nVault locked...")

    print("\n================================\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
