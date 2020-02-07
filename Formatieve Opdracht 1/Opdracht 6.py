#Bron: 3e-jaars student KI aan de UU (ookal werkt het nog steeds niet)

import statistics

numberList = [0, 1, 3, 3, 51, 2, 33, 2, 1, 44, 2, 3, 6, 4, 8, 8, 9, 3, 6, 45, 8, 456, 8]

def average():
    averageNumbers = statistics.mean(numberList)
    print(averageNumbers)

average()

def averageInput():
    #averageInputList = []
    loLists = input('Input the list of lists (numbers only): ')
    loAverage = []
    for i, l in enumerate(loLists):
        average = 0
        for elem in l:
            if type(elem) == int:
                average += elem
                print(elem)


        average /= len(l)
        loAverage.append(average)
        print("Average of list no. " + str(i) + ": " + str(average))
    print("Average of all lists:" + statistics.mean(loAverage))




    '''while True:
        averageInputNumbers = int(input('Input list of numbers: '))
        averageInputList.append(averageInputNumbers)
        if averageInputNumbers == '':
            return (statistics.mean(averageInputList))'''

averageInput()