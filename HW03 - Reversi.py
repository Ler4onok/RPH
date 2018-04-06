class MyPlayer:
    '''Player plays correctly'''
 
    def __init__(self, my_color, opponent_color):
        self.name = 'chyzhval'
        self.my_color = my_color
        self.opponent_color = opponent_color
 
 
    def moves_player_can_do(self, board, x, y):
 
        my_player = self.my_color
        my_opponent = self.opponent_color
 
        def player_steps(board, my_player, step_x, step_y):
            a = []
            dir = [
                (1, 0), #right
                (-1, 0), #left
                (0, 1), #down
                (0, -1), #up
                (1, 1), #down_right
                (-1, 1), #down_left
                (1, -1), #up_right
                (-1, -1) #up_left
             ]
 
            for i in dir:
                x = step_x
                y = step_y
                x += i[0]
                y += i[1]
                coordinates = []
                game = False
                while (x in range(8) and y in range(8)):
 
                    my_board = board[x][y]
 
                    if my_board == my_player:
                        game = True
                        break
 
                    if my_board == -1:
                        break
 
                    if my_board == my_opponent:
                        coordinates += [(x, y)]
 
                    x += i[0]
                    y += i[1]
                a += coordinates if game == True and len(coordinates) else []
            return a
 
        if not (x in range(8) and y in range(8) and board[x][y] == -1 ):
            return False
 
        main = []
        b = player_steps(board, my_player, x, y)
        c = len(b)
        if c: #you know it's a smile
            main += b
 
        return main if len(main) != 0 else False
 
    def MakeMove(self, board):
        for r in range(8):
            for c in range(8):
                if self.moves_player_can_do(board, r, c):
                    return (r,c)
    def move(self, board):
        return self.MakeMove(board)