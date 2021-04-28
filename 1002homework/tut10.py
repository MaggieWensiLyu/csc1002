class Game:
    def __init__(self, board = [["0","0","0"],
                                ["0","0","0"],
                                ["0","0","0"]]):
        self.board = board
    # def setBoard(self,board):
    #     self.board = board
    def drawBoard(self):
        for row in self.board:
         b = " | ".join(row)
         b.replace("1","x")
         b.replace("2","o")
         b.replace("0"," ")
         print(b)

    def player_1_move(self,column,row):
        self.board[column-1][row-1] = 1 #check whether it is valid
    def player_2_move(self,column,row):
        self.board[column-1][row-1] = 2 #same pb
    def checkFull(self):
        b = set(self.board)
        if 0 in b:
            print("the game is full")
            return True     
    def checkBoard(self):
        if self.board[0][0] == 1:
            if self.board[0][1] == 1 and self.board[0][2] == 1:
                print("one")
            elif   self.board[1][0] == 1 and self.board[2][0] == 1:
                print("one")
            elif  self.board[1][1] == 1 and self.board[2][2] == 1:
                print("one")
        if self.board[0][0] == 2:
            if self.board[0][1] == 2 and self.board[0][2] == 2:
                print("two")
            elif   self.board[1][0] == 2 and self.board[2][0] == 2:
                print("two")
            elif  self.board[1][1] == 2 and self.board[2][2] == 2:
                print("two")
        else:
            print("none")


   

game = Game()
# print(type(game.drawBoard()))
game.drawBoard()