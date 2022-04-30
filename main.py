def find_kaprekar_constant(val):

    if val < 100 or val > 9999:
        raise ValueError ('must be between 100 and 9999')

    if len(set(map(int, str(val)))) < 2:
        raise ValueError ('at least two digits should have different')


    val_1 = val

    for i in range(1,20):

        print(f'iter: {i}')

        val_1 = int("".join(sorted(str(val_1),reverse=True)))
        if val >= 1000 and len(str(val_1)) == 3:
            val_1 = val_1 * 10
        if val < 1000 and len(str(val_1)) == 2:
            val_1 = val_1 * 10

        print(f'val_1: {val_1}')
        val_2 = str(val_1)[::-1]
        val_2 = int(val_2)
            
        print(f'reverse: {val_2}')

        val_1 = abs(val_1 - val_2)

        print(f'new val_1: {val_1}')
        if val >= 1000 and val_1 == 6174:
            print(f'I found it in iter {i}...')
            break

        if val < 1000 and val_1 == 495:
            print(f'I found it in iter {i}...')
            break

find_kaprekar_constant(1000)
