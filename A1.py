def getMaxLen(a):
    c = 0
    mmax = 0
    for i in range(len(a)):
        if a[i] == 0: c = 0
        else:
            c+=1 
            mmax = max(mmax, c)

    return mmax

a = [1,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,0]
print(getMaxLen(a))