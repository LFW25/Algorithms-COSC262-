### Assignment 1 ###
### Lily Williams ###
## 42415299, lfw25 ##
# May 2021 #

#import numpy as np
##### Question 1 #####
"""
>>> s1 = 'butts'
>>> s2 = 'but'
>>> print(lcs(s1, s2))
but

>>> s1 = "Look at me, I can fly!"
>>> s2 = "Look at that, it's a fly"
>>> print(lcs(s1, s2))
Look at ,  a fly

>>> s1 = "abcdefghijklmnopqrstuvwxyz"
>>> s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
>>> print(lcs(s1, s2))
<BLANKLINE>

>>> s1 = "balderdash!"
>>> s2 = "balderdash!"
>>> print(lcs(s1, s2))
balderdash!

>>> s1 = 1500 * 'x'
>>> s2 = 1500 * 'y'
>>> print(lcs(s1, s2))
<BLANKLINE>
"""
def lcs(s1, s2):
    """ 
    Bottom-up DP approach to the longest common substring (LCS) problem
    Must be iterative
        Inputs:
            s1 - the first string to be compared
            s2 - the second string to be compared

        Outputs:
            Returns the longest common substring to both strings
    
    
        Plan:
        - Create a table according to:
                        0                                   i = 0 or j = 0
            L[i][j] =   L[i-1][j-1] + 1                     s1[i] = s2[j]
                        max(L[i][j-1], L[i-1][j])           s1[i] != s2[j]
        - Backtrack down the table to find the LCS
    """

    m = len(s1)
    n = len(s2)
  
    table = [[0]*(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                table[i][j] = 0

            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1]+1

            else:
                table[i][j] = max(table[i-1][j] , table[i][j-1])

    lcs_string = ''

    a = len(s1)
    b = len(s2)

    while a > -1 and b > -1:
        if table[a][b] == table[a][b-1]:
            b -= 1
        elif table[a][b] == table[a-1][b]:
            a -= 1
        else:
            a -= 1
            b -= 1
            lcs_string += s1[a]
    
    return lcs_string[::-1]

##### Question 3 #####
def line_edits(s1, s2):
    """ 
    Uses a BOTTOM-UP edit_distance algorithm, with whole lines as the comparison elements,
    to determine which lines to delete, insert, alter (substitute), or just copy.
        Inputs:
            s1 - the previous version of the program
            s2 - the current version of the program

        Outputs:
            Returns an (operation, left_line, right_line) tuple
            that corresponds line-for-line with the output table.
                operation - has the value C, S, D, or I for Copied,
                                Substituted, Deleted, and Inserted.
                left-line - contents of the left table cells,
                                empty for 'I' operations.
                right_line - contents of the right table cells,
                                empty for 'D' operations.
    
    
        Plan:
        - Create a table according to:
                        0                                   i = 0 or j = 0
            L[i][j] =   L[i-1][j-1] + 1                     s1[i] = s2[j]
                        max(L[i][j-1], L[i-1][j])           s1[i] != s2[j]
        - Backtrack down the table to find the LCS
    """
    prev, curr = s1.splitlines(), s2.splitlines()

    for lists in [prev, curr]:
        if len(lists) == 0 and not (len(s1) == len(s2) == 0):
            lists.append('')

    m, n = len(prev), len(curr)
  
    table = [[0]*(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if j == 0 or i == 0:
                table[i][j] = i + j

            elif prev[i - 1] == curr[j - 1]:
                table[i][j] = table[i - 1][j - 1]

            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])

    return backtrack(table, (m, n), (prev, curr), (s1, s2))

def backtrack(table, mn, prevcurr, s1s2):
    """
    Backtracks through the table
    to reconstruct the correct methods
    """
    m, n = mn[0], mn[1]
    prev, curr = prevcurr[0], prevcurr[1]
    s1, s2 = s1s2[0], s1s2[1]
    edits = []

    while m >= 0 and n >= 0 and len(edits) <= len(s1) and len(edits) <= len(s2):
        if m-1 >= 0 and n-1 >= 0 and prev[m - 1] == curr[n - 1]:
            edits.append(('C', prev[m - 1], curr[n - 1]))
            m, n = m - 1, n - 1

        else:
            if m-1 < 0 and n-1 < 0:
                break

            elif (m-1 < 0 and n-1 >= 0) or len(prev[m-1]) == 0:
                diag = [float('inf')]
                left = [table[m][n-1], ('I', '', curr[n - 1]), 0, 1]
                up = [float('inf')]

            elif (m - 1 >= 0 and n-1 < 0) or len(curr[n-1]) == 0:
                    
                diag = [float('inf')]
                left = [table[m][n-1], ('I', '', curr[n - 1]), 0, 1]
                up = [table[m-1][n], ('D', prev[m - 1], ''), 1, 0]
                
            else:
                diag = [table[m-1][n-1], ('S', prev[m - 1], curr[n - 1]), 1, 1]
                up = [table[m-1][n], ('D', prev[m - 1], ''), 1, 0]
                left = [table[m][n-1], ('I', '', curr[n - 1]), 0, 1]

            min_move = min(diag, up, left, key = lambda x: x[0])

            if min_move == diag:
                commons = lcs(prev[m - 1], curr[n - 1])
                line1, line2 = common_highlights(prev[m - 1], curr[n - 1], commons)
                min_move = [table[m-1][n-1], ('S', line1, line2), 1, 1]

            edits.append(min_move[1])
            m, n = m - min_move[2], n - min_move[3]
            
                   
    return edits[::-1]

def common_highlights(line1, line2, common):
    """
    Takes the two lines
    puts the not common letters in double square brackets
    [[]]
    and returns them to backtracking to be appended
    """
    new_lines = []
    nline1 = []
    nline2 = []
    common_local1 = list(common)
    common_local2 = list(common)


    for i in range(0, len(line1)):
        char = line1[i]

        if len(common_local1) > 0 and common_local1[0] == char:

            nline1.append(common_local1[0])
            common_local1.pop(0)
                
        else:
            nline1.append('[[' + char + ']]')

    new_lines.append(nline1)
    


    for i in range(0, len(line2)):
        char = line2[i]

        if len(common_local2) > 0 and common_local2[0] == char:

            nline2.append(common_local2[0])
            common_local2.pop(0)
                
        else:
            nline2.append('[[' + char + ']]')

    new_lines.append(nline2)

    s = ''
    line1, line2 = s.join(new_lines[0]), s.join(new_lines[1])
    return line1, line2

def lcs(s1, s2):
    """
    Identifies the longest common subsequence
    between 2 strings
    """

    m = len(s1)
    n = len(s2)
  
    table = [[0]*(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                table[i][j] = 0

            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1]+1

            else:
                table[i][j] = max(table[i-1][j] , table[i][j-1])

    lcs_string = ''

    a = len(s1)
    b = len(s2)

    while a > -1 and b > -1:
        if table[a][b] == table[a][b-1]:
            b -= 1
        elif table[a][b] == table[a-1][b]:
            a -= 1
        else:
            a -= 1
            b -= 1
            lcs_string += s1[a]
    
    return lcs_string[::-1]

s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)

# ('S', 'Line[[1]]', 'Line[[5]]')
# ('S', '[[L]]ine[[ ]]2[[a]]', '[[l]]ine2')
# ('C', 'Line3', 'Line3')
# ('D', 'Line4', '')

# s1 = "Line1\nLine2\nLine3\nLine4\n"
# s2 = "Line1\nLine3\nLine4\nLine5\n"
# table = line_edits(s1, s2)
# for row in table:
#    print(row)

# # ('C', 'Line1', 'Line1')
# # ('D', 'Line2', '')
# # ('C', 'Line3', 'Line3')
# # ('C', 'Line4', 'Line4')
# # ('I', '', 'Line5')

# print('----------------------------')
# s1 = "Line1\nLine2\nLine3\nLine4\n"
# s2 = "Line5\nLine4\nLine3\n"
# table = line_edits(s1, s2)
# for row in table:
#    print(row)
# # ('S', 'Line1', 'Line5')
# # ('S', 'Line2', 'Line4')
# # ('C', 'Line3', 'Line3')
# # ('D', 'Line4', '')

# print('----------------------------')	
# s1 = "Line1\n"
# s2 = ""
# table = line_edits(s1, s2)
# for row in table:
#     print(row)
# # ('D', 'Line1', '')

# print('----------------------------')
# s1 = ""
# s2 = "Line1\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)
# # ('I', '', 'Line1')

# print('----------------------------')
# s1 = "Line1\nLine3\nLine5\n"
# s2 = "Twaddle\nLine5\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)
# # ('D', 'Line1', '')
# # ('S', 'Line3', 'Twaddle')
# # ('C', 'Line5', 'Line5')

# print('----------------------------')
# s1 = ""
# s2 = ""
# table = line_edits(s1, s2)
# for row in table:
#     print(row)
# #

# print('----------------------------')
# s1 = "a\n"
# s2 = "b\nc\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)
# # ('I', '', 'b')
# # ('S', 'a', 'c')