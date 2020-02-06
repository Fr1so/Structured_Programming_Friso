#Bron: https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
'''Schrijf een compress-programma, dat uit een gegeven bestand een nieuwe bestand maakt,
waarbij van iedere regel alle spaties en tabs aan het begin van de regel zijn verwijderd.
Verder zijn alle lege regels verwijderd (een lege regel bevat ’\n’ , eventueel voorafgegaan door spaties en tabs(‘\t’)).'''


def compression():
oldFile = open('oldFile.txt', 'r')