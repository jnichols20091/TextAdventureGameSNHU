def show_instructions():
    print("Welcome to the Haunted Themepark game!")
    print("The instructions are simple: ")
    print("You must collect all of the items in the park in order to defeat the final boss.")
    print("You must type North, East, South, or West to move in that direction.")
    print("You must type Exit to exit the game.")
    print("Good luck!")

rooms = {
    'Fame-Street USA': {'West': 'Main gate', 'South': 'Mini-Town', 'North': 'Dangerous Fog',
                        'East': 'Edison-World'},
    'Main gate': {'East': 'Fame-Street USA', 'Item': 'Flashlight'},
    'Mini-Town': {'North': 'Fame-Street USA', 'East': 'Adventureland', 'Item': 'Gas mask'},
    'Adventureland': {'North': 'Edison-World', 'West': 'Mini-Town', 'Item': 'Key to Castle'},
    'Edison-World': {'North': 'Frontierland', 'West': 'Fame-Street USA', 'South': 'Adventureland',
                     'Item': 'Armor'},
    'Frontierland': {'North': 'The Castle', 'West': 'Critter Country', 'South': 'Edison-world',
                     'Item': 'Medical kit'},
    'Critter country': {'East':'Frontierland', 'Item': 'Gun'},
    'The Castle': {'Villian': 'The Shadow Person', 'South': 'Frontierland'},
    'Dangerous Fog': {'South': 'Fame-Street USA'}
}


def main():

    show_instructions()
    current_room = 'Fame-Street USA'
    command = 'None'
    inventory = []
    # while loop to keep the game going until the player wins or quits
    while command != 'Exit':
        print()
        print('You are here: ', current_room)
        print("Inventory:", inventory)
        room_dict = rooms[current_room]
        if "Item" in room_dict:
            item = room_dict["Item"]
            if item not in inventory:
                print("You see a", item)
                user_input = input("Enter 'Collect *item name*: ")
                if user_input == "Collect " + item:
                    print(item, "collected")
                    inventory.append(item)
                else:
                    print("Invalid entry")
                continue
        # if the player has all the items, they win
        if "Villian" in room_dict:
            if "Key to Castle" in inventory:
                print("You have defeated the", room_dict["Villian"])
                print("Congratulations! You have won the game!")
                break
            else:
                print("You must collect the Key to Castle to defeat the", room_dict["Villian"])
        command = input('Enter a direction or Exit game: ')
        if command == 'Exit':
            current_room = 'Exit'
            print('Thanks for playing!')
        elif command in room_dict:
            current_room = room_dict[command]
        else:
            print('You cannot go that way!')
main()
