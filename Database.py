import Piececlasses

position = [['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'white k bishop', 'white k knight', 'white k rook'], ['white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn'], ['black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']]

def make_position (position):

    new_position = position

    for i in range (8):

        for j in range (8):

            user_input = input (": ")

            new_position [i] [j] = user_input

    return new_position
            

if __name__ == "__main__":

    print (make_position (position))


def position_of_piece (piece, pos):

    for i in range (8):

        for j in range (8):

            if pos [i] [j] == piece:

                return [i ,j]
            
def piecename_to_piececlass (piecename):

    for i in Piececlasses.list_of_pieces:

        if i.name == piecename:

            return i
