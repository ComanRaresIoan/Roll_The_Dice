import random

def parse_input(input_string): # has the role to define the faces of the dice
    if input_string in {'1', '2', '3', '4', '5', '6'}: # # set of values
        return int(input_string)
    else:
        print("Enter a number from 1 to 6: ")
        raise SystemExit(1) # it raises error otherwise

num_dice_input = input("How many dice do you want to roll? [1-6]: ") # number of dices that user chooses to roll

num_dice = parse_input(num_dice_input) # We call the function parse_input

def roll_dice(num_dice): # has the role to define the number of dices to roll
    roll_results = [] # we store the values of the dices in a list
    for _ in range(num_dice):  # we define a for loop to iterare through each dice
        roll = random.randint(1, 6) # we generate pseudo random integer from 1 to 6
        roll_results.append(roll) # we add the roll of the dice to the results list
    return roll_results # we exit the function using the return instruction

roll_results = roll_dice(num_dice) # we call the function roll_dice to roll the dice a certain number of times

DICE_ART = { # We define the dictionary with the faces of the dices to make it look better
    1: (
        "┌─────────┐", # The corresponding face for 1
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐", # The corresponding face for 2
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐", # The corresponding face for 3
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐", # The corresponding face for 4
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐", # The corresponding face for 5
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐", # The corresponding face for 6
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DICE_HEIGHT = len(DICE_ART[1]) # we define the height of the dice as being the length of the first column
DICE_WIDTH = len(DICE_ART[1][0]) # we define the width of the dice as being the length of the first row
DICE_FACE_SEPARATOR = " " # we define the space separator of the dices to not make the dice face overlap

def generate_dice_faces_diagram(dice_values): # has the role of assigning the diagram face to the integer
    dice_faces = [] # we store the faces in a list
    for value in dice_values: # we iterate in each dice value to see what values we meet
        dice_faces.append(DICE_ART[value]) # we dd the value to the dice faces list

    dice_faces_rows = [] # we store the faces rows in a list

    for row_idx in range(DICE_HEIGHT): # we iterate in the dice height with the row index
        row_components = [] # we define the row components as a list
        for dice in dice_faces: # we define a for loop to iterate in the dice faces
            row_components.append(dice[row_idx]) # we add the row index of the dice in the row components list
        row_string = DICE_FACE_SEPARATOR.join(row_components) # add the dice separator to remove the overlap of dice margins
        dice_faces_rows.append(row_string) # we add the row string to the dice_faces_rows list

    width = len(dice_faces_rows[0]) # we assign the length of the dice values of the row to be the width
    diagram_header = "RESULTS".center(width, "~") # we create a header of the results and we center it

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows) # we create the final diagram using the heder and the rows
    return dice_faces_diagram # we exit the function the diagrams

dice_face_diagram = generate_dice_faces_diagram(roll_results) # we call the function to generate the dice faces
print(f"\n{dice_face_diagram}") # We print the final results
