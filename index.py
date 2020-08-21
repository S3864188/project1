a =[1,2,3]
def reveerse(a):
    b=a[::-1]
    return b
    
print(reveerse(a))

def count(list, item):
    total = 0
    for x in list:
        if x == item:
            total += 1
    return total
print(count([2, 3, 4, 5, 6], 3))

def isin(list, item):
    for x in list:
        if x == item:
            return True
    return False
print(isin([2, 3, 3, 4, 5, 6], 3))

def index(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1
print(index([2, 3, 4, 5, 6], 4))

def insert(list, index, item):
    list[index:index] = [item]
    return list

print(insert([1,2,3,4], 1, 5))

def insert2(lst, index, item):
    lst1 = lst[0:index]
    lst1.append(item)
    lst2 = lst[index:-1]
    new_lst = lst1 + lst2
    return new_lst
print(insert2([1, 2, 4, 7, 9, 10], 3, 4321))
