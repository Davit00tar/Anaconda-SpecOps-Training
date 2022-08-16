# 1 REMOVE DUPLICATS
lst = [1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8]
def rem_dup(data):
    return list(set(data))

print(rem_dup(lst))

# 2 MERGE ARRAYS
lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 7]
def merge_arr(data1, data2):
    data1 = (data1 + data2)
    data1.sort()
    return data1

print(merge_arr(lst1, lst2))

# 3 CONTAINS DUPLICATE
def isduplicate(lst):
    return False if len(list(set(lst))) == len(lst) else True

print(isduplicate(lst))

# 4 SINGLE NUMBER
lst4 = [1, 2, 3, 1, 3]
def single_num(data):
    lst = []
    for i in data:
        if i in lst:
            lst.remove(i)
        else:
            lst.append(i)
    return lst[0]

print("SINGLE NUMBER IS", single_num(lst4))

# 5 MISSING NUMBER
lst5 = [1, 0, 2, 3, 4]
def missing_number(data):
    guess = len(data)
    while guess >= 0:
        if guess in data:
            guess -= 1
        else:
            break
    return guess

print("MISSING NUMBER IS", missing_number(lst5))

# 6 BINARRY ARR
def maxof(data):
    max = data[1]
    for i in range(1,len(data)):
        if max < data[i]:
            max = data[i]
    return max
def consecutive(data):
    lst = []
    j = 0
    for i in range(len(data)):
        if data[i] != data[j]:
            lst.append(i-j)
            j = i
        else:
            lst.append(i-j)
    return maxof(lst)
print(consecutive([1,0,0,0,1,0,0,0,0,1]))

# 7 ARRAY PARTITION
lst6 = [1, 2, 5, 7, 3, 4]
def arr_partition(data):
    data.sort()
    sum = 0
    while len(data) >= 2:
        sum += min(data[0], data[1])
        data = data[2:]
    return sum

print(arr_partition(lst6))

# 8 LARGEST PRIME COUNT
def biggest_prime(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n //= i
        i += 1
    return n

print(biggest_prime(600851475143))

# 9 MAX PALINDROMIC
def ispal(x):
    return str(x) == str(x)[::-1]

def biggest_pal(start, end):
    max_ans = 0
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            p = i * j
            if ispal(p) and max_ans < p:
                max_ans = p
    return max_ans

print(biggest_pal(100, 999))

# 10 SMALLEST MULTIPLE #WRONG
def smal_mult(n):
    answer = 1
    lst = []
    for i in range(2,n + 1):
        divider = 2
        num = i
        while num > 1:
            if num % divider == 0:
                lst.append(divider)
                num //= divider
            else:
                divider += 1
    lst = rem_dup(lst)
    for i in lst:
        answer *= i
    return answer
print(smal_mult(20))

# 11 SUM SQUARE DIFFERENCE

def square_dif(n):
    a1 = 0
    a2 = 0
    for i in range(n):
        a1 += i ** 2
        a2 += i
    return a2 ** 2 - a1

print(square_dif(100))

# 12
def nth_prime(n):
    counter = 2
    for i in range(3, n**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
               break
        else:
            counter += 1
        if counter == n:
            return i

print(nth_prime(100001))



