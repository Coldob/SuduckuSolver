#Hi
from copy import copy

possibleNumbers = [1,2,3,4,5,6,7,8,9,0]
possibleLetters = ['a','b','c','d','e','f','g','h','i']
symbols = ['a1','a2','a3','a4','a5','a6','a7','a8','a9',
'b1','b2','b3','b4','b5','b6','b7','b8','b9',
'c1','c2','c3','c4','c5','c6','c7','c8','c9',
'd1','d2','d3','d4','d5','d6','d7','d8','d9',
'e1','e2','e3','e4','e5','e6','e7','e8','e9',
'f1','f2','f3','f4','f5','f6','f7','f8','f9',
'g1','g2','g3','g4','g5','g6','g7','g8','g9',
'h1','h2','h3','h4','h5','h6','h7','h8','h9',
'i1','i2','i3','i4','i5','i6','i7','i8','i9']

quadrants = [['a1','a2','a3','b1','b2','b3','c1','c2','c3'],
     ['a4','a5','a6','b4','b5','b6','c4','c5','c6'],
     ['a7','a8','a9','b7','b8','b9','c7','c8','c9'],
     ['d1','d2','d3','e1','e2','e3','f1','f2','f3'],
     ['d4','d5','d6','e4','e5','e6','f4','f5','f6'],
     ['d7','d8','d9','e7','e8','e9','f7','f8','f9'],
     ['g1','g2','g3','h1','h2','h3','i1','i2','i3'],
     ['g4','g5','g6','h4','h5','h6','i4','i5','i6'],
     ['g7','g8','g9','h7','h8','h9','i7','i8','i9']]

possibilities= {'a1':[],'a2':[],'a3':[],'a4':[],'a5':[],'a6':[],'a7':[],'a8':[],'a9':[],
'b1':[],'b2':[],'b3':[],'b4':[],'b5':[],'b6':[],'b7':[],'b8':[],'b9':[],
'c1':[],'c2':[],'c3':[],'c4':[],'c5':[],'c6':[],'c7':[],'c8':[],'c9':[],
'd1':[],'d2':[],'d3':[],'d4':[],'d5':[],'d6':[],'d7':[],'d8':[],'d9':[],
'e1':[],'e2':[],'e3':[],'e4':[],'e5':[],'e6':[],'e7':[],'e8':[],'e9':[],
'f1':[],'f2':[],'f3':[],'f4':[],'f5':[],'f6':[],'f7':[],'f8':[],'f9':[],
'g1':[],'g2':[],'g3':[],'g4':[],'g5':[],'g6':[],'g7':[],'g8':[],'g9':[],
'h1':[],'h2':[],'h3':[],'h4':[],'h5':[],'h6':[],'h7':[],'h8':[],'h9':[],
'i1':[],'i2':[],'i3':[],'i4':[],'i5':[],'i6':[],'i7':[],'i8':[],'i9':[]}
exists = {}
game = True
matching = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[]}

def setup():
    for x in temp:
        temp2 = x.split(" ")
        location = temp2[0]
        value = int(temp2[1])
        exists[location] = value
        possibilities.pop(location)

def findQuad(sym):
    for x in range(9):
        for y in range(9):
            if sym == quadrants[x][y]:
                return(x)

def eliminatingNumbers(letter, num):
    possibleNumbers = [1,2,3,4,5,6,7,8,9]
    #column
    for x in possibleLetters:
        if (type(exists.get(x+num))==int):
            try:
                possibleNumbers.remove(exists.get(x+num))
            except:
                pass
    #row
    for x in range(9):
        z = str(x)
        if (type(exists.get(letter+z))==int):
            try:
                possibleNumbers.remove(exists.get(letter+z))
            except:
                pass
    #quadrant
    quadrant = findQuad(letter+num)
    for x in quadrants[quadrant]:
        if (type(exists.get(x))==int):
            try:
                possibleNumbers.remove(exists.get(x))
            except:
                pass
    return(possibleNumbers)



def reCheck():
    temp = []
    for x in possibilities:
        if len(possibilities[x])==1:
            temp.append(x)
    if len(temp)==0:
        return(False)
    else:
        for x in temp:
            exists[x] = (possibilities[x][0])
            possibilities.pop(x)
            return(True)


