INPUT_STR = "652601"
INPUT_INT = int(INPUT_STR)  # to save time casting later
INPUT_LEN = len(INPUT_STR)  # to save time computing later

# create new recipe
def add(a, b):
    recipes = ""
    for new_recipe in str(int(a) + int(b)):
        recipes += new_recipe
    return recipes

# update the elf's current value
def update_current(c, board):
    return (c + 1 + int(board[c])) % len(board)


if __name__ == "__main__":
    # initialisation
    elf1 = 0
    elf2 = 1
    board = "37"

    # not optimal (takes about a minute to complete), but elegant
    while INPUT_STR not in board[-(INPUT_LEN + 1):]:
        # add new recipes to the board
        additions = add(board[elf1], board[elf2])
        board += additions
        # update elves' current values
        elf1 = update_current(elf1, board)
        elf2 = update_current(elf2, board)

    print("Answer #1:", board[INPUT_INT:INPUT_INT + 10])
    print("Answer #2:", board.index(INPUT_STR))
