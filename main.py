board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


print_board(board)

def quit(user_input):
    if user_input == "q":
        print("Thank you for playing!")
        return True
    else:
        return False

def check_input(user_input):
    # check if valid
    if not isValid(user_input):
        return False
    user_input = int(user_input)
    # check if 1-9
    return True


def isValid(user_input):
    if not user_input.isnumeric():
        print("Invalid!")
        return False
    else:
        return True

def inBounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This place does not exist! Try again.")

while True:

    user_input = input("Enter a position 1-9 or enter \"q\" to quit ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please re-enter a number 1-9.")
        continue