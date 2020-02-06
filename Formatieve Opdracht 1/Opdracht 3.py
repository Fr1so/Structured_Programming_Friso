#Opdracht 3a

numberList = [-2, -1, 0, 1, 2, 1, 3, 4, 4, 5, 4, 5, 18, 44, 52, 12, 44, 23, 6, 7, 8, 9]

def count():

    x = int(input('Check how often this number shows up the list: '))
    numberTimes = numberList.count(x)
    print('This number shows up', numberTimes, 'time(s) in the list!')

count()

#Opdracht 3b

def biggestDifference():

    numberList.sort()
    differenceNumber = numberList[-1] - numberList[0]
    print('The difference between the smallest and the biggest number in the list is:', differenceNumber)

biggestDifference()

#Opdracht 3c
onesAndZerosList = [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]

def oneAndZero():
    amountOne = onesAndZerosList.count(1)
    amountZero = onesAndZerosList.count(0)

    if amountOne > amountZero:
        print('Amount of one (',amountOne,') is greater than the amount of zero (',amountZero,') in the list.')
    else:
        print('Amount of one (', amountOne, ') is smaller than the amount of zero (', amountZero, ') in the list.')

    if amountZero > 12:
        print('There are more than 12 zeros.')
    else:
        print('There are less than 12 zeros.')

oneAndZero()