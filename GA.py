import re

from collections import Counter

def tuple_convert (l):

    if len (l) == 8:

        return tuple (tuple (x) for x in l)

    elif len (l) == 2:

        return (l [0], tuple (l [1]))

def list_convert (l):

    a = []

    for i in l:

        if i == "black" or i == "white" or i == "checkmate" or re.search (r"move", i) or re.search (r"capture", i):

            a .append (i)

        else:

            a. append (list (list (x) for x in i))

    return a

def set_refine (l):

    for i in Counter (tuple_convert (l)):

        for j in range (1, Counter (tuple_convert (l)) [i]):

            l. remove (list_convert (i))

def change_turn (l):

    if l [-1] == "black":

        l [-1] = "white"

    elif l [-1] == "white":

        l [-1] = "black"

def temp_list_1 (previous_list, new_pos, checkmate):

    previous_list. insert (-1, new_pos)

    previous_list. append (checkmate)

    return previous_list

def temp_list_2 (previous_list, new_pos):

    l = []

    for i in previous_list:

        l. append (i)

    l. append (new_pos)

    return l

def copy_list (List):

    foo = []

    for i in List:

        if i == "checkmate" or i == "black" or i == "white":

            foo.append (i)

        else:

            a = []

            for j in i:

                a. append (j)

            foo. append (a)

    return foo

def position_of_piece (piece, pos):

    for i in range (8):

        for j in range (8):

            if pos [i] [j] == piece:

                return [i ,j]

def return_name (string, pat):

    for i in pat:

        if re.search (i, string):

            return i

def reverse_move_or_capture (position, last_move, past_positions, turn, promotion_number, patterns):

    for i in past_positions:

        past_pos = list (list (x) for x in i)

        temp_list = copy_list (past_pos)

        if move_or_capture (last_move, temp_list, turn, promotion_number, patterns) == position:
            
            return past_pos

def move_or_capture (ply, position, turn, promotion_number, patterns):

    if len (ply) == 1:

        ply = ply [0]

    if re.search (r"capture", ply [0]):

        return capture (ply, position, turn, promotion_number, patterns)

    elif re.search (r"move", ply [0]):

        return move (ply, position, turn, promotion_number, patterns)

def move (valid_move, pos, turn, promotion_number, patterns):

    if re.search (r"kingside castle", valid_move [0]):

        rook_square = [valid_move [1] [0], valid_move [1] [1] - 1]

        if re.search (r"white", valid_move [0]):

            rook_name = "white k rook can move to"

        elif re.search (r"black", valid_move [0]):

            rook_name = "black k rook can move to"

        pos = move ([rook_name, rook_square], pos, turn, promotion_number, patterns)

        pos = move ([return_name (valid_move [0], patterns) + " can move to", valid_move [1]], pos, turn, promotion_number, patterns)

        return pos

    if re.search (r"queenside castle", valid_move [0]):

        rook_square = [valid_move [1] [0], valid_move [1] [1] + 1]

        if re.search (r"white", valid_move [0]):

            rook_name = "white q rook can move to"

        elif re.search (r"black", valid_move [0]):

            rook_name = "black q rook can move to"

        pos = move ([rook_name, rook_square], pos, turn, promotion_number, patterns)

        pos = move ([return_name (valid_move [0], patterns) + " can move to", valid_move [1]], pos, turn, promotion_number, patterns)

        return pos

    if  re.search (r"promotion", valid_move [0]):

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

        pos [final_destination[0]] [final_destination[1]] =  new_name

        return pos

    else:

        piece_name = return_name(valid_move [0], patterns)

        final_destination = valid_move [1]

        y = position_of_piece (piece_name, pos)

        pos [y[0]] [y[1]] = "empty"

        pos [final_destination[0]] [final_destination[1]] = piece_name

        return pos

def capture (valid_capture, pos, turn, promotion_number, patterns):

    if re.search (r"enpass", valid_capture [0]):

        piece_name = return_name(valid_capture [0], patterns)

        final_destination = valid_capture [1]

        y = position_of_piece (piece_name, pos)

        pos [y[0]] [y[1]] = "empty"

        if re.search (r"white", valid_capture [0]):

            pos [final_destination[0] + 1] [final_destination[1]] = piece_name

            pos [final_destination[0]] [final_destination[1]] = "empty"

            return pos

        elif re.search (r"black", valid_capture [0]):

            pos [final_destination[0] - 1] [final_destination[1]] = piece_name

            pos [final_destination[0]] [final_destination[1]] = "empty"

            return pos

    elif  re.search (r"promotion", valid_capture [0]):

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

        pos [final_destination[0]] [final_destination[1]] =  new_name

        return pos

    else:     

        piece_name = return_name(valid_capture [0], patterns)

        final_destination = valid_capture [1]

        y = position_of_piece (piece_name, pos)

        pos [y[0]] [y[1]] = "empty"

        pos [final_destination[0]] [final_destination[1]] = piece_name

        return pos

def checkmate (checking_list, content):

    for i in content:

        if i [-1] == checking_list [-1]:

            if i [-2] == checking_list [-2]:

                if i [-3] == checking_list [-3]:

                    return True
                
    return False

content = set([])

def genetic (value, position, list_of_current_valid_moves, turn, last_moves, promotion_number, patterns, past_positions):

    global content

    if value == "clear":

        content = {}

    elif value == "move":

        for j in list_of_current_valid_moves:

            if not (tuple_convert (position), turn, tuple_convert (j), "checkmate") in content:

                return j

        content.add ((past_positions [-2], turn, tuple_convert (last_moves [-2]), "checkmate"))

        return j

    elif value == "checkmate":

        content. add ((past_positions [-2], turn, tuple_convert (last_moves [-2]), "checkmate"))

    elif value == "opposite":

        pass
    
    elif value == "test":

        return reverse_move_or_capture (position, last_move, past_positions, turn, promotion_number, patterns)

        

            

            

        

                

        

                            
                            

                            



    

        

