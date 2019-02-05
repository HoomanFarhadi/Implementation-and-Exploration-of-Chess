position = [['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'white k bishop', 'white k knight', 'white k rook'], ['white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn'], ['black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']]


class Piece ():

    first_move = True

    def __init__ (self, name):

        self.name = name


list_of_pieces = []

for i in position:

    for j in i:

        if not j == "empty":

            list_of_pieces.append (Piece (j))



