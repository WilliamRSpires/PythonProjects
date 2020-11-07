L=list(range(1,100))
for num in L:
    if num % 15==0:
        print('FizzBuzz')
    elif num % 5==0:
        print('Buzz')
    elif num % 3==0:
        print('Fizz')
    else:
        print(num)
