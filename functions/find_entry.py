def find_entry(data, entry_name):
    matching_entry = list(filter(lambda entry: entry["name"] == entry_name, data))
    return matching_entry