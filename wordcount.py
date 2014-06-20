path = input("Count words in which file? ")
with open(path, 'rt') as infile:
    document = infile.read()
whitespace = "\t \n"
isWord = False
wordcount = 0
for char in document:
    if isWord and char in whitespace:
        isWord = False
    else:
        if char not in whitespace:
            wordcount += 1
            isWord = True
print(wordcount)
