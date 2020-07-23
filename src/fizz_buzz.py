# class FizzBuzz:

def fizz_buzz(num):
    if (num % 3 ==0 and num % 5==0):
        return "FizzBuzz"
    if(num % 3 == 0):
        return "Fizz"
    if (num % 5 ==0):
        return "Buzz"
    else:
        return str(num)
    # string=""
    # if (num % 3 == 0):
    #     string=string+"Fizz"

    # if(num %5==0):
    #     string=string+"Buzz"
    # else:
    #     string=str(num)

    # return string
