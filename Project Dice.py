import random

# Defined functions for multiple call
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

def enemy_roll(num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(9)]
    return rolls

def store_enemy(rolls, enemy_store):
    enemy_store.extend(rolls)
    return enemy_store

# Game Constants
store = [] # Store the player rolls
enemy_store = [] # Store the npc roll
num_dice = 7  # Set the number of dice to 7
num_sides = 6  # Set the number of sides on each die to 6
reroll_count = 0  # Set initial count to 0
roll_used = False  # Track if the roll command had been used
player_health = 50 # Set player health to 50
enemy_health = 50 # Set npc health to 50

# Game loop
while True:
    command = input("Enter 'roll', 'reroll', 'fight', or 'exit': ")

    # Player commands
    if command == 'roll' and not roll_used:
        roll_used = True
        rolls = roll_dice(num_dice, num_sides)
        print(f"Rolling {num_dice} dice with {num_sides} sides each:")
        print("Results:", rolls)
        indices = input("Enter which you shall keep: (i.e '0 3' to store the 1st and 4th)")
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
            indices = input("Enter which you shall keep: (i.e '0 3' to store the 1st and 4th)")
            indices = [int(i) for i in indices.split()]
            store = store_roll(new_rolls, store, indices) # Store indicated dice rolls
        
        print("Total stored rolls:", store)

    elif command == 'fight':
        rolls = enemy_roll(num_sides)
        print (f"Rolling 9 dice with {num_sides} sides each:")
        print ("Results:", rolls)
        enemy_store = store_enemy(rolls, enemy_store)
        player_total = sum(store)
        enemy_total = sum(enemy_store)
        print ("Player's Power:", player_total, "Devil's Power:", enemy_total)

        # Compare player to enemy and determine game state
        if player_total > enemy_total:
            damage_enemy = player_total - enemy_total
            enemy_health = enemy_health - damage_enemy
            print ("Dealt damage:", damage_enemy, "Total enemy health", enemy_health)
            if enemy_health <= 0:
                print("JACKPOT!")
                break
            else:
                print("LUCK'S RUNNING HOT!")
  
        
        else:
            damage_player = enemy_total - player_total
            player_health = player_health - damage_player
            print ("Damage recieved:", damage_player, "Remaining HP:", player_health)
            if player_health <= 0:
                print("THE STAKES WERE TOO HIGH, GAMBINO!")
                break
            else:
                print("DON'T FOLD YET!")
        
        # Reset all parameters after fight command
        roll_used = False
        reroll_count = 0
        store = []
        enemy_store = []


    elif command == 'exit':
        print("See you later, Gambino...")
        break

    else:
        print("Can't let you do that, Gambino...")
