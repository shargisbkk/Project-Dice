import random

#Here's a comment from cecrumpton
def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def store_roll(rolls, store, indices):
    selected_rolls = [rolls[i] for i in indices]
    store.extend(selected_rolls)
    return store

def reroll(store, num_dice, num_sides):
    new_rolls = roll_dice(num_dice - len(store), num_sides)
    return new_rolls

store = []
num_dice = 8  # Set the number of dice to 8
num_sides = 6  # Set the number of sides on each die to 6

while True:
    command = input("Enter 'roll' to roll dice, 'reroll' to reroll, or 'exit' to exit: ")
    
    #roll command for initial dice roll
    if command == 'roll':
        rolls = roll_dice(num_dice, num_sides)
        print(f"Rolling {num_dice} dice with {num_sides} sides each:")
        print("Results:", rolls)
        indices = input("Enter the indices of the dice to store (e.g., '0 2' to store the first and third dice): ")
        indices = [int(i) for i in indices.split()]
        store = store_roll(rolls, store, indices)
        print("Total stored rolls:", store)
    
    #set rerolls to maximum 3
    elif command == 'reroll':
        new_rolls = reroll(store, num_dice, num_sides)
        print(f"Rerolling {num_dice - len(store)} dice with {num_sides} sides each:")
        print("Results:", new_rolls)
        indices = input("Enter the indices of the dice to store (e.g., '0 2' to store the first and third dice): ")
        indices = [int(i) for i in indices.split()]
        store = store_roll(new_rolls, store, indices)
        print("Total stored rolls:", store)
    
    #finalize all dice
    elif command == 'done':
        print("Final Score", store)

    elif command == 'exit':
        break
    
    else:
        print("Invalid command. Please try again.")
