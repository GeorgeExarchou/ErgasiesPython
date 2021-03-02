
file = input("give an ascii file")

for j in range(len(file)):
    letter = file[len(file)-j -1]
    num1 = ord(letter)
    num2 = 128 - num1 # katoptrikos
    ascii = chr(num2)

    print(ascii , end ="")
