# From algebraic notation to how the program accepts input which is:

#piece name : for example white q knight,  black promoted queen 1

#starting square: for example [3, 4] corrosponds to e4

#ending square: for example [3, 4] corrsoponds to e4

#action: move, capture, promotion, enpass, castling

import re

conversions = {'f1': [0, 5], 'f2': [1, 5], 'f3': [2, 5], 'f4': [3, 5], 'd8': [7, 3], 'f6': [5, 5], 'f7': [6, 5], 'f8': [7, 5], 'h3': [2, 7], 'h1': [0, 7], 'h6': [5, 7], 'h7': [6, 7], 'h4': [3, 7], 'h5': [4, 7], 'b4': [3, 1], 'b5': [4, 1], 'b6': [5, 1], 'b7': [6, 1], 'b1': [0, 1], 'b2': [1, 1], 'b3': [2, 1], 'd6': [5, 3], 'd7': [6, 3], 'd4': [3, 3], 'd5': [4, 3], 'b8': [7, 1], 'd3': [2, 3], 'd1': [0, 3], 'e1': [0, 4], 'f5': [4, 5], 'd2': [1, 3], 'e5': [4, 4], 'h2': [1, 7], 'e3': [2, 4], 'h8': [7, 7], 'e2': [1, 4], 'g7': [6, 6], 'g6': [5, 6], 'g5': [4, 6], 'g4': [3, 6], 'g3': [2, 6], 'g2': [1, 6], 'g1': [0, 6], 'e4': [3, 4], 'g8': [7, 6], 'a1': [0, 0], 'a3': [2, 0], 'a2': [1, 0], 'a5': [4, 0], 'a4': [3, 0], 'a7': [6, 0], 'a6': [5, 0], 'c3': [2, 2], 'a8': [7, 0], 'c1': [0, 2], 'e6': [5, 4], 'c7': [6, 2], 'c6': [5, 2], 'c5': [4, 2], 'c4': [3, 2], 'e7': [6, 4], 'c8': [7, 2], 'c2': [1, 2], 'e8': [7, 4]}

def convert (user_move, turn, position):

    if user_move == "O-O":

        if turn == "white":

            return ["kingside castle: white king can move to", [0, 6]]

        elif turn == "black":

            return ["kingside castle: black king can move to", [7, 6]]

    elif user_move == "O-O-O":

        if turn == "white":

            return ["queenside castle: white king can move to", [0, 2]]

        elif turn == "black":

            return ["queenside castle: black king can move to", [7, 2]]

    elif re.search (r"x", user_input):

        #if re.search (r"e.p.", user_input)

        pass

        
