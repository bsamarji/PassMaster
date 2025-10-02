import sys


def add_entry(data):
    """
    Collects user input for a new entry, validates name, username, and password,
    and appends it to the data list. Exits gracefully on critical errors.

    Args:
        data (list): The list of existing entry dictionaries.

    Returns:
        list: The updated list of entries, or the original data if cancelled.
    """
    new_entry = {}

    # Define fields that must not be empty
    required_fields = ["name", "username", "password"]

    # --- 1. Robust Input Collection and Validation for Required Fields ---

    for field in required_fields:
        # Standardize the prompt for better readability
        prompt = f"\nWhat is the {field} you want to store?\n"
        if field == "name":
            prompt = "\nWhat do you want to name the new entry?\n"

        while True:
            # Use a try-block to handle potential input errors (like CTRL+D/EOF)
            try:
                value = input(prompt).strip()
            except EOFError:
                print("\n\nInput cancelled (EOF detected). Returning without changes.")
                return data  # Return the original data without changes
            except Exception as e:
                # Catch unexpected input errors
                print(f"\nCRITICAL ERROR during input for {field}: {e}")
                sys.exit(1)

            if value:
                new_entry[field] = value
                break  # Exit the validation loop once a valid value is entered
            else:
                print(
                    f"Error: The '{field}' field cannot be empty. Please enter a value."
                )

    # --- 2. Optional Input Collection (No mandatory validation) ---

    # No loop needed, as empty input is acceptable.
    new_entry["website"] = (
        input("\nWhat website is the username and password for? (Optional)\n").strip()
        or None
    )
    new_entry["notes"] = (
        input("\nDo you have any notes for this entry? (Optional)\n").strip() or None
    )

    # --- 3. Appending Data with Critical Error Handling ---

    try:
        # Check if 'data' is a list before appending
        if not isinstance(data, list):
            print(
                f"\nCRITICAL ERROR: Data structure passed to add_entry is not a list ({type(data).__name__})."
            )
            sys.exit(1)

        data.append(new_entry)
        print(f"\nEntry '{new_entry['name']}' successfully added.")

    except Exception as e:
        # Catch any unexpected errors during the append operation
        print(
            f"\nCRITICAL ERROR: Failed to append new entry to data list. Details: {e}"
        )
        sys.exit(1)

    return data
