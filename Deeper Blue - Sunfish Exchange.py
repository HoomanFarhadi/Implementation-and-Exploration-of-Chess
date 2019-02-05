import DeeperBlue

import sunfish

import time

import Piececlasses

#current survial is 90 moves. If we assume that there are on average 15 moves per position, we would
#need to play 8^45 games to trace to the beggening . Current speed is about 7s per game, so this
#would take ~ 1.775 * 10 ^ 39 earth years (unfeasable).

player = "deeper blue"

previous_pieces = []

enpassent = {'a4b3': 'a4b4', 'a5b6': 'a5b5', 'b4c3': 'b4c4', 'b4a3': 'b4a4', 'b5c6': 'b5c5', 'b5a6': 'b5a5', 'c4d3': 'c4d4', 'c4b3': 'c4b4', 'c5d6': 'c5d5', 'c5b6': 'c5b5', 'd4e3': 'd4e4', 'd4c3': 'd4c4', 'd5e6': 'd5e5', 'd5c6': 'd5c5', 'e4f3': 'e4f4', 'e4d3': 'e4d4', 'e5f6': 'e5f5', 'e5d6': 'e5d5', 'f4g3': 'f4g4', 'f4e3': 'f4e4', 'f5g6': 'f5g5', 'f5e6': 'f5e5', 'g4h3': 'g4h4', 'g4f3': 'g4f4', 'g5h6': 'g5h5', 'g5f6': 'g5f5', 'h4g3': 'h4g4', 'h5g6': 'h5g5'}

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

def after_before_convert (first, second):

    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

    numbers = ["1","2","3","4","5","6","7","8"]

    num1  = numbers [first [0]]

    let1 = letters [first [1]]

    num2 = numbers [second [1] [0]]

    let2 = letters [second [1] [1]]

    return let1 + num1 + let2 + num2

def exchange (position):

    if DeeperBlue.turn == "white":

        temp_position = DeeperBlue.copy_2D_list (DeeperBlue.position)

        #print (DeeperBlue.current_valid_moves (DeeperBlue.turn, DeeperBlue.position))

        #print (DeeperBlue.turn)

        #print (DeeperBlue.position)

        return_ply = DeeperBlue.GA.genetic ("move", DeeperBlue.position, DeeperBlue.current_valid_moves (DeeperBlue.turn, DeeperBlue.position), DeeperBlue.turn, DeeperBlue.last_moves, DeeperBlue.promotion_number, DeeperBlue.patterns, DeeperBlue.last_positions)

        #print (return_ply)

        previous_pieces. append (DeeperBlue.position_of_piece (DeeperBlue.return_name (return_ply [0], DeeperBlue.patterns), temp_position))

        first = previous_pieces [-1]
        
        DeeperBlue.move_or_capture (return_ply, DeeperBlue.position, first)

    elif DeeperBlue.turn == "black":

        last_move = "None" if DeeperBlue.past_moves == [] else DeeperBlue.past_moves [-1]

        first_move = previous_pieces [-1]

        return_move = after_before_convert (first_move, last_move)

        #print(return_move)

        #try:

        x = sunfish.main (return_move)

        #except:

        #x = input("Custom Move: ")

        first = x [:-2]
        
        recieved = DeeperBlue.before_after_convert (x, DeeperBlue.position)

        if recieved == []:

            recieved = DeeperBlue.before_after_convert (enpassent [x], DeeperBlue.position)

        DeeperBlue.move_or_capture (recieved, DeeperBlue.position, first)

        last_move = "None" if DeeperBlue.past_moves == [] else DeeperBlue.past_moves [-1]

        #DeeperBlue.gen ("opposite", DeeperBlue.copy_2D_list (DeeperBlue.position), DeeperBlue.current_valid_moves (DeeperBlue.turn, DeeperBlue.position), DeeperBlue.turn, last_move, DeeperBlue.promotion_number, DeeperBlue.patterns, last_position)

try:

    DeeperBlue.GA.content = contents ("Gamefile.txt")

    count = 0

    while True:

        #t = time.time()

        #yes = 0

        while True:

            pos = tuple (tuple (x) for x in DeeperBlue.position)

            #time.sleep(2.5)

            #print (pos)

            DeeperBlue.print_board (DeeperBlue.position, DeeperBlue.column, DeeperBlue.row)

            #print (current_valid_moves (turn, position))

            if pos in DeeperBlue.past_positions:

                DeeperBlue.past_positions [pos] += 1

            else:

                DeeperBlue.past_positions [pos] = 1

            value = DeeperBlue.win_or_draw (DeeperBlue.position, DeeperBlue.past_positions)

            if value == "game over":

                break

            #y = time.time()

            exchange (DeeperBlue.position)

            #yes += 1

            #print (time.time() - y)

            #change_player ()

            DeeperBlue.change_turn ()

        #print ("moves: " + str (yes))

        DeeperBlue.position = [['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'white k bishop', 'white k knight', 'white k rook'], ['white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], ['black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn'], ['black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']]

        DeeperBlue.turn = "white"

        DeeperBlue.promotion_number = 1

        DeeperBlue.patterns = ['white q rook', 'white q knight', 'white q bishop', 'white queen', 'white king', 'white k bishop', 'white k knight', 'white k rook', 'white A pawn', 'white B pawn', 'white C pawn', 'white D pawn', 'white E pawn', 'white F pawn', 'white G pawn', 'white H pawn', 'black A pawn', 'black B pawn', 'black C pawn', 'black D pawn', 'black E pawn', 'black F pawn', 'black G pawn', 'black H pawn', 'black q rook', 'black q knight', 'black q bishop', 'black queen', 'black king', 'black k bishop', 'black k knight', 'black k rook']

        DeeperBlue.past_positions = {}

        DeeperBlue.past_moves = []

        DeeperBlue.past_inputs = []

        DeeperBlue.last_positions = []

        DeeperBlue.last_moves = []

        Piececlasses.list_of_pieces = []

        previous_pieces = []

        for i in DeeperBlue.position:

            for j in i:

                if not j == "empty":

                    Piececlasses.list_of_pieces.append (Piececlasses.Piece (j))

        sunfish.pos = sunfish.Position(sunfish.initial, 0, (True,True), (True,True), 0, 0)
        
        sunfish.searcher = sunfish.Searcher()

        #print (time.time() - t)

        count += 1

        print (count)

except KeyboardInterrupt:

    print ("Write experience to file?")

    user_input = input ("Your choice: ")

    while not user_input == "yes" and not user_input == "no":

        print ("Invalid input!")

        user_input = input ("Your choice: ")

    if user_input == "yes":

        filewrite (DeeperBlue.GA.content, "Gamefile.txt")
