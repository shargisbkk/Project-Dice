import random

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def force_store(new_rolls, store):
    store.extend(new_rolls)
    return store

def store_roll(rolls, store, indices):
    selected_rolls = [rolls[i] for i in indices]
    store.extend(selected_rolls)
    return store

def reroll(store, num_dice, num_sides, reroll_count):
    new_rolls = roll_dice(num_dice - len(store), num_sides)
    return new_rolls, reroll_count + 1

store = []
num_dice = 7  # Set the number of dice to 7
num_sides = 6  # Set the number of sides on each die to 6
reroll_count = 0  # Set initial count to 0
roll_used = False  # Track if the roll command had been used

while True:
    command = input("Enter 'roll' to roll dice, 'reroll' to reroll, 'done' to finalize, or 'exit' to exit: ")

    if command == 'roll' and not roll_used:
        roll_used = True
        rolls = roll_dice(num_dice, num_sides)
        print(f"Rolling {num_dice} dice with {num_sides} sides each:")
        print("Results:", rolls)
        indices = input("Enter the indices of the dice to store (e.g., '0 2' to store the first and third dice): ")
        indices = [int(i) for i in indices.split()]
        store = store_roll(rolls, store, indices)
        print("Total stored rolls:", store)

    elif command == 'reroll':
        new_rolls, reroll_count = reroll(store, num_dice, num_sides, reroll_count)
        print(f"Rerolling {num_dice - len(store)} dice with {num_sides} sides each:")
        print("Results:", new_rolls)
        
        if reroll_count == 2:
            print("Take 'em or Leave 'em!")
            store = force_store(new_rolls, store)  # Store all dice rolls
        else:
            indices = input("Enter the indices of the dice to store (e.g., '0 2' to store the first and third dice): ")
            indices = [int(i) for i in indices.split()]
            store = store_roll(new_rolls, store, indices) # Store indicated dice rolls
        
        print("Total stored rolls:", store)

    elif command == 'done':
        print("Final Score", store)

    elif command == 'exit':
        break

    else:
        print("Invalid command. Please try again.")
