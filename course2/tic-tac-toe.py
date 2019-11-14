import random
Map = InitMap = [['_', '_', '_'],
                ['_', '_', '_'],
                ['_', '_', '_'],]
moves = 0
while 1:
    while 1:
        lin_col = input("Introdu o pozitie de forma <linie> <coloana>. \n")
        lin_col = lin_col.split(" ")
        lin = lin_col[0]
        col = lin_col[1]
        if ((not lin.isdigit()) or (not col.isdigit()) or int(lin) > 2
                or int(col) > 2 or int(lin) < 0 or int(col) < 0 or Map[int(lin)][int(col)] != '_'):
            print("Introdu o pozitie valida.")
        else:
            Map[int(lin)][int(col)] = 'X'
            moves = moves + 1
            break

    for i in Map:
        for j in i:
            print(" " + j + " ", end='')
        print ("")
    for i in Map:
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            print("X a castigat!")
            break
    for i in range(0, 2):
        if Map[0][i] == Map[1][i] == Map[2][i] == 'X':
            print("X a castigat!")
            break
    if Map[0][0] == Map[1][1] == Map[2][2] == 'X':
        print("X a castigat!")
        break
    if Map[0][2] == Map[1][1] == Map[2][0] == 'X':
        print("X a castigat!")
        break
    if moves == 9:
        print("Remiza.")
        break
    while 1:
        lin_O = random.randint(0, 2)
        col_O = random.randint(0, 2)
        if Map[lin_O][col_O] == '_':
            ++moves
            break
    print("Mutarea adversarului:")
    Map[lin_O][col_O] = 'O'
    for i in Map:
        for j in i:
            print(" " + j + " ", end='')
        print ("")
    for i in Map:
        if i[0] == i[1] == i[2] == 'O':
            print("O a castigat!")
            break
    for i in range(0, 2):
        if Map[0][i] == Map[1][i] == Map[2][i] == 'O':
            print("O a castigat!")
            break
    if Map[0][0] == Map[1][1] == Map[2][2] == 'O':
        print("O a castigat!")
        break
    if Map[0][2] == Map[1][1] == Map[2][0] == 'O':
        print("O a castigat!")
        break


