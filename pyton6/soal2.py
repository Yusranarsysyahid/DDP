hasil = 0
for i in range(1, 20, 2):
    hasil += i 
    print(i, end=" ")
    if i != 19:
        print("+", end=" ")
print('=', hasil)