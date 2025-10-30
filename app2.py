for i in range(100, 0, -1):
    s = str(i)
    clap = s.count('3') + s.count('6') + s.count('9')
    print('짝'*clap if clap else i) 
