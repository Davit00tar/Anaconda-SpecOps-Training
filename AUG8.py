# EX 1
def stack(target,n):
    ans = []
    count = len(target)
    lst = [el + 1 for el in range(n)]
    for i in lst:
        if i in target:
            ans.append("PUSH")
        else:
            ans.append("PUSH")
            ans.append("POP")
        count -= 1
        if count < 0:
            break

    return ans

print(stack([1,2,4],4))


# EX 2
def intersection(lst1, lst2):
    ans=[]
    for i in lst1:
        for j in lst2:
            if i == j:
                ans.append(i)
    return ans
print(intersection([1, 2, 4, 6], [1, 6, 2]))


# EX 3
def cuant(data):
    ans={}
    for x in data:
        if x in ans:
            ans[x] += 1
        else:
            ans[x] = 1
    return ans

def degree(data):
    max =0
    num = -1
    for i in data:
        if max < data[i]:
            num = data[i]
    return num

def sub_arr(data):
    d=degree(cuant(data))
    for start in range(len(data)):
        if data[start] == d:
            data = data[start:]
            break
    for end in range(len(data), 0, -1):
        if data[end-1] == d:
            data = data[:end]
            break
    return len(data)

print(sub_arr([1, 2, 3, 1, 4, 1,5,7]))

# EX 4
def is_even(n):
    return True if n % 2 == 0 else False

def sort_parity(lst):
    lst1=[]
    lst2=[]
    for i in lst:
        if is_even(i):
            lst1.append(i)
        else:
            lst2.append(i)
    return lst1 + lst2

print(sort_parity([1,2,3,4,5,6]))

# EX 5
def sum_of_unique(lst):
    unique = []
    sum = 0
    for i in lst:
        if i in unique:
            unique.remove(i)
        else:
            unique.append(i)
    for i in unique:
        sum += i
    return sum
print(sum_of_unique([1,2,1,2,14,15,16,15]))




# EX 7
def last_word(str):
    lst = str.split(" ")
    ans = len(lst[-1])
    return ans
print(last_word("Hello World LOL"))

# EX 8
def is_palindrome(str):
    new=""
    for symbol in str:
        if symbol.isalnum():
            new += symbol
    new = new.lower()
    return True if new == new[::-1] else False

print(is_palindrome("A man, a plan, a canal: Panama"))

# EX 9
def email_cuant(data):
    ans = 0
    for email in data:
        num = email.index("@")
        local = email[:num-1]
        domain = email[num+1:]
        if "+" in local:
            sign = local.index("+")
            local = local[sign + 1:]
        email = local + "@" + domain
        if email[0] != "+" and local != "" and domain != "" and email[-4:] == ".com":
            ans += 1
    return ans
print(email_cuant(["davit@mail.com", "an+anna@mail.com"]))

# EX 10
def my_binary(data, target, leftbias):
    l = 0
    r = len(data) - 1
    i = -1
    while l <= r:
        mid = (l + r) // 2
        if target < data[mid]:
            r = mid -1
        elif target > data[mid]:
            l = mid + 1
        else:
            i = mid
            if leftbias:
                r = mid - 1
            else:
                l = mid + 1

    return i
def left_and_right(data, target):
    left = my_binary(data, target, True)
    right = my_binary(data, target, False)
    return [left, right]

print(left_and_right ([1, 2, 2, 2, 3, 4, 5, 6], 2))













