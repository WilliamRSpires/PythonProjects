
string = input("Enter your string: ")
stringReversed = string[::-1]
if string==stringReversed:
    print(string + ' is a Palindrome')
else:
    print(string + ' is not a Palindrome')
