def add_entry(data):
    new_entry = {}
    new_entry["name"] = input("What do you want to name the new entry?\n").strip()
    new_entry["username"] = input("What is the username you want to store?\n").strip()
    new_entry["password"] = input("What is the password you want to store?\n").strip()
    new_entry["website"] = input("What website is the username and password for?\n").strip() or None
    new_entry["notes"] = input("Do you have any notes for this entry?\n").strip() or None
    data.append(new_entry)
    return data