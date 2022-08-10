# EX3
def square_of_sum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum ** 2

def sum_of_squares(n):
    sum = 0
    for i in range(n + 1):
        sum += i ** 2
    return sum

def difference(n):
    return abs(sum_of_squares(n) - square_of_sum(n))

print(difference(100))


# EX 4
import urllib.request

link = "https://projecteuler.net/project/resources/p022_names.txt"
text =urllib.request.urlopen("https://projecteuler.net/project/resources/p022_names.txt")

for line in text:
    line = line.capitalize()
    print(line)
with open('names.tx','w') as output_file:
    for line in text:
        output_file.write(line)


# EX 5
def digit_count(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

def lst_from_num(n):
    lst = []
    count =digit_count(n)
    while count > 0:
        el = n - (n // 10) * 10
        lst.append(el)
        n = (n - el) // 10
        count -= 1
    return lst

def is_palindrom(n):
    return lst_from_num(n) == lst_from_num(n)[::-1]

print(is_palindrom(12344321))




