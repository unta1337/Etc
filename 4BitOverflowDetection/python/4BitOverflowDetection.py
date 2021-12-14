# %% Genorate strings of binary numbers between 0 and 15.
binListString = []
for i in range(16):
    temp = str(bin(i))
    temp = temp[2:].zfill(4)
    binListString.append(temp)

# %% Convert binary number strings into integer type.
binList = [[] * 4 for _ in range(16)]
for i in range(16):
    for j in range(4):
        # Reverse the order of digits; consider the most singificant bit.
        binList[i].append(int(binListString[i][3 - j]))

# %% Get carries of 4-bit input; default carry input is 0.
def getCarry(X, Y, carryIn = 0):
    C = [carryIn]
    for i in range(4):
        term1 = binList[X][i] & binList[Y][i]
        term2 = binList[X][i] ^ binList[Y][i]
        result = term1 | term2 & C[i]
        C.append(result)
    return C

# %% Function for getting sums of 4-bit input; default carry input is 0.
def getSum(X, Y, carryIn = 0):
    C = getCarry(X, Y, carryIn)
    S = []
    for i in range(4):
        term1 = binList[X][i] ^ binList[Y][i] ^ C[i]
        S.append(term1)
    return S

# %% Function for logical negation of X.
def neg(X):
    return 0 if X else 1

# %% Function of statement for overflow detection.
def OFD(X, Y, carryIn = 0):
    C = getCarry(X, Y, carryIn)
    S = getSum(X, Y, carryIn)
    term1 = neg(binList[X][3]) & neg(binList[Y][3]) & S[3]
    term2 = binList[X][3] & binList[Y][3] & neg(S[3])
    result = term1 | term2
    return result

# %% Function for signed 4-bit decimal.
def signed4(X):
    return X - 16 if X > 7 else X

# %% Function for printing binary expression of a number.
def printBin(X):
    for i in range(4):
        # Consider the bits are reversed.
        print(binList[X][3 - i], end = '')
    print()

# %% Function for evaluating statements and store its values.
# Function for data frame printing.
def evaluateStatement(function):
    result = [[0] * 16 for i in range(16)]
    for i in range(16):
        for j in range(16):
            term1 = binListString[i] + '(' + str(signed4(i)) + ')'
            term2 = binListString[j] + '(' + str(signed4(j)) + ')'
            term3 = str(signed4(i + j))
            term4 = '[' + str(function(i, j)) + ']'
            temp = term1 + ' + ' + term2 + ' = ' + term3 + term4
            result[i][j] = temp
    return result

# Function for .csv export.
def evaluateStatementWithEnter(function):
    result = [[0] * 16 for i in range(16)]
    for i in range(16):
        for j in range(16):
            term1 = binListString[i] + '(' + str(signed4(i)) + ')'
            term2 = binListString[j] + '(' + str(signed4(j)) + ')'
            term3 = str(signed4(i + j))
            term4 = '[' + str(function(i, j)) + ']'
            temp = term1 + '\n' + term2 + '\n' + term3 + term4
            result[i][j] = temp
    return result

# %% Import pandas to print result.
from pandas import *

# %% Genorate a table with pandas data frame.
resultDataFrame = DataFrame(evaluateStatement(OFD))
resultDataFrame

# %% Export result data frame as .csv.
resultOut = DataFrame(evaluateStatementWithEnter(OFD))
resultOut.to_csv('result.csv')
