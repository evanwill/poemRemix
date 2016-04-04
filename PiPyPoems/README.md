# Pi Py Poetry: Pi Day Remix 

> Its 3:14 on 3/14 (2016)! You love the Sonnet and the Haiku, but how about the wonderful new form, the Pi Poem?

To honor Pi Day, I played around with Python to remix poetry following the digits of Pi. This example uses public domain poetry to create some classical Pi Poems. I originally worked with poems from [Vandal Poem of the Day](http://poetry.lib.uidaho.edu/) project shared in this [Gist](https://github.com/evanwill/poemRemix/blob/master/PiPyPoems/PiPoemsVPOD.md).

## Create GoldenTreasuryLines.csv

To create Pi based poetry, I wanted a csv with the author, lines of poetry, and number of words in the line. How can we take a book and make it into data?

> THE GOLDEN TREASURY

> Of the best Songs and Lyrical Pieces, In the English Language

> Selected by Francis Turner Palgrave, 1861

> [Project Gutenberg EBook #19221](http://www.gutenberg.org/ebooks/19221)

I created the poem CSV using [OpenRefine](https://github.com/OpenRefine/OpenRefine) to parse [HTML text](http://www.gutenberg.org/ebooks/19221) from Project Gutenberg.
Since there is no markup other than `<pre>` tags, parsing was mostly achieved using regular expressions. The poem text has the title in all caps at the beginning and the author in all caps at the end. These patterns can be targeted with regex to create separate title, author, and poem columns. For this use, I removed the title column. 

Next, I want to split the poem column into a row for each line, usually achieved in OpenRefine with split multi-valued cells. However, this function will not split cells with a separator of \n. Thus, I first transform cells > `value.replace('\n','$$')` then split multivalued cells on `$$`.

I fill down on the author column to fill in the blanks. Then facet poem column on blank, and remove all blank rows. This gives us 10,014 lines of poetry from 78 different authors to work with. 

Next, I add a new column 'words' based on poem using `length(value.ngram(1))`. This counts the number of words in each line. 
Then I add a new column 'characters' based on poem using `length(value)`. This gives a character count for each line. 

The final csv has the columns `author,poem,words,characters` and only includes lines with 1 to 9 words. It is included in this repository as `GoldenTreasuryLines.csv`. More complete files can be found in [GoldenTreasury](https://github.com/evanwill/poemRemix/tree/master/GoldenTreasury).

## Python for Poems 

To simplify creating Pi poems I used the Python modules random and pandas. The poem loop iterates over the digits of Pi to choose a random line of the correct length. Since we have a nice structured poetry data set already set up, this process is fairly simple.
Information is available in the comments of `GoldenTreasuryPiPoems.py`.

## Examples

Some Pi Py Poems can be found in [PiPoems.md](https://github.com/evanwill/poemRemix/blob/master/PiPyPoems/PiPoems.md).
