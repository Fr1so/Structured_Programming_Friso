def pyramidForLoop():
    for star in range(0, 5):
        star += 1
        print(star * '*')

    for epic in range(0, 5):
        star -= 1
        print(star * '*')

pyramidForLoop()

def pyramidWhileLoop():
    row = 0
    end = 5
    while end > row:
        print(row * '*')
        row += 1

    while row > 0:
        print(row * '*')
        row -= 1


pyramidWhileLoop()
