rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(val, end =" ")
        val += 1
        if val > 5:
            val = 0
        print(val)