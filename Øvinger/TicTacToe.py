'''  Project Description:
 Tic-Tac-Toe
 The aim of this project is to write a program that allows two users to play a game of Tic-Tac-Toe. Your
 program should follow the standard rules in which two players alternate turns and put X or O onto a board. If
 a player has three pieces in a row either vertically, horizontally, or diagonally, he/she is the winner. You will
 represent the Tic-Tac-Toe board using the integers 1-9 for the 9 spaces on the board. An empty spot on the
 board will be represented by an underscore
 
Status 12.10.24:
Funker sånn tålelig greit, noe rot med rekursive funksjoner og løkker, men ellers er det kjørbart.
Mindre justeringer som må til for at det funker 100% etter oppgaven.  
Mye rom for optimalisering og smartere løsninger. 

Rough layout:
----------
(x) Hvem spiller? Lagre navn i variabler 
() En måte å holde kontroll på hvem sin tur det er
(x) En liste som holder oversikt over brettet. Vi lager denne som en tabell, 
    da er det enklere å kjøre regelsjekk etterpå, kanskje?
(x) Funksjon for å tegne brettet. 
    () (finn funksjonen for å slette terminal output etter hver kjøring)
() En funksjon som validerer input og sjekker om det er ledig plass på brettet. 
        og returnerer korresponderende tall på koordinatform [x][y]
(x) En funksjon som sjekker om noen har vunnet
() En funksjon 
'''
global brett
global endGame
endGame = False
def generer_brett():
    '''Lager brettet som en liste i en liste(tabell/2D-array). Var egen funksjon før jeg fant ut at google var en ting. 
    Med den nye løsningen er det ikke behov for å ha dette som en egen funksjon'''
    global brett
    brett = [["_" for i in range(3)] for j in range(3)]
    return brett

def tegn_brett(brett:list):
    '''Tegner brettet slik vi ønsker å vise det.'''
    print("Current board: ")
    print(" ", "_"*6, sep=None)
    print("|", brett[0][0],brett[0][1],brett[0][2], "|")
    print("|", brett[1][0],brett[1][1],brett[1][2], "|")
    print("|", brett[2][0],brett[2][1],brett[2][2], "|")
    print("-"*9)
    print()
    print("Choose your square:")
    print( "_"*9, sep = None)
    print("|", "1","2","3", "|")
    print("|", "4","5","6", "|")
    print("|", "7","8","9", "|")
    print("-"*9)
    print()
    return

def harNoenVunnet(brett:list, spiller:str):
    '''Sjekker om valgt spiller har vunnet eller ikke. Returnerer symbol for spiller som angis i stor O og X'''
    global endGame
    #Horisontal sjekk:    
    for x in brett:
        if x[0] == spiller and x[1] == spiller and x[2] == spiller:
            return spiller
    #Vertikal sjekk:
    for y in range(3):
        if brett[0][y] == spiller and brett[1][y] == spiller and brett[2][y]==spiller:
            return spiller
    #Diagonal sjekk:
    if brett[0][0] == spiller and brett[1][1] == spiller and brett[2][2] == spiller:
        return spiller
    if brett[0][2] == spiller and brett[1][1] == spiller and brett[2][0] == spiller:
        return spiller
    return None

def koordinaterTilTall(x:int,y:int):
    '''Tar et sett koordinater og genererer et tall basert på disse. Forventer int.'''
    return x*3 + y+1

def tallTilKoordinater(tall:int):
    '''Motsatt operasjon av koordinaterTilTall. Forventer int: x, y'''
    x = (tall - 1) //3 #rader  
    y = (tall - 1) % 3 #kolonner 
    return x, y

def plasserBrikke(tall:int,spiller:str):
    '''Plasserer O eller X i koordinater tilsvarende tall. Spiller må være O eller X'''
    global brett
    x,y = tallTilKoordinater(tall)
    if brett[x][y] == "_": 
        brett[x][y] = spiller
        return True
    else: 
        print("Spot occupied, try another!")
        return False
    
def validerInput(tall:str):
    '''String som input, sjekker om det er et tall i området 1-9'''
    if tall.isdigit() and int(tall) in range(1,9):
        return int(tall)
    else:
        print("INPUT ERROR!")
        print("Please input a number 1-9 corresponding to the square you want")
        return False
    


print("Welcome to TicTacToe!")
print("---------------------")
print()
brett = generer_brett()
Spiller1Tegn = "X"
Spiller2Tegn = "O"
while endGame == False:
    tegn_brett(brett)
    while plasserBrikke(validerInput(input("Spiller 1:" )),"X") == False:
        if harNoenVunnet(brett, Spiller1Tegn) == Spiller1Tegn:
            print("Gratulerer Spiller1!!!")
            break
        tegn_brett(brett)
    while plasserBrikke(validerInput(input("Spiller 2:" )),"O") == False:
        
        if harNoenVunnet(brett, Spiller1Tegn) == Spiller2Tegn:
            print("Gratulerer Spiller2!!!!")
            break
        tegn_brett(brett)
    