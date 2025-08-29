from typing import List, Union, Tuple, IO

def afun(a, b, c):
    print(a)
    print(b)
    print(c)

def writeList(a_list):
    strs = [','.join(l) for l in a_list]
    print("\n the lists are " + str(strs))

def saveLines(a_list: list,a_file: IO,):
    strs = [','.join(l) for l in a_list]
    a_file.writelines(strs)


list1 = [('1', '2', '3'), ('geeks', 'for', 'geeks', '7')]
# writeList([(1,2,3),(4,5,6,7)])
#writeList([('1', '2', '3'), ('geeks', 'for', 'geeks', '7')])
writeList(['1', '2', '3', 'geeks', 'for', 'geeks', '7'])

f = open("temp1.txt", "w")
#saveLines((a_list = list1, a_file = f)
saveLines(list1,f)
f.close()
print()


