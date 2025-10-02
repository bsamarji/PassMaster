import json
import os
import sys


def load_data():
    """
    Load all data from the password vault. If a critical error occurs,
    it logs the error and exits the program gracefully.

    Returns:
        list: The loaded data.
    """
    vault = "./vault.json"

    # Check 1: File existence and size (still useful for expected scenarios)
    if not os.path.isfile(vault):
        print(
            f"Vault file '{vault}' not found. Creating empty vault..."
        )
        return []
    
    if os.stat(vault).st_size == 0:
        print(f"Vault file '{vault}' is empty. Continuing with empty vault.")
        return []

    # Check 2: Error handling for reading and JSON parsing
    try:
        with open(vault, "r") as f:
            data = json.load(f)

            # Critical check: Ensure the loaded data is actually a list
            if not isinstance(data, list):
                print(
                    f"CRITICAL ERROR: Data loaded from '{vault}' is not a list ({type(data).__name__})."
                )
                print("Exiting program to prevent potential data loss or corruption.")
                sys.exit(1)  # Exit with a non-zero status (1) to indicate failure
                
            return data

    except json.JSONDecodeError as e:
        # File is corrupt or invalid JSON
        print(
            f"CRITICAL ERROR: Vault file '{vault}' is corrupted or contains invalid JSON data."
        )
        print(f"Details: {e}")
        print("Exiting program to prevent potential data loss or corruption.")
        sys.exit(1)

    except IOError as e:
        # File permission issues or other file-related problems
        print(
            f"CRITICAL ERROR: Could not read from vault file '{vault}'. Check file permissions."
        )
        print(f"Details: {e}")
        sys.exit(1)

    except Exception as e:
        # Catch all other unexpected errors
        print(
            f"CRITICAL ERROR: An unexpected error occurred while loading data from '{vault}'."
        )
        print(f"Details: {e}")
        sys.exit(1)
