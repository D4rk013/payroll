for i in range(0,5):
    for j in range(0,i+1):
        print('* ',end=' ')
    print()

#star
k = 1
for i in range(0,5):
    for j in range(0,k):
        print('*', end=' ')
    k = k+2
    print()
    
#star new pattern
k = 8
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()

#new pattern
k = 0
rows = 5
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()