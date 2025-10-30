i = 1
while i < 101:
    if i % 2 == 0 and i % 5 == 0:
        print("2와 5의 배수입니다.")
    elif i % 2 == 0:
        print("2의 배수입니다.")
    elif i % 5 == 0:
        print("5의 배수입니다.")
    else:
        print(str(i))
    i += 1