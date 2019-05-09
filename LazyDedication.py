import sys

text = ' '.join(sys.argv[1:])
for i in range(0, text.__len__() + 1):
    print(text[0:i])
for i in range(text.__len__() - 1, 0, -1):
    print(text[0:i])