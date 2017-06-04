f = []

for i in range(100):
    if i == 0:
        f[i] = 0
    elif i == 1:
        f[i] = 1
    else:
        f[i] = f[i-1] + f[i-2]
    print(f[i])
