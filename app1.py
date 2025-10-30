for x in range(1, 101):
    # 2의 배수이면서 5의 배수인 경우
    if x % 2 == 0 and x % 5 == 0:
        print(f"{x}는 2와 5의 배수입니다.")
    # 2의 배수인 경우
    elif x % 2 == 0:
        print(f"{x}는 2의 배수입니다.")
    # 5의 배수인 경우
    elif x % 5 == 0:
        print(f"{x}는 5의 배수입니다.")
    # 그 외
    else:
        print(x)
