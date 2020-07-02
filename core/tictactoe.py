# write your code here
import sys


def who_win(outputs, empties):
    winner = "Draw" if empties == [] else "continue"
    for i in range(3):
        if outputs[0][i] == outputs[1][i] == outputs[2][i]:
            if outputs[0][i] not in ("_", " "):
                winner = "Impossible" if outputs[0][i] != winner[0] and winner.endswith("wins") else outputs[0][
                                                                                                         i] + " wins"
        if outputs[i][0] == outputs[i][1] == outputs[i][2]:
            if outputs[i][0] not in ("_", " "):
                winner = "Impossible" if outputs[i][0] != winner[0] and winner.endswith("wins") else outputs[i][
                                                                                                         0] + " wins"
    if outputs[0][0] == outputs[1][1] == outputs[2][2]:
        if outputs[0][0] not in ("_", " "):
            winner = "Impossible" if outputs[0][0] != winner[0] and winner.endswith("wins") else outputs[1][1] + " wins"
    if outputs[0][2] == outputs[1][1] == outputs[2][0]:
        if outputs[1][1] not in ("_", " "):
            winner = "Impossible" if outputs[1][1] != winner[0] and winner.endswith("wins") else outputs[1][1] + " wins"
    return winner


def is_legal_step(step, empties):
    if step in ("\\q", "exit", "quit"):
        print("Quit the game, bye!")
        sys.exit(0)
    steps = step.split()
    try:
        digital_step = [int(x) for x in steps]
    except ValueError:
        print("You should enter numbers!")
        return is_legal_step(input("Enter the coordinates: >"), empties)
    else:
        is_legal = True
        for n in digital_step:
            if n <= 0 or n > 3:
                is_legal = False
        if is_legal:
            if digital_step in empties:
                return digital_step
            else:
                print("This cell is occupied! Choose another one!")
                return is_legal_step(input("Enter the coordinates: >"), empties)
        else:
            print("Coordinates should be from 1 to 3!")
            return is_legal_step(input("Enter the coordinates: >"), empties)


def after_move(matrix, step, is_X):
    ind = 0
    if step[1] == 3:
        ind = 0
    elif step[1] == 2:
        ind = 1
    elif step[1] == 1:
        ind = 2
    matrix[ind][step[0] - 1] = "X" if is_X else "O"
    return matrix


layouts = "         "  # input("Enter cells: > ")
# convert initial layouts to matrix
inputs = []
for i in range(0, len(layouts), 3):
    inputs.append([layouts[i], layouts[i + 1], layouts[i + 2]])
# calc initial matrix to get empty spaces matrix according to the coordinates user input
empty_spaces = []
vertical = 3
for rows in inputs:
    horizon = 1
    for columns in rows:
        if columns in (" ", "_"):
            empty_spaces.append([horizon, vertical])
        horizon += 1
    vertical -= 1

diver = "---------"
next_step_is_X = True
while True:
    print(diver)
    X_total = O_total = blank = 0
    for rows in inputs:
        line = ""
        for columns in rows:
            line += " " + columns
            if columns == "X":
                X_total += 1
            elif columns == "O":
                O_total += 1
            else:
                blank += 1
        print("|" + line + " |")
    print(diver)
    prompt = who_win(inputs, empty_spaces)
    if prompt == "Draw" or prompt.endswith("wins"):
        diver = prompt
        break
    next_step = is_legal_step(input("Enter the coordinates: > "), empty_spaces)
    inputs = after_move(inputs, next_step, next_step_is_X)
    empty_spaces.remove(next_step)
    next_step_is_X = False if next_step_is_X else True

print(diver)
