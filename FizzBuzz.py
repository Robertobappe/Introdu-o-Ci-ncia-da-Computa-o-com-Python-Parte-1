def fizzbuzz(n):
    if n%3==0 and n%5!=0:
        return "Fizz"

    else:
        if n%5==0 and n%3!=0:
            return"Buzz"

        else:
            if n%3==0 and n%5==0:
                return "FizzBuzz"

        if n%53!=0 and n%5!=0:
            return n
