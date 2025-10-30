<<<<<<< HEAD
i = 100
while i > 0:
    j = i // 10
    k = i % 10
    if (j % 3 == 0 and j != 0) and (k % 3 == 0 and k != 0):
        print("짝짝")
    elif (j % 3 == 0 and j != 0) or (k % 3 == 0 and k != 0):
        print("짝")
    else:
        print(str(i))
    i -= 1

for i in range(100, 0, -1):
    s = str(i)
    clap = s.count('3') + s.count('6') + s.count('9')
    print('짝'*clap if clap else i)
=======
for i in range(100, 0, -1):
    s = str(i)
    clap = s.count('3') + s.count('6') + s.count('9')
    print('짝'*clap if clap else i) 

>>>>>>> b1293880c61471947111177009670c64f7237345
