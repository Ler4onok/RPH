class MyPlayer:
    '''Player plays correctly'''
 
    def __init__(self, my_color, opponent_color):
        self.name = 'chyzhval' #my name
        self.my_color = my_color
        self.opponent_color = opponent_color
 
 
    def moves_player_can_do(self, board, x, y):
 
        my_player = self.my_color
        my_opponent = self.opponent_color
 
        def player_steps(board, my_player, step_x, step_y):
            a = [] #the list with  valid coordinates
            directions = [ #directions of my player's moves
                (1, 0), #right
                (-1, 0), #left
                (0, 1), #down
                (0, -1), #up
                (1, 1), #down_right
                (-1, 1), #down_left
                (1, -1), #up_right
                (-1, -1) #up_left
             ]
 
            for i in directions:
 
                x, y = step_x, step_y
                x, y = x + i[0], y + i[1]
                coordinates = [] #the list with opponent's coordinates
                coordinates1 = []
                game = False #block the move
 
                while (x in range(8) and y in range(8)):
 
                    my_board = board[x][y]
 
                    if my_board == my_player: #if my player is at this position
                        game = True
                        break
 
                    if my_board == -1: #if the board is full
                        break
 
                    if my_board == my_opponent: #if my opponent is at this position
                        coordinates += [(x, y)] #add the coordinates to the list
 
                    x, y = x + i[0], y + i[1]
 
                if game == True: #if everything is ok
                    a += coordinates #add valid coordinates to the list
            return a
 
        if not (x in range(8) and y in range(8) and board[x][y] == -1 ): #if x and y are out of board or the board is full
            return False #end the game
 
        main = []
        b = player_steps(board, my_player, x, y)
        c = len(b)
        if c: #you know it's a smile
            main += b
 
 
        if len(main) != 0:
            return main #return valid moves
        else:
            return False
 
 
    def MakeMove(self, board):
        for r in range(8):
            for c in range(8):
                if self.moves_player_can_do(board, r, c):
                    return (r,c)
 
    def move(self, board):  #make valid moves
        return self.MakeMove(board)