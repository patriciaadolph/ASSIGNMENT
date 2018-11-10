import re
def rect_frame(words):
    length = max(len(word) for word in words)
    print('*' * (length + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=length))
    print('*' * (length + 4))

str=input("Enter the string:")
reg=re.compile('^[\.]+$')
if all(x.isalpha() or x.isspace() or reg.match(x) for x in str):
    words = str.split()
    rect_frame(words)
else:
    print("Please Enter a valid input by avoiding special characters and numbers")