def addRowsto(char):
    print(char)
    temp = {}
    for x in possibilities[(char + '1')]:
        temp[(char + '1')] = x
        for x in possibilities[(char + '2')]:
            temp[(char + '2')] = x
            for x in possibilities[(char + '3')]:
                temp[(char + '3')] = x
                for x in possibilities[(char + '4')]:
                    temp[(char + '4')] = x
                    for x in possibilities[(char + '5')]:
                        temp[(char + '5')] = x
                        for x in possibilities[(char + '6')]:
                            temp[(char + '6')] = x
                            for x in possibilities[(char + '7')]:
                                temp[(char + '7')] = x
                                for x in possibilities[(char + '8')]:
                                    temp[(char + '8')] = x
                                    for x in possibilities[(char + '9')]:
                                        temp[(char + '9')] = x
                                        checkRow = []
                                        for x in temp:
                                            checkRow.append(temp[x])
                                        if len(checkRow) == len(set(checkRow)):
                                            matching[char].append(copy(temp))

def finalCheck(board):
    #quadrant
    for x in quadrants:
        templist = []
        for y in x:
            templist.append(board[y])
        if len(templist) != len(set(templist)):
            return(False)
    #column
    for y in range(9):
        y += 1
        sY = str(y)
        templist = []
        for x in possibleLetters:
            templist.append(board[x+sY])
        if len(templist) != len(set(templist)):
            return(False)
    return(True)

def combine():
    attemptNum = 0
    for rowA in matching['a']:
        for rowB in matching['b']:
            for rowC in matching['c']:
                for rowD in matching['d']:
                    for rowE in matching['e']:
                        for rowF in matching['f']:
                            for rowG in matching['g']:
                                for rowH in matching['h']:
                                    for rowI in matching['i']:
                                        attemptNum = attemptNum + 1
                                        tempExists = {}
                                        tempExists.update(rowA)
                                        tempExists.update(rowB)
                                        tempExists.update(rowC)
                                        tempExists.update(rowD)
                                        tempExists.update(rowE)
                                        tempExists.update(rowF)
                                        tempExists.update(rowG)
                                        tempExists.update(rowH)
                                        tempExists.update(rowI)
                                        print(attemptNum)
                                        if finalCheck(tempExists):
                                            return(tempExists)



print("""
──────────────────────────────────
───────────────▀█▄█▀──────────────
────────▄█████▄─███───────────────          _____                    _____                    _____
──────▄████████████▄██████▄───────         /\    \                  /\    \                  /\    \\
──────██████████████████████──────        /::\    \                /::\____\                /::\____\\
──────██████████████████████──────       /::::\    \              /:::/    /               /:::/    /
──────██████████████████████──────      /::::::\    \            /:::/    /               /:::/    /
──────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█──────     /:::/\:::\    \          /:::/    /               /:::/    /
──────██████████████████████──────    /:::/  \:::\    \        /:::/    /               /:::/____/
────▄█▀▀──────────────────▀▀█▄────   /:::/    \:::\    \      /:::/    /               /::::\    \\
──▄█▀────────────────────────▀█▄──  /:::/    / \:::\    \    /:::/    /      _____    /::::::\____\\________
─█▀────▄▀▀▀▀▄────────▄▀▀▀▀▄────▀█─ /:::/    /   \:::\ ___\  /:::/____/      /\    \  /:::/\:::::::::::\    \\
─█────█──▄▄──█─▄▀▀▄─█──▄▄──█────█─/:::/____/     \:::|    ||:::|    /      /::\____\/:::/  |:::::::::::\____\\
─█────█─████─██░░░░██─████─█────█─\:::\    \     /:::|____||:::|____\     /:::/    /\::/   |::|~~~|~~~~~
██──▄▄███████▀░░░░░░▀███████▄▄──██ \:::\    \   /:::/    /  \:::\    \   /:::/    /  \/____|::|   |
█──▀█░░░░░░░░░░▄▄▄▄░░░░░░░░░░█▀──█  \:::\    \ /:::/    /    \:::\    \ /:::/    /         |::|   |
█───▀█▀▄▄▄▄▄▄▀▀░░░░▀▀▄▄▄▄▄▄▀█▀───█   \:::\    /:::/    /      \:::\    /:::/    /          |::|   |
█────▀▄░░░░░░░░▄▄▄▄░░░░░░░░▄▀────█    \:::\  /:::/    /        \:::\__/:::/    /           |::|   |
██─────▀▀▀▀▀▀▀▀────▀▀▀▀▀▀▀▀─────██     \:::\/:::/    /          \::::::::/    /            |::|   |
─█──────────────────────────────█─      \::::::/    /            \::::::/    /             |::|   |
─█▄────────────────────────────▄█─       \::::/    /              \::::/    /              \::|   |
──█▄──────────────────────────▄█──        \::/____/                \::/____/                \:|   |
───█▄────────────────────────▄█───        ~~                        ~~                       \|___|
──────────────────────────────────
""")
print("""Welcome to Suduku Solver
the layout of the board is below""")
print("""a1|a2|a3|  |a4|a5|a6|  |a7|a8|a9
b1|b2|b3|  |b4|b5|b6|  |b7|b8|b9
c1|c2|c3|  |c4|c5|c6|  |c7|c8|c9
--------------------------------
d1|d2|d3|  |d4|d5|d6|  |d7|d8|d9
e1|e2|e3|  |e4|e5|e6|  |e7|e8|e9
f1|f2|f3|  |f4|f5|f6|  |f7|f8|f9
--------------------------------
g1|g2|g3|  |g4|g5|g6|  |g7|g8|g9
h1|h2|h3|  |h4|h5|h6|  |h7|h8|h9
i1|i2|i3|  |i4|i5|i6|  |i7|i8|i9""")

