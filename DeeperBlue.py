 #Modules and subfiles used

import Piececlasses

from Printboard import *

from Pawn import possible_pawn_moves

import re

import random

import sys

import collections

from AN import conversions

import GA









#Board representations used to test and play the game

#main
position = [['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'white k bishop', 'white k knight', 'white k rook'], ['white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn'], ['black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']]

#checking for checkmate
#position = [['white q rook', 'white q knight', 'white q bishop', 'empty', 'white king', 'white k bishop', 'white k knight', 'white k rook'], ['white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'empty', 'white F pawn', 'white G pawn', 'white H pawn'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'black C pawn', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'white queen', 'empty'], ['black A pawn', 'black B pawn', 'empty', 'black D pawn', 'black E pawn', 'black F pawn', 'empty', 'black H pawn'], ['black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'empty', 'black k rook']]

#checking for stalemate
#position = [['empty', 'white king', 'empty', 'black q knight', 'empty', 'empty', 'empty', 'black k rook'], ['black q rook', 'empty', 'empty', 'black queen', 'black king', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']]

#scholar's mate
#position = [['white q rook', 'white q knight', 'white q bishop', 'empty', 'white king', 'empty', 'white k knight', 'white k rook'], ['white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'white k bishop', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'white queen'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn'], ['black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']]

#checking for check valid pawn promotions
#position = [['empty', 'white q knight', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black k bishop', 'white k rook', 'black H pawn', 'black king', 'empty', 'empty', 'empty', 'empty'], ['empty', 'white king', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'black C pawn', 'empty', 'empty', 'empty', 'empty', 'empty'], ['white A pawn', 'white B pawn', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']]

#opposite colored bishops
#position = [['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black k bishop', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['white k bishop', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']]

#rook and king vs. king endgame
#position = [['empty', 'white king', 'empty', 'empty', 'empty', 'empty', 'empty', 'black k rook'], ['empty', 'empty', 'empty', 'empty', 'black king', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']]

#checking for en passent
#position = [['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['white A pawn', 'empty', 'white C pawn', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['white k rook', 'black B pawn', 'empty', 'black D pawn', 'empty', 'empty', 'black king', 'empty'], ['white king', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']]

#checking for castling
#position = [['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'empty', 'empty', 'white k rook'], ['white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'empty', 'white F pawn', 'white G pawn', 'white H pawn'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'black queen'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn'], ['black q rook', 'black q knight', 'black q bishop', 'empty', 'black king', 'black k bishop', 'black k knight', 'black k rook']]

#testing the genetic algorithm
#position = [['empty', 'white q rook', 'empty', 'empty', 'empty', 'empty', 'black k rook', 'empty'], ['black queen', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'black king', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'black q rook', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['white k rook', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'white king']]



























#Data for determining king and knight moves

knight_moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [-2, 1], [-2, -1], [2, -1]]

king_moves = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]


#First turn initialization

turn = "white"

#turn = "black"


#Keeping track of the number of promoted pieces, known piece names, past moves and past positions (Used in determining draws)

promotion_number = 1

