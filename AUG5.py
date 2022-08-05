#1
file=open("/Users/davit/desktop/myLanguage/test1.tx","r")

def sum_of_nums(data):
    sum = 0
    for line in data:
        sum += int(line)
    return sum

# 2---TITLE
text1=open("/Users/davit/desktop/myLanguage/text_for_Aug5_ex2","r")
text2=open("/Users/davit/desktop/myLanguage/text_for_Aug5_ex2","w")
def title_file(data,location):
    new_data=""
    for line in data:
        new_data += line.title()
    location.write(new_data)

#3
lst=[1,1,1,3,2,4,2,5,6,6,6,6,77,3]

def cuant(data):
    ans={}
    for x in data:
        if x in ans:
            ans[x] += 1
        else:
            ans[x] = 1
    return ans
print(cuant(lst))

#4



def cuant_symbols(data):
    ans={}
    for line in data:
        for char in line:
            if char in ans:
                ans[char] += 1
            else:
                ans[char] = 1
    return ans

# 5
str5="hello hello hello"
def del_third_symb(data):
    count = 1
    ans=""
    for char in data:
        if count  % 3 == 0:
            pass
        else:
            ans += char
        count += 1

    return ans
print(del_third_symb((str5)))

# 6
def count_word(data):
    lst=[]
    for line in data:
        lst += line.split(" ")

    ans=cuant(lst)# ogtagorcel 3rd exic
    return ans
print(count_word(text1))

# 7
lst=[7,4,5,56,34]
def sort_sqr(data):
    lst2=[el**2 for el in data]
    lst3=[]
    while lst2:
        min = lst2[0]
        a=0
        for pose in range(len(lst2)):
            print(len(lst2))
            if min > lst2[pose]:
                min = lst2[pose]
                a=pose
        lst3.append(min)
        lst2.pop(a)
    return lst3

# 8
def sum_of_symb(num):
    new_str = str(num)
    sum = 0
    for symb in new_str:
        sum += int(symb)
    return sum
print(sum_of_symb(145))

#9
def add_of_symb(num):
    new_str = str(num)
    add = 1
    for symb in new_str:
        add *= int(symb)
    return add

def diff_of_add_and_sum(num):   #ogtagorcvum e 8rd vqrjutyunic
    return add_of_symb(num)-sum_of_symb(num)
print(diff_of_add_and_sum(123488))

#10
def is_odd(num):
    return num % 2 == 1

def odd_nums_between(start,end):
    between = end - start -1
    odd_num_cuant = int(between/2)
    if is_odd(start):
        odd_num_cuant += 1
    if is_odd(end):
        odd_num_cuant += 1
    return odd_num_cuant
print(odd_nums_between(1,9))


























