from random import randint
def randnums(limit,range):
    i = 0
    with open("4b_rand.txt","w") as file:
        while i < limit:
            file.write(str(randint(1,range + 1))+'\n')
            i += 1

randnums(400000000,200)




