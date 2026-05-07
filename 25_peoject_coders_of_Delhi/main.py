import json

# Let's write a function to Load the data.
def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

data = load_data("massive_data.json")

print(data)

type(data)

# Write a funtion to display users and connections

def display_users(data):
    print("Users and their connections:\n")
    for user in data['users']:
        print(f"ID: {user['id']} - {user['name']} friends connections with: {user['friends']} and liked pages are {user['liked_pages']}")
    print("\nPages Information")
    for page in data['pages']:
        print(f"{page['id']} {page['name']}")
display_users(data)