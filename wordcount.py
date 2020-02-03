# put your code here.
#import test.txt
#import twain.txt


words = {}

def word_count(file):
    file = open(file).read()
    file = file.lower()
    file.strip('?' '.')
    print(file)
    file = file.split()
    for word in file:
        words[word] = words.get(word, 0) + 1

    return words

print(word_count('test.txt'))
