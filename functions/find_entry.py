import sys

def find_entry(data, search_term):
    """
    Finds entries in a list of dictionaries where the 'name' key contains the search_term. 
    Exits gracefully if data is corrupted.
    
    Args:
        data (list): A list of dictionaries.
        search_term (str): The term to search for within the 'name' field.
    
    Returns:
        list: A list of all matching entry dictionaries.
    """
    
    # We will search case-insensitively for a better user experience
    search_term_lower = search_term.lower()
    matching_entries = []

    if len(search_term) == 0:
        print("Search term cannot be empty, please try again by running the --find command.\n")
        sys.exit(0)
    
    for entry in data:
        try:
            # Check 1: Ensure it's a valid dictionary with a 'name' key
            entry_name = entry.get("name")
            
            if isinstance(entry, dict) and entry_name:
                # Check 2: Substring match (case-insensitive)
                if search_term_lower in entry_name.lower():
                    matching_entries.append(entry)
                
        except Exception as e:
            # CRITICAL ERROR: An item in the data list is corrupt
            print(f"CRITICAL ERROR: Data list contains a corrupted entry during search.")
            print(f"Details: {e}")
            sys.exit(1) # Exit immediately due to corrupted state
            
    # Success: Return the list of 0 or more matching entries
    return matching_entries