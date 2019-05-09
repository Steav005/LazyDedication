import sys

text = ' '.join(sys.argv[1:])
for i in range(0, text.__len__()):
    if text[i - 1] is not ' ': print(text[0:i])
for i in range(text.__len__(), 0, -1):
    if text[i - 1] is not ' ': print(text[0:i])