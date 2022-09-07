cache = {}

def lcs(s1, s2):
    if s1 == '' or s2 == '':
        return ''

    elif (s1, s2) in cache:
        return cache[(s1, s2)]

    else:
        if s1[-1] == s2[-1]:
            cache[(s1, s2)] = lcs(s1[:-1], s2[:-1]) + s1[-1]

        else:
            sol_1 = lcs(s1[:-1], s2)
            sol_2 = lcs(s1, s2[:-1])

            if len(sol_1) > len(sol_2):
                cache[(s1, s2)] = sol_1

            else:
                cache[(s1, s2)] = sol_2
        return cache[(s1, s2)]