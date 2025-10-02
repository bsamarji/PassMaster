from tabulate import tabulate 

def display_entries(entries):
    """
    Prints a list of entry dictionaries in a clean, professional columnar format.
    """
    if not entries:
        print("No matching entries found.")
        return
        
    # --- Data Preparation ---
    
    # 1. Determine all unique keys (column headers)
    headers = set()
    for entry in entries:
        headers.update(entry.keys())
    
    # Sort and prioritize key columns
    priority_keys = ["name", "username", "password", "website", "notes"]
    sorted_headers = priority_keys + sorted([h for h in headers if h not in priority_keys])
    
    # 2. Format the data rows
    table_data = []
    for entry in entries:
        row = []
        for header in sorted_headers:
            value = entry.get(header, "NULL") # Use 'NULL' for missing values
            row.append(value)

        table_data.append(row)

    # --- Print Output ---

    print("\n**SEARCH RESULTS**")
    print(tabulate(table_data, headers=sorted_headers, tablefmt="simple"))
