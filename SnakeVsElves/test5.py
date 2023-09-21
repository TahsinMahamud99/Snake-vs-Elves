for i in range(25):
    for j in range(42):
        if j == 0:
            print('[', end = '')
        elif j == 41:
            print('],', end = '')

        elif j == 1 or j == 40 or i == 0 or i == 24:
            print('1, ', end = '')
        else:
            print('0, ', end ='')
    print('')