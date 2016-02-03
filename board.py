import random


class Board():
    '''Class takes two inputs: size and mines.
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

        # Generates a list of random non-duplicate mine locations.  Uses helper function generateMineLocation(), which returns a random tuple.  
        index = 0
        while index < self.mines:
            myRandomLocation = self.generateMineLocation()
            if myRandomLocation in myMineLocations:
                continue
            else:
                myMineLocations.append(myRandomLocation)
                index += 1

        # Fills out the mine's adjacent locations with a counter for how many mines are nearby.  
        for location in myMineLocations:
            self.myBoard[location[0]][location[1]] = 'M'
            adjacentLocations = self.getAdjacentLocations(location)

            for neighbor in adjacentLocations:
                if self.myBoard[neighbor[0]][neighbor[1]] == 'M':
                    continue
                else:
                    self.myBoard[neighbor[0]][neighbor[1]] += 1
                    
    def cascade(self,cell):
        '''Reveals all adjacent non-mine locations if the player chooses a cell with value 0.  Continues to other locations with value 0.'''

        cellAdjacentLocations = self.getAdjacentLocations(cell)
        for neighbor in cellAdjacentLocations:
                if self.isMine(neighbor):
                    continue
                elif neighbor == cell:
                    continue
                elif self.isEmpty(neighbor) and self.playerView[neighbor[0]][neighbor[1]] == 'X':
                    self.revealLocation(neighbor)
                    self.cascade(neighbor)
                else:
                    self.revealLocation(neighbor)



    def generateMineLocation(self):
        randRow = random.randint(0,self.size - 1)
        randCol = random.randint(0,self.size - 1)
        return (randRow,randCol)

    def getAdjacentLocations(self,cell):
        '''Returns all adjacentLocations of the input cell as a list of tuples.  Cell is a tuple.'''
        adjacentLocations = []

        for row in range(-1,2):
                for col in range(-1,2):
                    adjacentLocation = (row + cell[0],col + cell[1])

                    if adjacentLocation[0] >= 0 and adjacentLocation[0] < self.size and adjacentLocation[1] >= 0 and adjacentLocation[1] < self.size:
                        adjacentLocations.append(adjacentLocation)

        return adjacentLocations

    def printBoard(self):
        '''This is a cheat method for trouble-shooting ONLY'''
        tempString = ''
        minefield = self.myBoard
        for row in minefield:
            for col in row:
                tempString += str(col)
            tempString += '\n'
        print(tempString)

    def printPlayerView(self):
        '''This is what the player sees.  It starts as a bunch of X's.'''
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
        
        # Added if-statement to make sure the reveal is not repeated
        if self.playerView[row][col] == 'X':
            self.playerView[row][col] = self.myBoard[row][col]
            self.numRevealedLocations += 1

    def reduceIndex(self,cell):
        '''Take into account python iteration starting at 0 for indices.'''

        # Break up the tuple into row and column values.  
        row = cell[0]
        col = cell[1]

        # Take into account python iteration starting at 0 upwards.  
        row -= 1
        col -= 1

        return (row,col)

    def isMine(self,cell):
        '''Checks if the cell contains a mine.  Returns True if so; False otherwise.'''
        # Break up the tuple into row and column values.  
        row = cell[0]
        col = cell[1]

        if self.myBoard[row][col] == 'M':
            return True
        else:
            return False

    def isEmpty(self,cell):
        '''Checks if the cell contains nothing (i.e., a zero).  Returns True if so; False otherwise.'''
        # Break up the tuple into row and column values.  
        row = cell[0]
        col = cell[1]

        if self.myBoard[row][col] == 0:
            return True
        else:
            return False

    def endGame(self,cell):
        '''Determine conditions to finish the game!'''

        if self.isMine(cell):
            self.gameOn = False
            print('You blew up!')
        elif self.isEmpty(cell):
            self.cascade(cell)

        if self.numRevealedLocations == self.numSafeLocations:
            self.gameOn = False
            self.printBoard()
            print('You win!!!')
            print('Come back and play again soon!  :)')
            print('\n')


    def play(self):
        '''Run a while loop while gameOn is set to True.  Takes in user input to reveal a row & col.  Checks endGame() to see if the game ended.'''
        while self.gameOn:
            b.printPlayerView()
            print('Choose which row and column to reveal!  Enter 0 to quit  ')
            playerRow = input('Which row #?  ')
            # quit clause
            if playerRow == 0:
                quit()
            playerCol = input('Which col #?  ')

            # Player has chosen location var cell on the board to unhide
            cell = (playerRow,playerCol)
            cell = self.reduceIndex(cell)
            if playerRow > (self.size + 1) or playerCol > (self.size + 1):
                continue
            elif playerRow > 0 and playerCol > 0:
                self.revealLocation(cell)
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
        self.numRevealedLocations = 0


        # Make the board, then insert mines.  
        self.setupBoard()
        self.insertMines()


# Driver    
b = Board()
b.printBoard()
b.play()



