import json
import sys


def save_data(entries):
    """
    Save entries to the password vault with error handling.

    Args:
        entries (list of dictionaries): The data to save, typically a list of dictionaries,
            each containing a name, username, password, website and note.

    Returns:
        bool: True if the save was successful, False otherwise.
    """
    vault = "./vault.json"

    try:
        # Attempt to open the file and write the JSON data
        with open(vault, "w") as f:
            json.dump(entries, f, indent=4)  # Added indent for readability

    except IOError as e:
        # Handle file-related errors (e.g., permissions, disk space, file not writable)
        print(f"Error: Could not write to file {vault}. Details: {e}")
        sys.exit(1)

    except TypeError as e:
        # Handle errors if the 'entries' object cannot be serialized to JSON
        print(f"Error: Data provided is not JSON serializable. Details: {e}")
        sys.exit(1)

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred during save. Details: {e}")
        sys.exit(1)

    # If the code reaches this point, the save was successful
    print("Entry successfully saved to vault!")
    print("Locking vault...")
    sys.exit(0)
