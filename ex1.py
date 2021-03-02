
import random
x = int(input("give square's side "))
y = x**2
if y % 2 == 1:
    pos = round(y/2) + 1
else:
    pos =  round(y/2)
sum = 0
for z in range (100):
    numbers=[0,1]
    n1 = 0
    n0 = 0
    table = []
    for i in range (x):
        list=[]
        for j in range (x):
            number = random.choice(numbers)
            if number == 1 and n1 < pos:
                list.append(number)
                n1 = n1 + 1
            elif number == 0 and n0 < y - pos:
                list.append(number)
                n0 = n0 + 1
            elif n1 == pos:
                    list.append(0)
            elif n0 == y - pos:
                    list.append(1)
        table.append(list)
    orizontia = 0
    katheta = 0
    diagwnia = 0
    for i in  range(x):
        o = 0
        for j in range(x):
            if table[i][j] == 1:
                o = o + 1
                if o == 4:
                   orizontia = orizontia + 1
            else:
                o = 0
    for i in  range(x):
        k = 0
        for j in range(x):
            if table[j][i] == 1:
                k = k + 1
                if k == 4:
                   katheta = katheta + 1
            else:
                k = 0
    for i in range(x):
        for j in range(x):
            if i == x -4 and j == x - 4:
                if table[i][j] == table[i+1][j+1] and table[i][j] == table[i+2][j+2] and table[i][j] == table[i+3][j+3] and table[i][j]==1:
                     diagwnia = diagwnia + 1
                if table[i][j] == table[i+1][j-1] and table[i][j] == table[i+2][j-2] and table[i][j] == table[i+3][j-3] and table[i][j]==1:
                    diagwnia = diagwnia + 1
    sum = sum + orizontia + katheta + diagwnia
mo = sum /100
print(mo)