patterns = ['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'white k bishop', 'white k knight', 'white k rook', 'white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn', 'black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn', 'black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']

past_positions = {}

past_moves = []

past_inputs = []

last_moves = []

last_positions = []

#letter_to_number = {"a":






    

















































#General Funcitons used

def contents (file):

    s = set([])

    with open (file, "r") as f:

        for i in f.readlines ():

            s. add (eval (i. strip ()))

    return s

def filewrite (s, file):

    with open (file, "w") as f:

        for cont in s:

            newline = str (cont) + "\n"

            f.write (newline)

def reset_piececlasses ():

    list_of_pieces = []

    for i in position:

        for j in i:

            if not j == "empty":

                list_of_pieces.append (Piece (j))

def move_or_capture (ply, position, first):

    last_positions. append (tuple (tuple (x) for x in position))

    last_moves. append (ply)

    if len (ply) == 1 or len (ply) > 2:

        ply = ply [0]

    #before = position_of_piece (return_name (ply [0], patterns), position)

    before = first

    try:

        before.  append (1)

        before. pop ()

        before = letnum (before)

    except:

        pass

    after = ply [1]

    if re.search (r"capture", ply [0]):

        capture (ply, position)

        #print ("Capture: {a} from {b} to {c}". format (a = return_name (ply [0], patterns), b = before , c = letnum (after)))

    elif re.search (r"move", ply [0]):

        move (ply, position)

        #print ("Move: {a} from {b} to {c}". format (a = return_name (ply [0], patterns), b = before , c = letnum (after)))

def letnum (square):

    for i in conversions:

        if conversions [i] == square:

            return i

def before_after_convert (move, pos):

    l = []

    #try:

    first = move [:2]

    second = move [-2:]

    initial_position = conversions [first]

    final_position = conversions [second]

    #print (move)

    #print (current_valid_moves (turn, pos))

    for i in current_valid_moves (turn, pos):
        
        if position_of_piece (return_name (i [0], patterns), pos) == initial_position:

            if i [1] == final_position:

                l. append (i)

    return l

    #except:

    return []
                
    

    

def first_move_true (move):

    piece_name = return_name (move [0], patterns)

    has_not_moved = piecename_to_piececlass (piece_name)

    has_not_moved.first_move = True



def piecename_to_piececlass (piecename):

    for i in Piececlasses.list_of_pieces:

        if i.name == piecename:

            return i

def make_list (x, y):

    l = [x, y]

    return l

def copy_2D_list (List):

    foo = []

    for i in List:

        a = []

        for j in i:

            a. append (j)

        foo. append (a)

    return foo

def return_name (string, pat):

    for i in pat:

        if re.search (i, string):

            return i
    
def position_of_piece (piece, pos):

    for i in range (8):

        for j in range (8):

            if pos [i] [j] == piece:

                return [i ,j]

def piece_of_position (square, pos):

    return pos [square[0]] [square[1]]


def tuple_adding (a, b):

    w = a [0]
    x = a [1]

    y = b [0]
    z = b [1]

    return [w + y, x + z]

def square_in_position (square, po):

    if square[0] < 0 or square[1] < 0:

        return False
    
    try:

        po [square[0]] [square[1]]
        return True

    except:

        return False

def piece_in_position (piece, po):

    if l[0] < 0 or l[1] < 0:

        return False
    
    try:

        po [l[0]] [l[1]]
        return True

    except:

        return False

def change_turn ():

    global turn

    if turn == "white":

        turn = "black"

    elif turn == "black":

        turn = "white"

def insuf (white_pieces, black_pieces):

    if white_pieces == {"p": 0, "r": 0, "n": 0, "b": 0, "q": 0, "k": 1} and black_pieces == {"p": 0, "r": 0, "n": 0, "b": 0, "q": 0, "k": 1}:

        return True

    elif white_pieces == {"p": 0, "r": 0, "n": 0, "b": 1, "q": 0, "k": 1} and black_pieces == {"p": 0, "r": 0, "n": 0, "b": 0, "q": 0, "k": 1}:

        return True

    elif white_pieces == {"p": 0, "r": 0, "n": 0, "b": 0, "q": 0, "k": 1} and black_pieces == {"p": 0, "r": 0, "n": 0, "b": 1, "q": 0, "k": 1}:

        return True

    elif white_pieces == {"p": 0, "r": 0, "n": 1, "b": 0, "q": 0, "k": 1} and black_pieces == {"p": 0, "r": 0, "n": 0, "b": 0, "q": 0, "k": 1}:

        return True

    elif white_pieces == {"p": 0, "r": 0, "n": 0, "b": 0, "q": 0, "k": 1} and black_pieces == {"p": 0, "r": 0, "n": 1, "b": 0, "q": 0, "k": 1}:

        return True

    return False

def position_draws (past_positions):

    global past_moves

    if len (past_moves) >= 100:

        for i in range (len (past_moves) - 100, len (past_moves)):

            if re.search (r"capture", past_moves [i] [0]) or re.search (r"pawn", past_moves [i] [0]):

                return False

        print ("50 Moves With No Captures or Pawn Moves: draw")

        return True

    return False


    


"""def algebraic_conversion (move):

    if re.search (r"x", move):

    elif re.search (r"=", move):

    elif re.search (r"0-0", move) or re.search (r"0-0-0", move):

    elif re.search (r"""

                    
def win_or_draw (position, pasts):

    global turn

   #print (turn)

    #print (position)

    #print (current_valid_moves(turn, position))

    if current_valid_moves (turn, position) == []:

        GA.genetic ("checkmate", position, current_valid_moves (turn, position), turn, last_moves, promotion_number, patterns, last_positions)

        change_turn ()

        for i in current_valid_moves (turn, position):

            capture = i [0]

            king = i [1]

            if re.search (r"capture", capture) and re.search (r"king", piece_of_position (king, position)):

                #print ("Checkmate: {x} wins" .format (x = turn))

                #sys.exit()

                #return "game over"

                pass


        #print ("Stalemate: draw")

        #sys.exit()

        return "game over"

        

    if position_draws (pasts) == True:

        sys. exit ()

    white_pieces = {"p": 0, "r": 0, "n": 0, "b": 0, "q": 0, "k": 0}

    black_pieces = {"p": 0, "r": 0, "n": 0, "b": 0, "q": 0, "k": 0}

    for i in position:

        for j in i:

            if re.search (r"white", j):

                if re.search (r"bishop", j):

                    white_pieces ["b"] += 1

                elif re.search (r"knight", j):

                    white_pieces ["n"] += 1

                elif re.search (r"rook", j):

                    white_pieces ["r"] += 1

                elif re.search (r"queen", j):

                    white_pieces ["q"] += 1

                elif re.search (r"king", j):

                    white_pieces ["k"] += 1

                elif re.search (r"pawn", j):

                    white_pieces ["p"] += 1

            elif re.search (r"black", j):

                if re.search (r"bishop", j):

                    black_pieces ["b"] += 1

                elif re.search (r"knight", j):

                    black_pieces ["n"] += 1

                elif re.search (r"rook", j):

                    black_pieces ["r"] += 1

                elif re.search (r"queen", j):

                    black_pieces ["q"] += 1

                elif re.search (r"king", j):

                    black_pieces ["k"] += 1

                elif re.search (r"pawn", j):

                    black_pieces ["p"] += 1

    if insuf (white_pieces, black_pieces) == True:

        print ("Insufficient Material: draw")

        sys.exit()
        
    for i in pasts:

        if pasts [i] >= 3:

            print ("Threefold Repetition: draw")

            sys.exit()
        
    

                                                              

    


















































#Data to determine queen, bishop and rook moves. Data for king and knight is in the beggening of the document and data for the pawn is in Pawn.py

def possible_queen_moves (queen, po):

    l =[]

    for i in possible_rook_moves (queen, po):

        l. append (i)

    for i in possible_bishop_moves (queen, po):

        l. append (i)

    return l

def possible_rook_moves (rook, po):

    l = []

    vert_cord = position_of_piece (rook, po) [0]

    horz_cord = position_of_piece (rook, po) [1]

    for i in range (vert_cord + 1, 8):

        if po [i] [horz_cord] == "empty":

            l.append ([rook + " can move to", [i, horz_cord]])

        elif re.match (r"white", po [i] [horz_cord]) and re.match (r"black", rook):

            l.append ([rook + " can capture", [i, horz_cord]])

            break

        elif re.match (r"black", po [i] [horz_cord]) and re.match (r"white", rook):

            l.append ([rook + " can capture", [i, horz_cord]])

            break

        else:

            break

    for i in range (vert_cord - 1, -1, -1):

        if po [i] [horz_cord] == "empty":

            l.append ([rook + " can move to", [i, horz_cord]])

        elif re.match (r"white", po [i] [horz_cord]) and re.match (r"black", rook):
            
            l.append ([rook + " can capture", [i, horz_cord]])

            break

        elif re.match (r"black", po [i] [horz_cord]) and re.match (r"white", rook):

            l.append ([rook + " can capture", [i, horz_cord]])

            break

        else:

            break

    for i in range (horz_cord - 1, -1, -1):

        if po [vert_cord] [i] == "empty":

            l.append ([rook + " can move to", [vert_cord, i]])

        elif re.match (r"white", po [vert_cord] [i]) and re.match (r"black", rook):

            l.append ([rook + " can capture", [vert_cord, i]])

            break

        elif re.match (r"black", po [vert_cord] [i]) and re.match (r"white", rook):

            l.append ([rook + " can capture", [vert_cord, i]])

            break

        else:

            break

    for i in range (horz_cord + 1, 8):

        if po [vert_cord] [i] == "empty":

            l.append ([rook + " can move to", [vert_cord, i]])

        elif re.match (r"white", po [vert_cord] [i]) and re.match (r"black", rook):

            l.append ([rook + " can capture", [vert_cord, i]])

            break

        elif re.match (r"black", po [vert_cord] [i]) and re.match (r"white", rook):

            l.append ([rook + " can capture", [vert_cord, i]])

            break

        else:

            break

    return l

    

def possible_bishop_moves (bishop, po):

    l = []

    vert_cord = position_of_piece (bishop, po) [0]

    horz_cord = position_of_piece (bishop, po) [1]

    up_right_diagonal = []

    up_left_diagonal = []

    down_right_diagonal = []

    down_left_diagonal = []

    a = vert_cord

    b = horz_cord
    
    while a < 7 and b < 7:

        a += 1
        b += 1

        up_right_diagonal. append ([a, b])

    a = vert_cord

    b = horz_cord
    
    while a < 7 and b > 0:

        a += 1
        b -= 1

        up_left_diagonal. append ([a, b])

    a = vert_cord

    b = horz_cord
    
    while a > 0 and b < 7:

        a -= 1
        b += 1

        down_right_diagonal. append ([a, b])

    a = vert_cord

    b = horz_cord
    
    while a > 0 and b > 0:

        a -= 1
        b -= 1

        down_left_diagonal. append ([a, b])

    for i in up_right_diagonal:

        if po [i[0]] [i[1]] == "empty":

            l.append ([bishop + " can move to", [i[0], i[1]]])

        elif re.match (r"white", po [i[0]] [i[1]]) and re.match (r"black", bishop):

            l.append ([bishop + " can capture", [i[0], i[1]]])

            break

        elif re.match (r"black", po [i[0]] [i[1]]) and re.match (r"white", bishop):

            l.append ([bishop + " can capture", [i[0], i[1]]])

            break

        else:

            break

    for i in up_left_diagonal:

        if po [i[0]] [i[1]] == "empty":

            l.append ([bishop + " can move to", [i[0], i[1]]])

        elif re.match (r"white", po [i[0]] [i[1]]) and re.match (r"black", bishop):

            l.append ([bishop + " can capture", [i[0], i[1]]])

            break

        elif re.match (r"black", po [i[0]] [i[1]]) and re.match (r"white", bishop):

            l.append ([bishop + " can capture", [i[0], i[1]]])

            break

        else:

            break

    for i in down_right_diagonal:

        if po [i[0]] [i[1]] == "empty":

            l.append ([bishop + " can move to", [i[0], i[1]]])

        elif re.match (r"white", po [i[0]] [i[1]]) and re.match (r"black", bishop):

            l.append ([bishop + " can capture", [i[0], i[1]]])

            break

        elif re.match (r"black", po [i[0]] [i[1]]) and re.match (r"white", bishop):

            l.append ([bishop + " can capture", [i[0], i[1]]])

            break

        else:

            break

    for i in down_left_diagonal:

        if po [i[0]] [i[1]] == "empty":

            l.append ([bishop + " can move to", [i[0], i[1]]])

        elif re.match (r"white", po [i[0]] [i[1]]) and re.match (r"black", bishop):

            l.append ([bishop + " can capture", [i[0], i[1]]])

            break

        elif re.match (r"black", po [i[0]] [i[1]]) and re.match (r"white", bishop):

            l.append ([bishop + " can capture", [i[0], i[1]]])

            break

        else:

            break

    return l


















































#check_valid checks if a given move will put the king a position so that it can be caputred on the next move


def check_valid (move_or_capture, position):

    #print (move_or_capture)

    if re.search (r"move", move_or_capture [0]):

        temp_position = copy_2D_list (position)

        fake_move (move_or_capture, temp_position)

        #print_board (temp_position, row, column)

        if turn == "white":
    
            for i in temp_position:

                #print (move_or_capture)

                #print (temp_position)

                for j in i:

                    if re.match (r"black", j):

                        #print (j)

                        for k in valid_moves_of_piece (j, temp_position):

                            #print (k)

                            if re.search (r"capture", k [0]) and re.search (r"king", piece_of_position (k [1], temp_position)):

                                return False

        if turn == "black":
    
            for i in temp_position:

                for j in i:

                    if re.match (r"white", j):

                        for k in valid_moves_of_piece (j, temp_position):

                             if re.search (r"capture", k [0]) and re.search (r"king", piece_of_position (k [1], temp_position)):

                                return False

    if re.search (r"capture", move_or_capture [0]):

        temp_position = copy_2D_list (position)

        fake_capture (move_or_capture, temp_position)

        if turn == "white":
    
            for i in temp_position:

                for j in i:

                    if re.match (r"black", j):

                        for k in valid_moves_of_piece (j, temp_position):

                            if re.search (r"capture", k [0]) and re.search (r"king", piece_of_position (k [1], temp_position)):

                                 return False

        if turn == "black":
    
            for i in temp_position:

                for j in i:

                    if re.match (r"white", j):

                        for k in valid_moves_of_piece (j, temp_position):

                             if re.search (r"capture", k [0]) and re.search (r"king", piece_of_position (k [1], temp_position)):

                                 return False

    return True



#The move function allows for regular moves, castling and promotion. Fake_move does not alter a pieces first_move attribute and does not consider promotions and is only used in the check_valid function

def move (valid_move, pos):

    global turn

    past_moves. append (valid_move)

    #print (valid_move)

    if re.search (r"kingside castle", valid_move [0]):

        rook_square = [valid_move [1] [0], valid_move [1] [1] - 1]

        if re.search (r"white", valid_move [0]):

            rook_name = "white k rook can move to"

        elif re.search (r"black", valid_move [0]):

            rook_name = "black k rook can move to"

        move ([rook_name, rook_square], pos)

        move ([return_name (valid_move [0], patterns) + " can move to", valid_move [1]], pos)

    if re.search (r"queenside castle", valid_move [0]):

        rook_square = [valid_move [1] [0], valid_move [1] [1] + 1]

        if re.search (r"white", valid_move [0]):

            rook_name = "white q rook can move to"

        elif re.search (r"black", valid_move [0]):

            rook_name = "black q rook can move to"

        move ([rook_name, rook_square], pos)

        move ([return_name (valid_move [0], patterns) + " can move to", valid_move [1]], pos)

    if  re.search (r"promotion", valid_move [0]):

        global promotion_number

        if re.search (r"queen", valid_move [0]):

           inp = "queen"

        elif re.search (r"bishop", valid_move [0]):

           inp = "bishop"

        elif re.search (r"knight", valid_move [0]):

           inp = "knight"

        elif re.search (r"rook", valid_move [0]):

           inp = "rook"

        piece_name = return_name(valid_move [0], patterns)

        final_destination = valid_move [1]

        y = position_of_piece (piece_name, pos)

        pos [y[0]] [y[1]] = "empty"

        new_name = turn + " promoted " + inp + " " + str (promotion_number)

        #print (" The new piece is: " + new_name)

        pos [final_destination[0]] [final_destination[1]] =  new_name

        promotion_number += 1

        patterns.append (new_name)

        Piececlasses.list_of_pieces.append (Piececlasses.Piece (new_name))

    else:

        piece_name = return_name(valid_move [0], patterns)

        final_destination = valid_move [1]

        #print (pos)

        #print (valid_move)

        #print (piece_name)

        y = position_of_piece (piece_name, pos)

        pos [y[0]] [y[1]] = "empty"

        pos [final_destination[0]] [final_destination[1]] = piece_name

        has_not_moved = piecename_to_piececlass (piece_name)

        has_not_moved.first_move = False

def fake_move (valid_move, pos):

            #print (valid_move)
            
            #print(pos)

            piece_name = return_name(valid_move [0], patterns)

            final_destination = valid_move [1]

            #print (pos)

            #print (valid_move)

            #print (piece_name)

            y = position_of_piece (piece_name, pos)

            pos [y[0]] [y[1]] = "empty"

            pos [final_destination[0]] [final_destination[1]] = piece_name



#The capture function allows for regular captures, en passent and promotion. Fake_capture does not alter a pieces first_move attribute and does not consider promotions and is only used in the check_valid function
        

def capture (valid_capture, pos):

    global turn

    past_moves. append (valid_capture)

    if re.search (r"enpass", valid_capture [0]):

        piece_name = return_name(valid_capture [0], patterns)

        final_destination = valid_capture [1]

        y = position_of_piece (piece_name, pos)

        pos [y[0]] [y[1]] = "empty"

        if re.search (r"white", valid_capture [0]):

            pos [final_destination[0] + 1] [final_destination[1]] = piece_name

            pos [final_destination[0]] [final_destination[1]] = "empty"

        elif re.search (r"black", valid_capture [0]):

            pos [final_destination[0] - 1] [final_destination[1]] = piece_name

            pos [final_destination[0]] [final_destination[1]] = "empty"

    elif  re.search (r"promotion", valid_capture [0]):

        global promotion_number

        """inp = input ("Piece would you like to promote to: ")

        while not inp == "queen" and not inp == "bishop" and not inp == "knight" and not inp == "rook":

            print ("Invalid piece!")

            inp = input ("Piece would you like to promote to: ")"""

        if re.search (r"queen", valid_capture [0]):

           inp = "queen"

        elif re.search (r"bishop", valid_capture [0]):

           inp = "bishop"

        elif re.search (r"knight", valid_capture [0]):

           inp = "knight"

        elif re.search (r"rook", valid_capture [0]):

           inp = "rook"

        piece_name = return_name(valid_capture [0], patterns)

        final_destination = valid_capture [1]

        y = position_of_piece (piece_name, pos)

        pos [y[0]] [y[1]] = "empty"

        new_name = turn + " promoted " + inp + " " + str (promotion_number)

        #print (" The new piece is: " + new_name)

        pos [final_destination[0]] [final_destination[1]] =  new_name

        promotion_number += 1

        patterns.append (new_name)

        Piececlasses.list_of_pieces.append (Piececlasses.Piece (new_name))

    else:     

        piece_name = return_name(valid_capture [0], patterns)

        final_destination = valid_capture [1]

        #print (pos)

        #print (valid_move)

        #print (piece_name)

        y = position_of_piece (piece_name, pos)

        pos [y[0]] [y[1]] = "empty"

        pos [final_destination[0]] [final_destination[1]] = piece_name

        has_not_moved = piecename_to_piececlass (piece_name)

        #print ("yes")

        has_not_moved.first_move = False

def fake_capture (valid_capture, pos):

        if re.search (r"enpass", valid_capture [0]):

            piece_name = return_name(valid_capture [0], patterns)

            final_destination = valid_capture [1]

            y = position_of_piece (piece_name, pos)

            pos [y[0]] [y[1]] = "empty"

            if re.search (r"white", valid_capture [0]):

                pos [final_destination[0] + 1] [final_destination[1]] = piece_name

                pos [final_destination[0]] [final_destination[1]] = "empty"

            elif re.search (r"black", valid_capture [0]):

                pos [final_destination[0] - 1] [final_destination[1]] = piece_name

                pos [final_destination[0]] [final_destination[1]] = "empty"

        else:

            piece_name = return_name(valid_capture [0], patterns)

            final_destination = valid_capture [1]

            #print (pos)

            #print (valid_move)

            #print (piece_name)

            y = position_of_piece (piece_name, pos)

            pos [y[0]] [y[1]] = "empty"

            pos [final_destination[0]] [final_destination[1]] = piece_name
    


















































#valid_moves_of_piece returns the legal moves of a piece without checking if they are check_valid. Current_valid_moves returns a list of legal moves and also checks if they are check_valid

def valid_moves_of_piece (piece, pos):

    l =[]

    if re.search (r"king", piece):

        for i in king_moves:

            new_square = tuple_adding (position_of_piece (piece, pos), i)

            if square_in_position (new_square, pos) == True:

                if pos [new_square[0]] [new_square[1]] == "empty":

                    l.append ([piece + " can move to", new_square])

                elif re.match (r"white", piece) and re.match (r"black", pos [new_square[0]] [new_square[1]]) :

                    l.append ([piece + " can capture", new_square])

                elif re.match (r"black", piece) and re.match (r"white", pos [new_square[0]] [new_square[1]]) :

                    l.append ([piece + " can capture", new_square])

        if piecename_to_piececlass (piece). first_move == True:

            if re. search (r"white", piece):

                if piecename_to_piececlass ("white k rook"). first_move == True and pos [0] [5] == "empty" and pos [0] [6] == "empty":

                    temp = copy_2D_list (pos)

                    temp [0] [5] = "white king"

                    value = True

                    for i in temp:

                        for j in i:

                            for k in valid_moves_of_piece (j, temp):

                                if re.search (r"capture", k [0]) and re.search (r"king", temp [k [1] [0]] [k [1] [1]]):

                                    value = False

                    if value == True:

                        l. append (["kingside castle: " + piece + " can move to", [0, 6]])

                if piecename_to_piececlass ("white q rook"). first_move == True and pos [0] [1] == "empty" and pos [0] [2] == "empty" and pos [0] [3] == "empty":

                    temp = copy_2D_list (pos)

                    temp [0] [3] = "white king"

                    value = True

                    for i in temp:

                        for j in i:

                            for k in valid_moves_of_piece (j, temp):

                                if re.search (r"capture", k [0]) and re.search (r"king", temp [k [1] [0]] [k [1] [1]]):

                                    value = False

                    if value == True:

                        l. append (["queenside castle: " + piece + " can move to", [0, 2]])

            elif re. search (r"black", piece):

                 if piecename_to_piececlass ("black k rook"). first_move == True and pos [7] [5] == "empty" and pos [7] [6] == "empty":

                    temp = copy_2D_list (pos)

                    temp [7] [5] = "black king"

                    value = True

                    for i in temp:

                        for j in i:

                            for k in valid_moves_of_piece (j, temp):

                                if re.search (r"capture", k [0]) and re.search (r"king", temp [k [1] [0]] [k [1] [1]]):

                                    value = False

                    if value == True:

                        l. append (["kingside castle: " + piece + " can move to", [7, 6]])

                 if piecename_to_piececlass ("black q rook"). first_move == True and pos [7] [1] == "empty" and pos [7] [2] == "empty" and pos [7] [3] == "empty":

                    temp = copy_2D_list (pos)

                    temp [7] [3] = "black king"

                    value = True

                    for i in temp:

                        for j in i:

                            for k in valid_moves_of_piece (j, temp):

                                if re.search (r"capture", k [0]) and re.search (r"king", temp [k [1] [0]] [k [1] [1]]):

                                    value = False

                    if value == True:

                        l. append (["queenside castle: " + piece + " can move to", [7, 2]])

    if re.search (r"knight", piece):

        for i in knight_moves:

            new_square = tuple_adding (position_of_piece (piece, pos), i)

            if square_in_position (new_square, pos) == True:

                if pos [new_square[0]] [new_square[1]] == "empty":

                    l.append ([piece + " can move to", new_square])

                elif re.match (r"white", piece) and re.match (r"black", pos [new_square[0]] [new_square[1]]) :

                    l.append ([piece + " can capture", new_square])

                elif re.match (r"black", piece) and re.match (r"white", pos [new_square[0]] [new_square[1]]) :

                    l.append ([piece + " can capture", new_square])

    if re.search (r"rook", piece):

        for i in possible_rook_moves (piece, pos):

            l.append (i)

    if re.search (r"bishop", piece):

        for i in possible_bishop_moves (piece, pos):

            l.append (i)

    if re.search (r"queen", piece):

        for i in possible_rook_moves (piece, pos):

            l.append (i)

        for i in possible_bishop_moves (piece, pos):

            l.append (i)

    if re.search (r"pawn", piece):

        for i in possible_pawn_moves (piece, pos):

            l.append (i)

        if len (past_moves) >= 1:

            if re.search (r"pawn", past_moves [-1] [0]):

                if past_moves [-1] [1] [0] == 3 or past_moves [-1] [1] [0] ==4:

                    if position_of_piece (piece, pos) [0] == past_moves [-1] [1] [0]:

                        if position_of_piece (piece, pos) [1] + 1 == past_moves [-1] [1] [1] or position_of_piece (piece, pos) [1] - 1 == past_moves [-1] [1] [1]:

                            if (re.search (r"black", past_moves [-1] [0]) and re.search (r"white", piece)) or (re.search (r"white", past_moves [-1] [0]) and re.search (r"black", piece)):

                                l. append (["enpass: " + piece + " can capture", past_moves [-1] [1]])
 
    return l

def current_valid_moves (turn, po):

    List = []

    if turn == "white":
    
        for i in po:

            for j in i:

                if re.search (r"white", j):

                        for k in valid_moves_of_piece (j, po):

                            #print (check_valid(k))

                            if check_valid (k, po) == True:

                                List.append (k)

    if turn == "black":
    
        for i in po:

            for j in i:

                if re.search (r"black", j):

                    for k in valid_moves_of_piece (j, po):

                        if check_valid (k, po) == True:

                            List.append (k)

    return List


















































#make_random_move selects a random move from the list of moves and makes that move. Action is the current user-interface interaction function, which includes the options to allow the user to make a move,
#prompt the computer to make a random move, prompt the computer to make a sensible move, or print the program.

def make_random_move (t, p):

    List = current_valid_moves (t, p)

    x = List [random.randint (0, len (List) - 1)]

    piece_name = return_name (x [0], patterns)

    y = position_of_piece (piece_name, p)

    final_destination = x [1]

    if re.search (r"move", x [0]):

        move (x, p)

        print ("Move: {a} from {b} to {c}".format (a = piece_name, b = letnum (y), c = letnum (final_destination)))

        print ("")

        #print (p)

        print ("")

    if re.search (r"capture", x [0]):

        capture (x, p)

        print ("Capture: {a} from {b} to {c}".format (a = piece_name, b = letnum (y), c = letnum (final_destination)))

        print ("")

        #print (p)

        print ("")


def action (position):

    global turn

    print ("")

    print ("Options: ")

    print ("")

    print ("s: the computer makes a sensible move")

    print ("r: computer makes a random move")

    print ("m: user specifies a move")

    print ("q: the program terminates")

    print ("")

    user_input = input ("Your choice: ")

    #user_input = "r"

    while not  user_input == "r" and not  user_input == "m" and not  user_input == "q":

        print ("Invalid Command!")
    
        user_input = input ("Your choice: ")

    if user_input == "q":

        print ("End of program")

        sys.exit()

    elif user_input == "r":

        make_random_move (turn, position)

    elif user_input == "m":

        while True:

                try:

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

                        raise NameError ("Did not go through")

                    if action == "move":

                        moves = [piece_name + " can move to", final_destination]

                        valid_moves = current_valid_moves (turn, position)

                        if moves not in valid_moves:

                            raise NameError ("Did not go through")
                        
                        move (moves, position)

                        print ("Move: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                        print ("")

                        break

                    elif action == "capture":

                        captures = [piece_name + " can capture", final_destination]

                        valid_captures = current_valid_moves (turn, position)

                        if captures not in valid_captures:

                            raise NameError ("Did not go through")

                        capture (captures, position)

                        print ("Capture: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                        print ("")

                        break

                    elif action == "enpass":

                        if turn == "white":

                            final_destination = [final_destination [0] - 1, final_destination [1]]

                        elif turn == "black":

                            final_destination = [final_destination [0] + 1, final_destination [1]]

                        #print (final_destination)

                        captures = ["enpass: " + piece_name + " can capture", final_destination]

                        valid_captures = current_valid_moves (turn, position)

                        if captures not in valid_captures:

                            raise NameError ("Did not go through")

                        capture (captures, position)

                        print ("Capture: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                        print ("")

                        break

                    elif action == "queenside castle" or action == "kingside castle":

                        moves = [action + ": " + piece_name + " can move to", final_destination]

                        valid_moves = current_valid_moves (turn, position)

                        if moves not in valid_moves:

                            raise NameError ("Did not go through")

                        move (moves, position)

                        print ("Castle: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                        print ("")

                        break

                    elif action == "promotion":

                        inp = input ("Piece would you like to promote to: ")

                        while not inp == "queen" and not inp == "bishop" and not inp == "knight" and not inp == "rook":

                            print ("Invalid piece!")

                            inp = input ("Piece would you like to promote to: ")

                        promotion_1 = [inp + " promotion: " + piece_name + " can capture", final_destination]

                        promotion_2 = [inp + " promotion: " + piece_name + " can move to", final_destination]

                        valid_captures = current_valid_moves (turn, position)

                        if promotion_1 not in valid_captures and promotion_2 not in valid_captures:

                            raise NameError ("Did not go through")

                        if promotion_1 in valid_captures:

                            capture (promotion_1, position)

                            print ("Promotion: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                            print ("")

                        elif promotion_2 in valid_captures:

                            capture (promotion_2, position)

                            print ("Promotion: {a} from {b} to {c}".format (a = piece_name, b = y, c = final_destination))

                            print ("")

                        break

                    else:

                        raise NameError ("Did not go through")                    

                except:

                    print ("Please enter something valid!")

                    print ("")


def action2 (position):

    global turn

    global last_positions

    print ("")

    print ("Options: ")

    print ("")

    print ("g: the computer makes a genetic move")

    print ("l: the computer executes a genetic loop")

    print ("r: computer makes a random move")

    print ("m: user specifies a move")

    print ("q: the program terminates")

    print ("")

    user_input = input ("Your choice: ")

    #user_input = "r"

    while not  user_input == "r" and not  user_input == "m" and not  user_input == "q" and not user_input == "g":

        print ("Invalid Command!")
    
        user_input = input ("Your choice: ")

    past_inputs. append (user_input)

    if user_input == "q":

        print ("Write experience to file?")

        user_input = input ("Your choice: ")

        while not user_input == "yes" and not user_input == "no":

            print ("Invalid input!")

            user_input = input ("Your choice: ")

        if user_input == "yes":

            filewrite (GA.content, "Gamefile.txt")

        print ("End of program")

        sys.exit()

    elif user_input == "r":

        make_random_move (turn, position)

    elif user_input == "g":

        while True:

            inp = input ("Clear genetic database? ")

            if inp == "yes":

                last_move = "None" if past_moves == [] else past_moves [-1]

                GA.genetic ("clear", position, current_valid_moves (turn, position), turn, last_moves, promotion_number, patterns, last_positions)

                break

            elif inp == "no":

                break

            else:

                print ("Invalid Command!")

        last_move = "None" if past_moves == [] else past_moves [-1]

        return_ply = GA.genetic ("move", position, current_valid_moves (turn, position), turn, last_moves, promotion_number, patterns, last_positions)

        first = position_of_piece (return_name (return_ply [0], patterns), position)

        move_or_capture (return_ply, position, first)
        
    elif user_input == "m":

        while True:

                user_move = input ("Your move: ")

                converted = before_after_convert (user_move, position)

                if not converted == []:

                    break

                print ("Invalid Move!")

        if len (converted) > 1:

            inp = input ("Piece would you like to promote to: ")

            while not inp == "queen" and not inp == "bishop" and not inp == "knight" and not inp == "rook":

                print ("Invalid piece!")

                inp = input ("Piece would you like to promote to: ")

            for i in converted:

                if re.search (inp, i [0]):

                    converted = [i]

                    break

        move_or_capture (converted, position, user_move [:-2])

        if len (past_inputs) >= 2 and past_inputs [-2] == "g":

            last_move = "None" if past_moves == [] else past_moves [-1]

            GA.genetic ("opposite", position, current_valid_moves (turn, position), turn, last_moves, promotion_number, patterns, last_positions)
        
        








































#main2 combines the functions that print the current board position, check for wins and draws, enable for user-interaction, and change the current turn to create the main program.
#main1 (now defunct) mostly identical to the action function with code integrations that allow for turn changes, checks for checkmate, print the valid moves (in a crude fashion), and more.


def main2 (position):

    global past_positions

    global turn

    global last_positions
    
    """while True:

        pos = tuple (tuple (x) for x in position)

        print_board (position, column, row)

        #print (current_valid_moves (turn, position))

        if pos in past_positions:

            past_positions [pos] += 1

        else:

            past_positions [pos] = 1

        win_or_draw (position, past_positions)

        action2 (position)

        #print (gen ("test", position, current_valid_moves (turn, position), turn, past_moves [-1], promotion_number, patterns, past_positions))

        change_turn ()"""

    GA.content = contents ("Gamefile.txt")

    while True:

        while True:

            pos = tuple (tuple (x) for x in position)

            print_board (position, column, row)

            #print (current_valid_moves (turn, position))

            if pos in past_positions:

                past_positions [pos] += 1

            else:

                past_positions [pos] = 1

            value = win_or_draw (position, past_positions)

            if value == "game over":

                break

            action2 (position)

            #change_player ()

            change_turn ()

        #position = [['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'white k bishop', 'white k knight', 'white k rook'], ['white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn'], ['black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']]

        position = [['empty', 'white q rook', 'empty', 'empty', 'empty', 'empty', 'black k rook', 'empty'], ['black queen', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'black king', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'black q rook', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['white k rook', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'white king']]

        turn = "white"

        promotion_number = 1

        patterns = ['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'white k bishop', 'white k knight', 'white k rook', 'white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn', 'black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn', 'black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']

        past_positions = {}

        past_moves = []

        past_inputs = []

        last_positions = []

        last_moves = []

        Piececlasses.list_of_pieces = []

        previous_pieces = []

        for i in position:

            for j in i:

                if not j == "empty":

                    Piececlasses.list_of_pieces.append (Piececlasses.Piece (j))

    """except:

        print ("Write experience to file?")

        user_input = input ("Your choice: ")

        while not user_input == "yes" and not user_input == "no":

            print ("Invalid input!")

            user_input = input ("Your choice: ")

        if user_input == "yes":

            filewrite (GA.content, "Gamefile.txt")"""

"""def main1 ():

    global turn

    global position
        
    user_input = input ("Enter 'm' ro make your own move or enter 'r' for random, or 'q' for quit: ")

    print ("")

    while user_input != "q":

        ui = input ("Display current valid moves? ")

        if ui == "yes":

            print (current_valid_moves (turn, position))

        if user_input == 'r':

            #print ("Current Valid Moves: ")

            print ("")

            #print (possible_pawn_moves ("white A pawn", position))

            #print (current_valid_moves(turn, position))

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

                        promotion_1 = ["promotion: " + piece_name + " can capture", final_destination]

                        promotion_2 = ["promotion: " + piece_name + " can move to", final_destination]
                        
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



if __name__ == "__main__":

    main2 (position)

    
#make_random_move (turn, position)   
    
#print (valid_moves_of_piece ("white k bishop", position))
    
                    


            


