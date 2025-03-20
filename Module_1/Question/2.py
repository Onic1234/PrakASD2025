def gambarlahPersegiEmpat(a,b):
    for i in range(a):
        if i == 0 or i == a-1:
            print("@"*b)
        else:
            print("@"+" "*(b-2)+"@")
            
gambarlahPersegiEmpat(4,5)            