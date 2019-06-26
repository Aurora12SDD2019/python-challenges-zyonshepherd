#6

word = str(input('What is your word? '))

wordBackwards = word[::-1]

if word == wordBackwards:
    print('Word is a palindrome')
else:
    print('Word is not the same backwards')