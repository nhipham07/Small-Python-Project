#TIC-TAC-TOE GAME (3x3)

import random
board = {"top-L": " ", "top-M": " ", "top-R": " ", "mid-L": " ", "mid-M": " ", "mid-R": " ", "low-L": " ", "low-M": " ", "low-R": " "}

def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])
    
computer_position = random.randint(1,9)
def convert_(computer_position):
    if computer_position == 1:
        computer_position = "top-L"
    elif computer_position == 2:
        computer_position = "top-M"
    elif computer_position == 3:
        computer_position = "top-R"
    elif computer_position == 4:
        computer_position = "mid-L"
    elif computer_position == 5:
        computer_position = "mid-M"
    elif computer_position == 6:
        computer_position = "mid-R"
    elif computer_position == 7:
        computer_position = "low-L"    
    elif computer_position == 8:
        computer_position = "low-M"
    else:
        computer_position = "low-R"
    return computer_position
   
def result_game(board):
    if board["top-L"] == board["top-M"] and board["top-L"] == board["top-R"] and board["top-L"] == "X":
        return "Congratulation, you win the game!!!"
    elif board["top-L"] == board["top-M"] and board["top-L"] == board["top-R"] and board["top-L"] == "O":
        return "Game over!!!"
    elif board["mid-L"] == board["mid-M"] and board["mid-L"] == board["mid-R"] and board["mid-L"] == "X":
        return "Congratulation, you win the game!!!"
    elif board["mid-L"] == board["mid-M"] and board["mid-L"] == board["mid-R"] and board["mid-L"] == "O":
        return "Game over!!!"
    elif board["low-L"] == board["low-M"] and board["low-L"] == board["low-R"] and board["low-L"] == "X":
        return "Congratulation, you win the game!!!"
    elif board["low-L"] == board["low-M"] and board["low-L"] == board["low-R"] and board["low-L"] == "O":
        return "Game over!!!"
    elif board["top-L"] == board["mid-M"] and board["top-L"] == board["low-R"] and board["top-L"] == "X":
        return "Congratulation, you win the game!!!"
    elif board["top-L"] == board["mid-M"] and board["top-L"] == board["low-R"] and board["top-L"] == "O":
        return "Game over!!!"
    elif board["low-L"] == board["mid-M"] and board["low-L"] == board["top-R"] and board["low-L"] == "X":
        return "Congratulation, you win the game!!!"
    elif board["low-L"] == board["mid-M"] and board["low-L"] == board["top-R"] and board["low-L"] == "O":
        return "Game over!!!"

print("Welcome to tic-tac-toe game (3x3).\nYou will be 'X' and the computer will be 'O'.\nGood luck!\n")   
while True: 
    # Ask the player moves
    while True:
        player_position = input("Move on which space?\n(top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R)\n")
        if board[player_position] == " ":
            board[player_position] = "X"
            break
        else:
            print("This position is out of space, please enter again")
    
    # Break the game when every space is fulfilled.
    if board["top-L"] != " " and board["top-M"] != " " and board["top-R"] != " " and board["mid-L"] != " " and board["mid-M"] != " " and board["mid-R"] != " " and board["low-L"] != " " and board["low-M"] != " " and board["low-R"] != " ":
        printBoard(board)
        result_game(board)
        print("End game")
        break
    
    # Computer move
    while True:
        if board[convert_(computer_position)] == " ":
            board[convert_(computer_position)] = "O"
            break
        else:
            computer_position = random.randint(1,9)
            convert_(computer_position)
      
    printBoard(board)
    
    # Result of the game
    result = result_game(board)
    if result == "Congratulation, you win the game!!!" or result == "Game over!!!":
        print(result)
        print("End game")
        break
    
        
    
    

