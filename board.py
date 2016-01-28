import random


class Board():
    '''Class takes two arguments: size and mines.
    Size is the size of the Minesweeper board.
    Mines is the number of the mines in the board.'''
    
                
    def setupBoard(self):
        self.size = input('Define dimensions of your board:  [ints only]')
        self.mines = input('How many mines?')
        self.size = int(self.size)
        self.mines = int(self.mines)
        self.numSafeLocations = self.size**2 - self.mines
        for row in range(self.size):
            self.myBoard.append([])
            self.playerView.append([])
            for col in range(self.size):
                self.myBoard[row].append(0)
                self.playerView[row].append('X')

    def insertMines(self):
        '''Randomly places mines onto the map'''
        myMineLocations = []

        # Generates random non-duplicate mine locations
        index = 0
        while index < self.mines:
            myRandomLocation = self.generateMineLocation()
            if myRandomLocation in myMineLocations:
                continue
            else:
                myMineLocations.append(myRandomLocation)
                index += 1

        # 
        for location in myMineLocations:
            self.myBoard[location[0]][location[1]] = 'M'

            for row in range(-1,2):
                for col in range(-1,2):
                    adjacentLocation = (row + location[0],col + location[1])

                    if adjacentLocation[0] >= 0 and adjacentLocation[0] < self.size and adjacentLocation[1] >= 0 and adjacentLocation[1] < self.size:
                        if self.myBoard[adjacentLocation[0]][adjacentLocation[1]] == 'M':
                            continue
                        else:
                            self.myBoard[adjacentLocation[0]][adjacentLocation[1]] += 1

                    

    def generateMineLocation(self):
        randRow = random.randint(0,self.size - 1)
        randCol = random.randint(0,self.size - 1)
        return (randRow,randCol)
                
    def getBoard(self):
        return self.myBoard

    def getPlayerView(self):
        return self.playerView

    def printBoard(self):
        tempString = ''
        minefield = self.myBoard
        for row in minefield:
            for col in row:
                tempString += str(col)
            tempString += '\n'
        print(tempString)

    def printPlayerView(self):
        tempString = ''
        minefield = self.playerView
        for row in minefield:
            for col in row:
                tempString += str(col)
            tempString += '\n'
        print(tempString)

    def revealLocation(self,cell):
        '''Reveal the content in the cell of interest.  Change from X to actual cell content.  Cell is a tuple of (row,col).'''
        # Break up the tuple into row and column values.  
        row = cell[0]
        col = cell[1]
        # Take into account python iteration starting at 0 upwards.  
        row -= 1
        col -= 1
        self.playerView[row][col] = self.myBoard[row][col]

    def isMine(self,cell):
        # Break up the tuple into row and column values.  
        row = cell[0]
        col = cell[1]
        # Take into account python iteration starting at 0 upwards.  
        row -= 1
        col -= 1

        if self.myBoard[row][col] == 'M':
            return True
        else:
            return False

    def endGame(self,cell):
        '''Determine conditions to finish the game!'''

        if self.isMine(cell):
            self.gameOn = False
            print('You blew up!')

        if self.numRevealedLocations == self.numSafeLocations:
            self.gameOn = False
            print('You win!!!')
            print('Come back and play again soon!  :)')
            print('\n')


    def play(self):
        '''Run a while loop while gameOn is set to True.  Takes in user input to reveal a row & col.  Checks endGame() to see if the game ended.'''
        self.numRevealedLocations = 0
        while self.gameOn:
            b.printPlayerView()
            print('Choose which row and column to reveal!')
            playerRow = input('Which row #?  ')
            playerCol = input('Which col #?  ')
            cell = (playerRow,playerCol)

            if playerRow > (self.size + 1) or playerCol > (self.size + 1):
                continue
            elif playerRow > 0 and playerCol > 0:
                self.revealLocation(cell)
                #b.printPlayerView()
                self.numRevealedLocations += 1
                b.endGame(cell)
            else:
                continue



    def __init__(self):
        # Init vars
        self.myBoard = []
        self.mines = 0
        self.size = 2
        self.playerView = []
        self.gameOn= True

        # Make the board, then insert mines.  
        self.setupBoard()
        self.insertMines()


# Driver    
b = Board()
b.printBoard()
#b.printPlayerView()
b.play()



