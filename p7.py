def display(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def heuristic(board):
    win = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == "X":
            return 2

        if board[a] == board[b] == board[c] == "O":
            return -2

    return 0


board = [" "] * 9
player = "X"

for turn in range(9):
    display(board)
    print("Player", player)

    while True:
        try:
            position = int(input("Enter position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Invalid position! Enter 1-9.")
            elif board[position] != " ":
                print("Position already occupied! Try again.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    board[position] = player

    score = heuristic(board)

    if score == 2:
        display(board)
        print("Player X wins!")
        break

    if score == -2:
        display(board)
        print("Player O wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    display(board)
    print("Game draw!")
