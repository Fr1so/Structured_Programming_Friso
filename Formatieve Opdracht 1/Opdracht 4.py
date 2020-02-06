def palindrome():
    normalWord = str(input('Check if this word is a palindrome: '))

    if normalWord == normalWord[::-1]:
        print(normalWord, 'is a palindrome!')
    else:
        print(normalWord, 'is not a palindrome!')

def palindromeLibrary():

    normalWord = str(input('Check if this word is a palindrome: '))
    reversedWord = "".join(reversed(normalWord))

    if normalWord == reversedWord:
        print(normalWord, 'is a palindrome!')
    else:
        print(normalWord, 'is not a palindrome!')

palindrome()
palindromeLibrary()