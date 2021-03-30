board = ["  " for i in range(9)]


def print_board():
  row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
  row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
  row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
  print()
  print(row1)
  print(row2)
  print(row3)
  print()


def player_move(icon):
  if icon == "X":
    number = 1
  elif icon == "0":
    number = 2
  print("Your turn player {}".format(number))
  choice = int(input("Make your choice(1-9): ").strip())
  if (choice > 9):
    print("Choice must be from 1 to 9")
  elif board[choice - 1] == "  ":
    board[choice - 1] = " {}".format(icon)
  else:
    print()
    print("That space is taken!")


def is_victory(icon):
  if (board[0] == " {}".format(icon) and board[1] == " {}".format(icon) and board[2] == " {}".format(icon)) or \
  (board[3] == " {}".format(icon) and board[4] == " {}".format(icon) and board[5] == " {}".format(icon)) or \
  (board[6] == " {}".format(icon) and board[7] == " {}".format(icon) and board[8] == " {}".format(icon)) or \
  (board[0] == " {}".format(icon) and board[3] == " {}".format(icon) and board[6] == " {}".format(icon)) or \
  (board[1] == " {}".format(icon) and board[4] == " {}".format(icon) and board[7] == " {}".format(icon)) or \
  (board[2] == " {}".format(icon) and board[5] == " {}".format(icon) and board[8] == " {}".format(icon)) or \
  (board[0] == " {}".format(icon) and board[4] == " {}".format(icon) and board[8] == " {}".format(icon)) or \
  (board[2] == " {}".format(icon) and board[4] == " {}".format(icon) and board[6] == " {}".format(icon)):
     return True
  else:
    return False

def is_draw():
  if "  " not in board:
    return True
  else:
    return False


def run_game():
  while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
      print("Congrats! X wins!")
      break
    elif is_draw():
      print("It's a draw!")
      break
    player_move("0")
    if is_victory("0"):
      print_board()
      print("Congrats! 0 wins!")
      break
    elif is_draw():
      print("It's a draw!")
      break