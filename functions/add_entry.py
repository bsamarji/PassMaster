def add_entry(data):
    new_entry = {}
    new_entry["name"] = input("\nWhat do you want to name the new entry?\n").strip()
    new_entry["username"] = input("\nWhat is the username you want to store?\n").strip()
    new_entry["password"] = input("\nWhat is the password you want to store?\n").strip()
    new_entry["website"] = input("\nWhat website is the username and password for?\n").strip() or None
    new_entry["notes"] = input("\nDo you have any notes for this entry?\n").strip() or None
    data.append(new_entry)
    return data