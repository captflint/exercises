path = input("Count words in which file? ")
with open(path, 'rt') as infile:
    document = infile.read()
whitespace = "\t \n"
isWord = False
wordcount = 0
for char in document:
    if isWord:
        if char in whitespace:
            isWord = False
        else:
            continue
    else:
        if char not in whitespace:
            wordcount += 1
            isWord = True
        else:
            continue
print(wordcount)
