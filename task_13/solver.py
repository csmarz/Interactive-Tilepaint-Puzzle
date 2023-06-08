from pysat.solvers import Glucose3
from pysat.formula import CNF
from pysat.card import *
import itertools

m = 0
n = 0

def h(i, j):
    return i*n + j + 1

def atMost(A, k):
    combi = list(itertools.combinations(A, k+1))
    combi_list = [[*a] for a in combi]
    combi_neg = [[-a for a in combi] for combi in combi_list]

    return combi_neg

def atLeast(A, k):
    return atMost([-a for a in A], len(A) - k)

def equals(A, k):
    cnf = []
    atleast, atmost = [*atLeast(A, k)], [*atMost(A, k)]
    if len(atleast) != 0:
        cnf.append(atleast)
    if len(atmost) != 0:
        cnf.append(atmost)
    
    return cnf

def phi_1(R, p):
    cnf = []
    for k in range(1, p+1):
        for i in range(len(R[k])):
            for j in range(i+1, len(R[k])):
                cnf.append([-1 * h(R[k][i][0], R[k][i][1]), h(R[k][j][0], R[k][j][1])])
                cnf.append([h(R[k][i][0], R[k][i][1]), -1 * h(R[k][j][0], R[k][j][1])])

    # print(cnf)
    return cnf

def phi_2(cc):
    cnf = []
    for j in range(n):
        if (cc[j] != -1):
            lits = []
            for i in range(m):
                lits.append(h(i,j))
            cnf.extend(equals(lits, cc[j]))

    return cnf

def phi_3(cr):
    cnf = []
    for i in range(m):
        if (cr[i] != -1):
            lits = []
            for j in range(n):
                lits.append(h(i,j))
            cnf.extend(equals(lits, cr[i]))

    return cnf

def solve(M, N, CG, CC, CR):
    # print(CG)
    global m
    global n

    m = M
    n = N

    MaxT = 0
    for i in range(len(CG)):
        MaxT = max(MaxT, max(CG[i]))
    R = [[] for _ in range(MaxT+1)]

    for i in range(M):
        for j in range(N):
            R[CG[i][j]].append((i, j))

    for i in range(M):
        if (CR[i] > N):
            return {'Model': None}

    for j in range(N):
        if (CC[j] > M):
            return {'Model': None}

    s = Glucose3()

    s.append_formula(phi_1(R, MaxT))
    for item in (phi_2(CC)) :
        s.append_formula(item)
    for item in (phi_3(CR)) :
        s.append_formula(item)

    s.solve()
    model = s.get_model()

    return {'Model': model}