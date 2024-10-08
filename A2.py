def pushZeros(a, end=True):
    z = 0
    non = 0

    if end:
        while non != len(a):
            if a[non] != 0:
                a[non], a[z] = a[z], a[non]
                z += 1
            non += 1
    else:
        while non != len(a):
            if a[non] != 0:
                a[non], a[z] = a[z], a[non]
                z += 1
            non += 1

a = [0, 3, 5, 6, 2, 3, 0, 2, 0, 5, 6, 0, 4, 7]
print(a)
pushZeros(a, True)
print(a)
pushZeros(a, False)
print(a)