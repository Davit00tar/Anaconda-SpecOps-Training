# EX2
def strmove(str,num):
    count = len(str) - num
    for i in range(count):
        change = str[0]
        str += change
        str = str[1:]
    return str
print(strmove("hello",2) == "lohel")

#EX3
def mult(a,b,below):
    sum = 0
    for num in range(below):
        if num % a == 0 or num % b ==0:
            sum += num
    return sum

print(mult(3,5,1000))

#EX4
def is_even(n):
    return True if n % 2 == 0 else False

def fib_even_sum():
    a = 0
    b = 1
    sum = 0
    while b < 4000000:
        a,b = b,a+b
        if is_even(b):
            sum += b
    return(sum)
print(fib_even_sum())

