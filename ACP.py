a = [0,2,0,2,2,1,2,1,0,1,2,0,1,1,0,2,0,2,1,0]
zeros, ones, twos, final = [], [], [], []

for i in a:
    if i == 0: zeros.append(i)
    elif i == 1: ones.append(i)
    elif i == 2: twos.append(i)
for i in zeros: final.append(i)
for i in ones: final.append(i)
for i in twos: final.append(i)

print(a)
print(final)