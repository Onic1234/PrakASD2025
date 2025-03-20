def cariLurus( wadah, target ):
    n =len( wadah ) 
    for i in range( n ):
        if wadah[i] == target: 
            return True
    return False

cariLurus( [1,2,3,4,5], 3 )