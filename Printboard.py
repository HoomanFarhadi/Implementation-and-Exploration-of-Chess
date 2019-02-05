# -*- coding: utf-8 -*-
import re

#from colorama import init, Fore

#init (convert = True)

#position = [q, e, q, e, e, e, q, q, e]

#box = " __________\n|           |\n|           |\n|           |\n|           |\n|           |\n|___________|"

#pawn = "    __\n   /  \\\n   \__/\n   |  |\n   |  |\n  /    \\\n /      \\\n/________\ "

symbols = {"wk": "♔", "wr": "♖", "wn": "♘", "wb": "♗", "wq": "♕","wp": "♙", "bk": "♚", "br": "♜", "bn": "♞", "bb": "♝", "bq": "♛","bp": "♟", "ee": " ."}

column = " a  b  c  d  e  f  g  h"

row = [8,7,6,5,4,3,2,1]

def decor (f):

    def wrap (a, b, c):

        print ("--------------------------------------------------------------------------------------------------------------------------------")

        f (a, b, c)

        print ("--------------------------------------------------------------------------------------------------------------------------------")

    return wrap

def return_piece (piece):

    if re.search (r"queen", piece):

        return "q"
    
    if re.search (r"pawn", piece):

        return "p"
    
    if re.search (r"knight", piece):

        return "n"
    
    if re.search (r"king", piece):

        return "k"
    
    if re.search (r"bishop", piece):

        return "b"
    
    if re.search (r"rook", piece):

        return "r"

    if re.search (r"empty", piece):

        return "e"
    
    
def return_color (piece):

    if re.search (r"white", piece):

        return "w"
    
    if re.search (r"black", piece):

        return "b"

    if re.search (r"empty", piece):

        return "e"
    
@decor
def print_board (position, column, row):

    print (column)

    linear_list = []

    for i in reversed (position):

        for j in i:

           color = return_color (j)

           piece = return_piece (j)

           symbol = color + piece

           linear_list. append (symbols [symbol])

           

   # print (linear_list)

    for k in range (8):

        num = row [k]

        string = ""

        for l in range (8):

            string += linear_list [(8 * k) + l]

        print (str (num) + string + str (num))

    print (column)

            




    
"""user_input = input ("Enter 'm' ro make your own move or enter 'r' for random, or 'q' for quit: ")

print ("")

while user_input != "q":

    ui = input ("Display current valid moves? ")

    if ui == "yes":

        print (current_valid_moves (turn, position))

    if current_valid_moves (turn, position) == []:

        print ("{x} just got checkmated". format (x = turn))

        print ("")

        sys.exit()

    if user_input == 'r':

        #print ("Current Valid Moves: ")

        print ("")

        #print (possible_pawn_moves ("white A pawn", position))

        print (current_valid_moves(turn, position))

        print ("")

        make_random_move (turn, position)

        if turn == "white":

            turn = "black"

        elif turn == "black":

            turn = "white"

    elif user_input == "m":

        while True:

            try:

                #print (current_valid_moves(turn, position))

                piece_name = return_name (input ("Enter piece name: "), patterns)

                print ("")
                    
                y = position_of_piece (piece_name, position)

                final_destination_1 = int(input("Enter the final destination 1st-cordinate: "))

                print ("")

                final_destination_2 = int(input("Enter the final destination 2nd-cordinate: "))

                print ("")

                action = input ("Enter desired action: ")

                final_destination = make_list (final_destination_1, final_destination_2)


                if position_of_piece (piece_name, position) == None:

                    #print ("yes")

                    raise NameError ("Did not go through")

                if action == "move":

                    moves = [piece_name + " can move to", final_destination]

                    valid_moves = current_valid_moves (turn, position)

                    #print (valid_moves)

                    if moves not in valid_moves:

                        #print ("yes 2")

                        raise NameError ("Did not go through")

                        #print (final_destination)

                        #print (y)

                    move (moves, position)

                    print ("Move: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                    print ("")

                    if turn == "white":

                        turn = "black"

                    elif turn == "black":
            
                        turn = "white"

                    break

                elif action == "capture":

                    captures = [piece_name + " can capture", final_destination]

                    valid_captures = current_valid_moves (turn, position)

                    if captures not in valid_captures:

                        raise NameError ("Did not go through")

                    capture (captures, position)

                    print ("Capture: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                    print ("")

                    if turn == "white":

                        turn = "black"

                    elif turn == "black":
            
                        turn = "white"

                    break

                elif action == "promotion":

                    promotion_1 = ["Promotion: " + piece_name + " can capture", final_destination]

                    promotion_2 = ["Promotion: " + piece_name + " can move to", final_destination]
                        
                    valid_captures = current_valid_moves (turn, position)

                    if promotion_1 not in valid_captures and promotion_2 not in valid_captures:

                        print (valid_captures)

                        #print ("error 1")

                        raise NameError ("Did not go through")

                    if promotion_1 in valid_captures:


                        capture (promotion_1, position, promotion_number)

                        print ("Promotion: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                        print ("")

                    elif promotion_2 in valid_captures:

                        capture (promotion_2, position)

                        print ("Promotion: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                        print ("")

                    if turn == "white":

                        turn = "black"

                    elif turn == "black":
            
                        turn = "white"

                    break

                else:


                    raise NameError ("Did not go through")                    

            except:

                print ("Please enter something valid!")

                print ("")
                

    else:

        print ("Please enter a valid command!")

        print ("")

    print_board (position, column, row)

    user_input = input ("Enter 'm' to make your own move or enter 'r' for random, or 'q' for quit: ")

    print ("")"""
         

            

            
           

                




    




       

 
