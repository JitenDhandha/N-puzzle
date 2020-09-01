####################################################################################
# Jiten Dhandha, 2020                                                              #
# A text-based N-puzzle (also known as sliding tile puzzle).                       #
####################################################################################

import numpy as np

#GLOBAL VARIABLES
N = 2    #Dimensions of game board
BOARD = np.zeros((N,N),dtype=int)    #The current state of the game board
CHKBOARD = np.zeros((N,N),dtype=int)    #The solved game board

#Function that initializes both BOARD and CHKBOARD
def create_board():

    global N, BOARD, CHKBOARD

    #Creating a "solved" game board
    BOARD = BOARD.flatten()
    for counter in range(1,N*N):
        BOARD[counter-1] = counter
    BOARD = BOARD.reshape(N,N)
    BOARD[-1][-1] = 0

    #Copying it over to CHKBOARD
    CHKBOARD[:] = BOARD[:]

#Function that shuffles the BOARD into a solvable state
def randomize_board():
    
    global N, BOARD, CHKBOARD
    
    #Performing Fisher-Yates shuffle
    BOARD = BOARD.flatten()
    for i in range(0,N*N-1): 
        j = np.random.randint(i,N*N) 
        BOARD[i], BOARD[j] = BOARD[j], BOARD[i]

    #Checking for solvability - see 'https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html'
    inversions = 0
    for i in range(0,N*N):
        num1 = BOARD[i]
        for j in range(i+1,N*N):
            num2 = BOARD[j]
            if(num1>num2 and num1!=0 and num2!=0):
                inversions+=1

    BOARD = BOARD.reshape(N,N)

    r0,c0 = np.where(BOARD==0)
    if(N%2==0 and inversions%2==0 and not r0%2==0):
        pass
    elif(N%2==0 and not inversions%2==0 and r0%2==0):
        pass
    elif(not N%2==0 and inversions%2==0):
        pass
    else:
        #Unsolvable so swap elements 1 and 2
        r1,c1 = np.where(BOARD==1)
        r2,c2 = np.where(BOARD==2)        
        BOARD[r1,c1], BOARD[r2,c2] = BOARD[r2,c2], BOARD[r1,c1]

#Function that prints the BOARD
def print_board():
    
    global N, BOARD

    #Printing a pretty game board
    print()
    for i in range(N):
        for j in range(N):
            print('{:6}'.format(BOARD[i][j]),end="")
        print()

#Function that swaps pieces in the BOARD
def swap_pieces(piece):

    global N, BOARD

    #Checking if input is an int
    try:
        piece = int(piece)
    except:
        print("Invalid input!")
        return

    #Checking if the input makes sense
    if(piece<1 or piece>N*N-1 or piece==0):
        print("Invalid input!")
        return

    #Attempting to move the piece
    r,c = np.where(BOARD==piece)
    r0,c0 = np.where(BOARD==0)

    if( (r0==r and (c0==c+1 or c0==c-1)) or (c0==c and (r0==r+1 or r0==r-1)) ):
        BOARD[r,c], BOARD[r0,c0] = BOARD[r0,c0], BOARD[r,c]
    else:
        print("Cannot move the piece anywhere!")

#Function that checks if the BOARD is solved
def check_board():

    global BOARD, CHKBOARD
    return (np.all(CHKBOARD==BOARD))

def main():

    #Initializing the game
    print("Starting game...")
    create_board()
    print("Randomizing board...")
    randomize_board()
    print_board()

    #Taking turns till it's solved or game is quit
    while(not check_board()):
        choice = input("Enter piece: ")
        if(choice=='q' or choice=='Q'):
            print("\nGame quit.")
            break
        else:
            swap_pieces(choice)
            print_board()

    #Printing an encouraging message in case of a win ;)
    if(check_board()):
        print("\nYou win! :)")

if __name__ == '__main__':
    main()
