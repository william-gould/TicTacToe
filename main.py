board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
# vars

user = True #true = x, false = o.
turns = 0

# Methods

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
    if not inBounds(user_input):
        return False
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
        return False
    else:
        return True


def isTaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("You can't go here!")
        return True
    else:
        return False


def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "x"
    else:
        return"o"

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
        return False


def check_col(user, board):
    complete_col = True
    for col in range(3):
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
        else:
            return False


def check_diag(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


def isWin(user, board):
    if check_row(user,board):
        return True
    if check_col(user,board):
        return True
    if check_diag(user,board):
        return True

# game while loop

while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Enter a position 1-9 or enter \"q\" to quit ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please re-enter a number 1-9.")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if isTaken(coords, board):
        print("Please pick another position")
        continue
    add_to_board(coords, board, active_user)

    if isWin(active_user, board):
        print_board(board)
        print(f"{active_user} won!")

    turns += 1
    if turns == 9:
        print("Draw!")
    user = not user
