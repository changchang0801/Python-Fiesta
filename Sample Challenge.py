import random

user_input=[' ']*10
# X = " "
# O = " "
player_1 = " "
player_2 = " "
placement = " "

# creating the board using print statement
def creating_board(user_input):
    print "   " + user_input[7] + "|" + user_input[8] + "|" + user_input[9]
    print "------------"
    print "   " + user_input[4] + "|" + user_input[5] + "|" + user_input[6]
    print "------------"
    print "   " + user_input[1] + "|" + user_input[2] + "|"+ user_input[3]

def player_selection():
    random_player = random.randint(0,1)
    if random_player == 0:
        player_1 = "X"
    else:
        player_2 = "O"

def placement_on_the_board():
    player_1= int(input("player_1, where do you want to place your move ?" ))
    player_2= int(input("player_2, where do you want to place your move ?" ))
    user_input[player_1]= "X"
    user_input[player_2]= "O"

def board_checker(user_input):
    if ' ' in user_input[1:]:
        print "what's your next move ? "
    elif ((user_input[1] !=" " and user_input[2] != "" and user_input [3] != "")or
        (user_input[4] != " " and user_input[5] != "" and user_input[6] != "") or
        (user_input[7] != " " and user_input[8] != "" and user_input[9] != "") or
        (user_input[1] != " " and user_input[4] != "" and user_input[7] != "") or
        (user_input[2] != " " and user_input[5] != "" and user_input[8] != "") or
        (user_input[3] != " " and user_input[6] != "" and user_input[9] != "") or
        (user_input[3] != " " and user_input[5] != "" and user_input[7] != "") or
        (user_input[1] != " " and user_input[5] != "" and user_input[9] != "")):

        print "You win !"
    else:
        print "board is full, rematch ? "

def check_space_availability(user_input):
    while user_input[player_1] != ' ' or user_input[player_2]!= ' ':
        print "The spot is not available"
        print  creating_board(user_input)


def show_the_board():
    print creating_board(user_input)


creating_board(user_input)
player_selection()
placement_on_the_board()
board_checker(user_input)
show_the_board()
placement_on_the_board()
board_checker(user_input)
show_the_board()
placement_on_the_board()
board_checker(user_input)
show_the_board()
placement_on_the_board()
board_checker(user_input)
show_the_board()
placement_on_the_board()
board_checker(user_input)
placement_on_the_board()
board_checker(user_input)
show_the_board()           