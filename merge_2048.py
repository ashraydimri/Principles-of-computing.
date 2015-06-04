"""
Merge function for 2048 game.
"""
def sorting(lst):
    """
    This is used to sort the at hand list.
    """
    for index in range(len(lst)):
        for index_index in range(len(lst)-1):
            if lst[index_index]==0 and index!=len(lst)-1:
                lst[index_index]=lst[index_index+1]
                lst[index_index+1]=0
    return lst            
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    beta=line[:]
    lit=sorting(beta)
    
    # replace with your code
    for index in range(len(lit)-1):
        if lit[index]==lit[index+1]:
            lit[index]=lit[index+1]+lit[index]
            lit[index+1]=0
    last=sorting(lit)
    if lit!=last:
        merge(last)
    else:
        return last
