import random
import numpy

class Tile:
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        
    def move(self, x, y):
        self.x = x
        self.y = y
        self.value = self.value - 1


class Border:
    def __init__(self, length):
        self.length = length
        self.grid = [[None for x in range(length)] for y in range(length)]
        grid = self.grid
        for i in range(len(grid[0])):
            grid[0][i] = self.randomValue()
            grid[length-1][i] = self.randomValue()
            grid[i][0] = self.randomValue()
            grid[i][length-1] = self.randomValue()

    def randomValue(self):
        return random.randint(1,4)

    def print(self):
        g = self.grid
        grid = [[None for x in range(self.length)] for y in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                if g[i][j] == None:
                    grid[i][j] = 0
                else:
                    grid[i][j] = g[i][j]
        
        for i in grid:
            print(i)



class Board:
    def __init__(self, length):
        self.length = length
        self.grid = [[None for x in range(length)] for y in range(length)]
        border = Border(length+2)
        self.borderGrid = border.grid

    def show(self):
        g = self.grid
        grid = [[None for x in range(self.length)] for y in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                if g[i][j] == None:
                    grid[i][j] = 'E0'
                else:
                    grid[i][j] = 'T' + str(g[i][j].value)
        print('\n')
        for i in grid:
            print(i)
        print('\n')

    def randomValue(self):
        return random.randint(1,4)

    def randomX(self):
        return random.randint(0,self.length-1)

    def newTile(self):
        grid = self.grid
        tile = Tile(self.randomX(), 0, self.randomValue())
        for i in range(self.length):
            if grid[i][tile.x] != None:
                tile.y = i-1
                grid[i-1][tile.x] = tile
                return("\nNew tile at (" + str(1 + tile.x) + "," + str(8 - tile.y) + ")")
                
            elif i == self.length-1:
                tile.y = i
                grid[i][tile.x] = tile
                return("\nNew tile at (" + str(1 + tile.x) + "," + str(8 - tile.y) + ")")


    def print(self):
        g = self.grid
        border = self.borderGrid
        board = [[None for x in range(len(border))] for y in range(len(border))]
        for i in range(len(board[0])):
            board[0][i] = ' ' + str(border[0][i])
            board[len(board)-1][i] = ' ' + str(border[len(border)-1][i])
            board[i][0] = str(border[i][0]) + ' |'
            board[i][len(board)-1] = '| ' + str(border[i][len(border)-1])
                    
        for i in range(self.length):
            for j in range(self.length):
                if g[i][j] == None:
                    board[i+1][j+1] = 'E0'
                else:
                    board[i+1][j+1] = 'T' + str(g[i][j].value)
        print('\n')
        board[0][0] = '  '
        board[0][len(board)-1] = '  '
        board[len(board)-1][0] = '  '
        board[len(board)-1][len(board)-1] = '  '
        for i in range(len(board)):
            print(' '.join(board[i]))
            if i == 0 or i == len(board)-2:
                print('   ' + '-' * 3 * (len(board)-2))
            
        print('\n')
        
    def add(self, tile):
        self.grid[tile.y][tile.x] = tile

    def remove(self, tile):
        self.grid[tile.y][tile.x] = None
        self.update()
        
    def move(self, x, y, direction):
        if direction != None:
            x = x - 1
            y = 8 - y
        grid = self.grid
        try:
            value = grid[y][x].value
            tile = Tile(x, y, value)
        except:
            print("NO TILE SELECTED")
            return
            
        if direction == 'r':
            try:
                tile.move(x+1, self.gravity(x+1, y))
                if not self.isTile(tile.x, tile.y):
                    self.add(tile)
                else:
                    print("THERE IS ALREADY A TILE THERE")
                    return
            except:
                print("INDEX ERROR")
                return

        elif direction == 'l':
            if x-1 >= 0:
                tile.move(x-1, self.gravity(x-1, y))
                if not self.isTile(tile.x, tile.y):
                    self.add(tile)
                else:
                    print("THERE IS ALREADY A TILE THERE")
                    return
            else:
                print("INDEX ERROR")
                return

        else:
            tile.y = self.gravity(x, y)
            self.add(tile)
            
        self.remove(grid[y][x])
        
        try:
            if grid[y-1][x] != None:
                self.move(x, y-1, None)
        except:
            pass
        self.update()
        
    def gravity(self, x, y):
        grid = self.grid
        try:
            if grid[y+1][x]  == None:
                y += 1
                return self.gravity(x, y)
        except:
            pass
        
        return y

    def isTile(self,x ,y):
       if self.grid[y][x] != None:
           return True

    def rotateBorder(self):
        self.borderGrid = numpy.rot90(self.borderGrid, -1)

    def update(self):
        global points
        grid = self.grid
        border = self.borderGrid
        length = self.length
        for i in range(length):
            for j in range(length):
                #left edge cases
                if self.isTile(i,j) and i==0:
                    if grid[j][0].value == border[j+1][0]:
                        print("\n" + str(grid[j][0].value) + " points gained. (L)(0," + str(8-j) + ")")
                        points += grid[j][0].value
                        self.remove(grid[j][0])
                        if grid[j-1][0] != None:
                            self.move(0, j-1, None)
                #right edge case
                if self.isTile(i,j) and i==length-1:
                    if grid[j][length-1].value == border[j+1][length+1]:
                        print("\n" + str(grid[j][length-1].value) + " points gained. (R)(8," + str(8-j) + ")")
                        points += grid[j][length-1].value
                        self.remove(grid[j][length-1])
                        if grid[j-1][length-1] != None:
                            self.move(length-1, j-1, None)
                #floor case
                if self.isTile(i,j) and j==length-1:
                    if grid[length-1][i].value == border[length+1][i+1]:
                        print("\n" + str(grid[length-1][i].value) + " points gained. (F)(" + str(1+i) + ",0)")
                        points += grid[length-1][i].value
                        self.remove(grid[length-1][i])
                        if grid[j-1][i] != None:
                            self.move(i, j-1, None)
                    
                    
        

board = Board(8)

board.add(Tile(0, 7, 4))
board.add(Tile(1, 7, 1))
board.add(Tile(1, 6, 2))
#board.add(Tile(3, 7, 0))
board.add(Tile(5, 7, 3))
board.add(Tile(5, 6, 4))
board.add(Tile(6, 7, 4))

turn = 1
global points
points = 0

while(True):
    print("-----------TURN " + str(turn) + "-----------")
    if turn != 1:
        print(board.newTile())
        print(board.newTile())
        print(board.newTile())
        print(board.newTile())

        board.update()
        print("\nTotal points at the start of the round: " + str(points))

    board.print()
    board.update()
    while(True):
        userInput = input("\nType MOVE, SHOW or END: ")
        if userInput.upper() == "MOVE":
            try:
                x = int(input("X: "))
                y = int(input("Y: "))
                direction = input("Direction: ")
                if direction.lower() == 'r' or direction.lower() == 'l':
                    board.move(x, y, direction.lower())
                else:
                    print("NO VALID DIRECTION")
                print('\n')
            except:
                print("NO INT")
            
        elif userInput.upper() == "SHOW":
            board.print()
        elif userInput.upper() == "END":
            print('\n')
            board.update()
            board.rotateBorder()
            
            turn += 1
            break
        else:
            print("ERROR")