print("Enter all \"location value, nextlocation value...\"")
print("*warning is not user friendly : )*")
temp = input()
temp = temp.split(", ")
setup()

while game:
    for x in possibilities:
        letter = x[0]
        num = x[1]
        possibilities[x] = eliminatingNumbers(letter, num)
    game = reCheck()
if len(possibilities)==0:
    print("Big Brain Play")
    board = f"""
    {exists['a1']}|{exists['a2']}|{exists['a3']}|  |{exists['a4']}|{exists['a5']}|{exists['a6']}|  |{exists['a7']}|{exists['a8']}|{exists['a9']}\n
    {exists['b1']}|{exists['b2']}|{exists['b3']}|  |{exists['b4']}|{exists['b5']}|{exists['b6']}|  |{exists['b7']}|{exists['b8']}|{exists['b9']}\n
    {exists['c1']}|{exists['c2']}|{exists['c3']}|  |{exists['c4']}|{exists['c5']}|{exists['c6']}|  |{exists['c7']}|{exists['c8']}|{exists['c9']}\n
    ───────────────────────
    {exists['d1']}|{exists['d2']}|{exists['d3']}|  |{exists['d4']}|{exists['d5']}|{exists['d6']}|  |{exists['d7']}|{exists['d8']}|{exists['d9']}\n
    {exists['e1']}|{exists['e2']}|{exists['e3']}|  |{exists['e4']}|{exists['e5']}|{exists['e6']}|  |{exists['e7']}|{exists['e8']}|{exists['e9']}\n
    {exists['f1']}|{exists['f2']}|{exists['f3']}|  |{exists['f4']}|{exists['f5']}|{exists['f6']}|  |{exists['f7']}|{exists['f8']}|{exists['f9']}\n
    ───────────────────────
    {exists['g1']}|{exists['g2']}|{exists['g3']}|  |{exists['g4']}|{exists['g5']}|{exists['g6']}|  |{exists['g7']}|{exists['g8']}|{exists['g9']}\n
    {exists['h1']}|{exists['h2']}|{exists['h3']}|  |{exists['h4']}|{exists['h5']}|{exists['h6']}|  |{exists['h7']}|{exists['h8']}|{exists['h9']}\n
    {exists['i1']}|{exists['i2']}|{exists['i3']}|  |{exists['i4']}|{exists['i5']}|{exists['i6']}|  |{exists['i7']}|{exists['i8']}|{exists['i9']}"""
    print(board)

else:
#complex still doesnt work this method would be very slow anyway if it did work
#I can do about 100000 comb per sec a tough puzzle has about 1329529324032 comb using this method
#number could be wrong on hard puzzle comb
    for char in exists:
        possibilities[char] = [exists[char]]




    for y in possibleLetters:
        addRowsto(y)
    print(len(matching['a']))
    print(len(matching['b']))
    print(len(matching['c']))
    print(len(matching['d']))
    print(len(matching['e']))
    print(len(matching['f']))
    print(len(matching['g']))
    print(len(matching['h']))
    print(len(matching['i']))

    print(combine())


    #print("known")
    #print(exists)
    #print("variables")
    #print(possibilities)
