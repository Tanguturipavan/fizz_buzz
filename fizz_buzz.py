
'''


              FIZZ_BUZZ:
              
              
'''

def fizz_buzz():
    number=int(input("enter any number"))
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
a=fizz_buzz()
print(a)