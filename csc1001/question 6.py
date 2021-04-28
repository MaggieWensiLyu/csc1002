import random
def display(chess):                 
        for i in chess:
            print(" ".join(i))

def availC(lastC):
    column = []
    if lastC == 0 or lastC == 1:                    #special case on the first two column
        for i in range(lastC+2,8):
            column.append(i)
    elif lastC == 6 or lastC == 7:                   #last two column
        for j in range(0,lastC-1):
            column.append(j)
    else:
        for k in range(lastC+2,8):
            column.append(k)
        for h in range(0,lastC-1):
            column.append(h)
    return column

def eachRow(row,column):
    columnChange = random.choice(column)
    chess[row][columnChange] = "|Q"              #switch the "| " to "|Q" to display the Q
    return chess

chess = [                                                   #use list to display the chess as there is row and column
          ["|Q","| ","| ","| ","| ","| ","| ","| ","|"],
          ["| ","| ","| ","| ","| ","| ","| ","| ","|"],
          ["| ","| ","| ","| ","| ","| ","| ","| ","|"],
          ["| ","| ","| ","| ","| ","| ","| ","| ","|"],
          ["| ","| ","| ","| ","| ","| ","| ","| ","|"],
          ["| ","| ","| ","| ","| ","| ","| ","| ","|"],
          ["| ","| ","| ","| ","| ","| ","| ","| ","|"],
          ["| ","| ","| ","| ","| ","| ","| ","| ","|"]
]

lastC = 0
row = 1
while row <= 7:
    column = availC(lastC)
    if len(column) == 0:
        row -= 1                                          #if there is no choice, return to the last row to choose again
        lastC = chess[row-1].index("|Q")                  
    else:
       chess = eachRow(row,column) 
       lastC = chess[row].index("|Q")                    # make the current column the "lastC" for next step
       row += 1


display(chess)