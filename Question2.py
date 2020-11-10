# 2)  Given a string S of length N, write a Java function that transforms the string 
#     by reversing characters in groups of four, and returns the transformed string
#     .e.g. when S = 'Lorem at' the output should be 'eroLta m'when S = ' Tempor ip' 
#     the output should be 'meT  roppi' 

def stringTransformation(s):
    splitted_s = list(s)
    reversed_list = []

    for x in range(0,len(splitted_s), 4):
        if x+3 < len(splitted_s):
            y = x+3

            for z in range(y, x-1, -1):
                reversed_list.append(splitted_s[z])
        
        else:
            y = len(splitted_s) - 1
            for z in range(y, x-1, -1):
                reversed_list.append(splitted_s[z])

    return ''.join(reversed_list)


print(stringTransformation(" Tempor ip"))
