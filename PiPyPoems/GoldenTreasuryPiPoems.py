# import stuff 
import pandas
import random

# create pandas dataframe from the poem CSV
poemDF = pandas.read_csv('GoldenTreasuryLines.csv')
# create list with digits of Pi
piDigits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4]

# create a random poem based on digits of Pi
# first decide number of lines in the poem, 
# I based this on the approximate range observed in the original corpus.		
poemLength = random.randrange(5,60)

# start the author variable, other authors will be added by the loop.
author = 'Pi Py Poetry'

# create a poem of the random length,
# the digits of Pi are the number of words per line.
for i in range(poemLength):
    if piDigits[i] == 0:
        print("\n")
    else: 
        newLine = poemDF[poemDF['words'] == piDigits[i]].sample()
        author += ', ' + newLine.values[0][0]
        line = newLine.values[0][1]
        print(line)
print('\nBy '+author)