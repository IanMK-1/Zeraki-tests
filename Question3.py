# 3)  A mouse is looking over a river that's 21 feet wide. There are 20 stones placed in 
#     the river 1 foot apart, such that there is 1 foot from the beginning of the river to 
#     the first stone, and 1 foot from the first stone to the next stone, and so on; and 1 foot 
#     from the last stone to the end of the river. The mouse can jump over 1 foot or 2 feet such 
#     that the first step the mouse can make is either from the beginning of the river to the first 
#     stone, or from the beginning of the river to the second stone. If the mouse can't 
#     jump backwards, write a Java function that returns the number of different ways the mouse 
#     can jump from the beginning of the river to the end of the river.

def sequenceIteration(x): 
    if (x == 1): 
        return 1
    elif (x == 2): 
        return 2 
    else : 
        return sequenceIteration(x - 2) + sequenceIteration(x - 1)  
  

print(sequenceIteration(20)) 