from Database import position_of_piece

from Database import piecename_to_piececlass

import Piececlasses

import re

def possible_pawn_moves (pawn, pos):

    l = []

    if re.match (r"white", pawn):

        vert_cord = position_of_piece (pawn, pos) [0]

        horz_cord = position_of_piece (pawn, pos) [1]

        two_moves = vert_cord + 2

        one_moves = vert_cord + 1

        if horz_cord + 1 in range (0,8):

            right_capture = [vert_cord + 1, horz_cord + 1]

        else:

            right_capture = position_of_piece (pawn, pos)
            

        if horz_cord - 1 in range (0,8):

            left_capture = [vert_cord + 1, horz_cord - 1]

        else:

            left_capture = position_of_piece (pawn, pos)
        
        firstmove = piecename_to_piececlass (pawn)

        if firstmove.first_move == True and pos [two_moves] [horz_cord] == "empty" and pos [one_moves] [horz_cord] == "empty":

            l.append ([pawn + " can move to", [two_moves, horz_cord]])

        if pos [one_moves] [horz_cord] == "empty":

            if one_moves == 7:

                l.append (["queen promotion: " + pawn + " can move to", [one_moves, horz_cord]])
                l.append (["bishop promotion: " + pawn + " can move to", [one_moves, horz_cord]])
                l.append (["rook promotion: " + pawn + " can move to", [one_moves, horz_cord]])
                l.append (["knight promotion: " + pawn + " can move to", [one_moves, horz_cord]])

            elif not one_moves == 7:

                l.append ([pawn + " can move to", [one_moves, horz_cord]])

        if re.match (r"black", pos [right_capture[0]] [right_capture[1]]) and re.match (r"white", pawn):

            if right_capture [0] == 7:

                l.append (["queen promotion: " + pawn + " can capture", right_capture])
                l.append (["bishop promotion: " + pawn + " can capture", right_capture])
                l.append (["rook promotion: " + pawn + " can capture", right_capture])
                l.append (["knight promotion: " + pawn + " can capture", right_capture])

            elif not right_capture [0] == 7:

                l.append ([pawn + " can capture", right_capture])

        if re.match (r"black", pos [left_capture[0]] [left_capture[1]]) and re.match (r"white", pawn):

            if left_capture [0] == 7:

                l.append (["queen promotion: " + pawn + " can capture", left_capture])
                l.append (["bishop promotion: " + pawn + " can capture", left_capture])
                l.append (["rook promotion: " + pawn + " can capture", left_capture])
                l.append (["knight promotion: " + pawn + " can capture", left_capture])

            elif not left_capture [0] == 7:

                l.append ([pawn + " can capture", left_capture])

    if re.match (r"black", pawn):

        vert_cord = position_of_piece (pawn, pos) [0]

        horz_cord = position_of_piece (pawn, pos) [1]

        two_moves = vert_cord - 2

        one_moves = vert_cord - 1

        if horz_cord + 1 in range (0,8):

            right_capture = [vert_cord - 1, horz_cord + 1]

        else:

            right_capture = position_of_piece (pawn, pos)
            

        if horz_cord - 1 in range (0,8):

            left_capture = [vert_cord - 1, horz_cord - 1]

        else:

            left_capture = position_of_piece (pawn, pos)

        firstmove = piecename_to_piececlass (pawn)

        if firstmove.first_move == True and pos [two_moves] [horz_cord] == "empty" and pos [one_moves] [horz_cord] == "empty":

            l.append ([pawn + " can move to", [two_moves, horz_cord]])

        if pos [one_moves] [horz_cord] == "empty":

            if one_moves == 0:

                l.append (["queen promotion: " + pawn + " can move to", [one_moves, horz_cord]])
                l.append (["bishop promotion: " + pawn + " can move to", [one_moves, horz_cord]])
                l.append (["rook promotion: " + pawn + " can move to", [one_moves, horz_cord]])
                l.append (["knight promotion: " + pawn + " can move to", [one_moves, horz_cord]])

            elif not one_moves == 0:

                l.append ([pawn + " can move to", [one_moves, horz_cord]])

        if re.match (r"white", pos [right_capture[0]] [right_capture[1]]) and re.match (r"black", pawn):

            if right_capture [0] == 0:

                l.append (["queen promotion: " + pawn + " can capture", right_capture])
                l.append (["bishop promotion: " + pawn + " can capture", right_capture])
                l.append (["rook promotion: " + pawn + " can capture", right_capture])
                l.append (["knight promotion: " + pawn + " can capture", right_capture])

            elif not right_capture [0] == 0:

                l.append ([pawn + " can capture", right_capture])

        if re.match (r"white", pos [left_capture[0]] [left_capture[1]]) and re.match (r"black", pawn):

            if left_capture [0] == 0:

                l.append (["queen promotion: " + pawn + " can capture", left_capture])
                l.append (["bishop promotion: " + pawn + " can capture", left_capture])
                l.append (["rook promotion: " + pawn + " can capture", left_capture])
                l.append (["knight promotion: " + pawn + " can capture", left_capture])

            elif not left_capture [0] == 0:

                l.append ([pawn + " can capture", left_capture])

    return l

