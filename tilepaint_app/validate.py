m = 0
n = 0

def isSumEqual(CC, CR):
    sum_row, sum_col = 0, 0
    for item in CC:
        if (item == -1):
            return True
        sum_col += item

    for item in CR:
        if (item == -1):
            return True
        sum_row += item

    return sum_col == sum_row

def complyConstraint(Cell, CC, CR, m, n): 
    coloredCol, coloredRow = [0 for _ in range(n)], [0 for _ in range(m)]

    cr, cc = [], []

    for i in range(m):
        for j in range(n):
            if (Cell[i][j] == 1):
                coloredCol[j] += 1
                coloredRow[i] += 1

    for j in range(n) :
        if (CC[j] != -1 and coloredCol[j] != CC[j]) :
            cc.append(j+1)

    for i in range(m) :
        if (CR[i] != -1 and coloredRow[i] != CR[i]) :
            cr.append(i+1)

    return len(cc) == 0 and len(cr) == 0, cc, cr

def IsAllSame(CG, Cell, m, n, p):
    colored, cellTotal = [0 for _ in range(p+1)], [0 for _ in range(p+1)]

    for i in range(m):
        for j in range(n):
            cellTotal[CG[i][j]] += 1
            if (Cell[i][j] == 1):
                colored[CG[i][j]] += 1
        
    for i in range(1, p+1):
        if (colored[i] != cellTotal[i] and colored[i] != 0):
            return False

    return True

def color(CG, Cell, t, c):
    for i in range(len(CG)):
        for j in range(len(CG[i])):
            if (CG[i][j] == t) :
                Cell[i][j] = c

def validate(M, N, CG, S, CC, CR):
    MaxT = 0
    for i in range(len(CG)):
        MaxT = max(MaxT, max(CG[i]))
    
    Cell = [[0 for _ in range(N)] for _ in range(M)]

    for item in S:
        color(CG, Cell, item, 1)

    rule1 = isSumEqual(CC, CR)
    rule2 = IsAllSame(CG, Cell, M, N, MaxT)
    rule3, cc, cr = complyConstraint(Cell, CC, CR, M, N)

    # print(rule1, rule2, rule3)

    return {'Model': rule1 and rule2 and rule3, "cc": cc, "cr": cr}