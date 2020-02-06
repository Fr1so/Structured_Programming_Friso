def indexCheck():

    string1 = str(input('Input a string: '))
    string2 = str(input('Input a string: '))
    index = 0
    if len(string2) >= len(string1):
        for firstCharacter in string1:
            while firstCharacter != string2[index]:
                print('The first difference is at index:', str(index))
                break
            else:
                index += 1
                print('help')


indexCheck()