# random to choose x and o for players
import random
# to check if the correct format of position of token is entered or not
import re
# to get emoji we need emojize
import emoji
# to get a little big text using ASCII art
import pyfiglet
# getting to the main() function
def main():
    # everything inside infinite loop
    print_large_text("Welcome to\nTic Tac Toe")
    while True:
        # getting the name of players
        player_1 = input("Enter the name of Player 1: ")
        player_2 = input("Enter the name of Player 2: ")
        print()
        # assigning x and o to the players
        token_1 = random.choice(['X', 'O'])
        if token_1 == 'X':
            token_2 = 'O'
        else: 
            token_2 = 'X'
        # Tell players with what token have to play with
        print(f"{player_1} will play with {token_1}")
        print(f"{player_2} will play with {token_2}")
        print()
        # creating an grid of 3x3 empty hopefullly!!
        grid = [["", "", ""], ["", "", ""], ["", "", ""]]
        # ask players where they want to put their token 
        flag, key = 1, None # to make a while loop flag will be zero as soon as the game ends and we get out of the while loop, key is set to None which will be checked for draw later in program
        turns = 0 # if the game is going to be a draw we need ot exit at 4.5 turns after both players had 4 turns we need to have the first player have a turn not the second one cause no more squares ofcc!!
        while flag == 1: # until the game ends
            while True:
                turns += 1 
                position_1 = input(f"{player_1} where do you want to put {token_1}? ").strip() # checking the right format is entered or not
                if re.fullmatch(r"[1-3]{1}x[1-3]{1}", position_1): # checking their position and splitting it
                    row_1, col_1 = map(int, position_1.split("x")) # storing the position and mapping
                    row_1, col_1 = row_1 - 1, col_1 - 1
                    if grid[row_1][col_1] == "": # checking if the spot choosen is empty or not
                        grid[row_1][col_1] = token_1
                    else:
                        print("Position already taken! Try again.")
                        continue
                    break # exiting infinite loop
                else:
                    print("Invaid position syntax, type position in matrix-address format")
                    continue # prompting again 
            # printing board to show the move player 1 played
            print_board(grid)
            # checking if the player has won or not
            flag, key = check_result(grid, flag, key)
            # if player has won we need to get out of while loop using flag
            if flag == 0: break
            # doing same for player_2
            while True:
                if turns == 5 and all(box != "" for row in grid for box in row): # accesing whole grid and checking if all elements al filled or not and turns == 5
                    flag = 0 
                    break # to avoid the second player play first
                position_2 = input(f"{player_2} where do you want to put {token_2}? ").strip()
                if re.fullmatch(r"[1-3]{1}x[1-3]{1}", position_2): 
                    row_2, col_2 = map(int, position_2.split("x")) 
                    row_2, col_2 = row_2 - 1, col_2 - 1
                    if grid[row_2][col_2] == "": 
                        grid[row_2][col_2] = token_2
                    else:
                        print("Position already taken! Try again.")
                        continue
                    break
                else:
                    print("Invaid position syntax, type position in matrix-address format")
                    continue
            print_board(grid)
            flag, key = check_result(grid, flag, key)
        # outside while loop trying to print the result as game is over and then breaking out of the first infinite loop
        print_result(key, token_1, token_2, player_1, player_2)
        break
    

def print_board(grid):
    i = 0
    print()
    for row in grid:
        i += 1
        print(" | ".join(row)) # joins rows by ' | '
        while i != 3: 
            print("-" * 9)  # Adds a separator between rows
            break
    print()


# now we try to check if there is any winner or not every condition will have a return statement at the end to exit and prevent the other statements from running
def check_result(grid, flag, key):
    # first we try to check it row by row
    for i in range(3):
        if grid[i][0] != "" and grid[i][0] == grid[i][1] == grid[i][2]: # the elements should be empty and equal at the same time
            key = grid[i][0] # using key to store the token of winner so that we can identify by token who won
            flag = 0
            return (flag, key)
        else:
            continue
    # now we check verically in a column
    for i in range(3):
        if grid[0][i] != "" and grid[0][i] == grid[1][i] == grid[2][i]:
            key = grid[0][i]
            flag = 0
            return (flag, key)
        else:
            continue
    # now we check in diagonal (both diagonals) we don't need any loop here
    if grid[0][0] == grid[1][1] == grid[2][2] != "": # they should be equal and not equal to empty 
        key = grid[0][0]
        flag = 0
        return (flag, key)
    elif grid[0][2] == grid[1][1] == grid[2][0] != "":
        key = grid[0][2]
        flag = 0
        return (flag, key)
    # now checking if it's a draw
    if all(box != "" for row in grid for box in row) and flag == 0:
        key = None
    return (flag, key)


def print_result(key, token_1, token_2, player_1, player_2):
    # printing results with emojis
    win_emoji = emoji.emojize("🎉🎊🥳🔥👑")
    if key == token_1:
        print_large_text("Voila")
        print(f"Congratuations, {player_1} playing with {token_1} you are the winner{win_emoji}!!")
    elif key == token_2:
        print_large_text("Voila")
        print(f"Congratuations, {player_2} playing with {token_2} you are the winner{win_emoji}!!")
    elif key == None:
        draw_emoji = emoji.emojize("🤝 😐 ⚖️")
        print(f"It's a draw{draw_emoji}!!!")


def print_large_text(text): # taken through AI
    ascii_art = pyfiglet.figlet_format(text, font = 'slant') # figlet_format takes input as a normal text and makes it's ASCII art
    print(ascii_art)


if __name__ == "__main__":
    main()