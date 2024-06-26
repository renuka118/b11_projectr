##              $$$$             Assignemt-01

#######Data types

# $$$
### List datatype :list is a built-in data type that represents an ordered collection of items. Lists are versatile and widely used due to their simplicity and flexibility.
# list a collection which is ordered and changeable. Allows duplicate members.

# list=[]
# print(list)   #[]
# print(dir(list))   #'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# $$$ 1

"""
list1 = [10, 20, 30, 40, 50, 60]
# print(list1)      # [10, 20, 30, 40, 50, 60]
# print(list1[0])    # 10
# print(list1[5])     # 60
# print(list1[-1])  # 60
# print(list1[-4])  # 30
# print(list1[-6])  # 10

list1.append(70)
# print(list1)    #[10, 20, 30, 40, 50, 60, 70]

list1.append(80)  #append()
# print(list1)    # [10, 20, 30, 40, 50, 60, 70, 80]

lt=[80,90,100]
list1.extend(lt)  #extend()
# print(list1)    #[10, 20, 30, 40, 50, 60, 70, 80, 80, 90, 100]

list1.insert(2, 25)
# print(list1)      # [10, 20, 25, 30, 40, 50, 60, 70, 80, 80, 90, 100]

list1.remove(80)
# print(list1)     #[10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]

list1.pop(3)
# print(list1)    #[10, 20, 25, 40, 50, 60, 70, 80, 90, 100]

lt =list1.index(70)
# print(lt)   #6 

list1.append(25)
# print(list1)  #[10, 20, 25, 40, 50, 60, 70, 80, 90, 100, 25]

lt= list1.count(25)
# print(lt)   # 2

list1.reverse()
# print(list1)   # [25, 100, 90, 80, 70, 60, 50, 40, 25, 20, 10]

list1.sort()
print(list1)   #[10, 20, 25, 25, 40, 50, 60, 70, 80, 90, 100]

lt1=list1.copy()
print(lt1)    #[10, 20, 25, 25, 40, 50, 60, 70, 80, 90, 100]

print(list1) # [10, 20, 25, 25, 40, 50, 60, 70, 80, 90, 100]

lt1.clear()
print(lt1)  #[]

"""
## $$ 2


list2 = ["Aarav", "Arnav", "Bhavesh", "Esha", "Gautam", "Jay", "Neha"]
# print(list2) #['Aarav', 'Arnav', 'Bhavesh', 'Esha', 'Gautam', 'Jay', 'Neha']


list2.append("Dev")
# print(list2)  # ['Aarav', 'Arnav', 'Bhavesh', 'Esha', 'Gautam', 'Jay', 'Neha', 'Dev']

lt = ["Kaya", "Raghav"]
list2.extend(lt)
# print(list2) #['Aarav', 'Arnav', 'Bhavesh', 'Esha', 'Gautam', 'Jay', 'Neha', 'Dev', 'Kaya', 'Raghav']

list2.insert(2, "Abhi")
# print(list2) #['Aarav', 'Arnav', 'Abhi', 'Bhavesh', 'Esha', 'Gautam', 'Jay', 'Neha', 'Dev', 'Kaya', 'Raghav']

list2.remove("Esha")
# print(list2) #['Aarav', 'Arnav', 'Abhi', 'Bhavesh', 'Esha', 'Gautam', 'Jay', 'Neha', 'Dev', 'Kaya', 'Raghav']


lt = list2.pop(3)
# print(lt)  #Bhavesh

# print(list2) #['Aarav', 'Arnav', 'Abhi', 'Gautam', 'Jay', 'Neha', 'Dev', 'Kaya', 'Raghav']
lt1 = list2.index("Gautam")
# print(lt1)  # 3


ct = list2.count("Jay")
# print(ct)  #1

list2.reverse()
# print(list2)  #['Raghav', 'Kaya', 'Dev', 'Neha', 'Jay', 'Gautam', 'Abhi', 'Arnav', 'Aarav']

list2.sort()
# print(list2) #['Aarav', 'Abhi', 'Arnav', 'Dev', 'Gautam', 'Jay', 'Kaya', 'Neha', 'Raghav']

lt2 = list2.copy()
# print( lt2)  # ['Aarav', 'Abhi', 'Arnav', 'Dev', 'Gautam', 'Jay', 'Kaya', 'Neha', 'Raghav']

lt2.clear()
# print(lt2)  # []


# # $$ 3

list3 = [10, 20, 30, 40]

# print(list3)  #[10, 20, 30, 40]

list3.append(69)
# print(list3)  #[10, 20, 30, 40, 69]

lt3 = [22, 33, 44]
list3.extend(lt3)
# print(list3)  #[10, 20, 30, 40, 69, 22, 33, 44]


list3.append("Ravi")
# print(list3)  #[10, 20, 30, 40, 69, 22, 33, 44, 'Ravi']

list3.insert(2, "Rohan")
# print(list3) #[10, 20, 'Rohan', 30, 40, 69, 22, 33, 44, 'Ravi']

list3.remove(30)
# print(list3) #[[10, 20, 'Rohan', 40, 69, 22, 33, 44, 'Ravi']

list3.pop(4)
# print(list3) #[10, 20, 'Rohan', 40, 22, 33, 44, 'Ravi']


lt = list3.index("Rohan")
# print(lt)  #2

ct = list3.count(22)
# print(ct)  #1


lt = list3.copy()
# print(lt)  #[10, 20, 'Rohan', 40, 22, 33, 44, 'Ravi']


lt.clear()
# print(lt)  #[]


It1 = list3.pop(2)
IT2 = list3.pop(6)
# print(list3) #[10, 20, 40, 22, 33, 44]

list3.reverse()
# print(list3)  #[44, 33, 22, 40, 20, 10]
list3.sort()
# print(list3)  #[10, 20, 22, 33, 40, 44]


# ## $$$ 4

list4 = ["z", "n", "e", "d", "f", "t", "s"]

list4.append("b")
# print(list4)  #[' z', 'n', 'e', 'd', 'f', 't', 's', 'b']

lt = ["h", "o", "w", "x"]
list4.extend(lt)
# print(list4)  #[' z', 'n', 'e', 'd', 'f', 't', 's', 'b', 'h', 'o', 'w', 'x']

list4.insert(2, "l")
# print(list4) #[' z', 'n', 'l', 'e', 'd', 'f', 't', 's', 'b', 'h', 'o', 'w', 'x']
""
list4.remove("e")
# print(list4)  #[' z', 'n', 'l', 'd', 'f', 't', 's', 'b', 'h', 'o', 'w', 'x']

lt = list4.pop(2)
# print(list4) #['z', 'n', 'd', 'f', 't', 's', 'b', 'h', 'o', 'w', 'x']

ct = list4.index("d")
# print(ct) #2

ct = list4.count("f")
# print(ct)  #1

list4.sort()
# print(list4)  #[' z', 'n', 'd', 'f', 't', 's', 'b', 'h', 'o', 'w', 'x']

list4.reverse()
# print(list4)  #['z', 'x', 'w', 't', 's', 'o', 'n', 'h', 'f', 'd', 'b']

lt = list4.copy()
# print(lt)  #['z', 'x', 'w', 't', 's', 'o', 'n', 'h', 'f', 'd', 'b']

lt.clear()
# print(lt)  #[]

## $$5

list5 = [1, "Avinash", 5, 7, 6.34, "Red", 3, 4]
# print(list5)  #[1, 'Avinash', 5, 7, 6.34, 'Red', 3, 4]

list5.append("Blue")
# print(list5) #[1, 'Avinash', 5, 7, 6.34, 'Red', 3, 4, 'Blue']

lt = [8, "Chery", 9, 5.55]
list5.extend(lt)
# print(list5)  #[1, 'Avinash', 5, 7, 6.34, 'Red', 3, 4, 'Blue', 8, 'Chery', 9, 5.55]

lt = list5.index("Chery")
# print(lt) #10

ct = list5.count(5)
# print(ct) #1

lt = list5.copy()
# print(lt) #[1, 'Avinash', 5, 7, 6.34, 'Red', 3, 4, 'Blue', 8, 'Chery', 9, 5.55]

lt.clear()
# print(lt) #[]


list5.remove("Blue")
# print(list5) #[1, 'Avinash', 5, 7, 6.34, 'Red', 3, 4, 8, 'Chery', 9, 5.55]


##########  Set
# Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

set1 = {1, 2, 3, 4, 5}
# print(set1) #{1, 2, 3, 4, 5}

# print(dir(set1))
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove'

set1.add(6)
# print(set1) #{1, 2, 3, 4, 5, 6}

set1.update([7, 8, 9])
# print(set1) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

set1.remove(5)
# print(set1) #{1, 2, 3, 4, 6, 7, 8, 9}

set1.discard(8)
# print(set1) #{1, 2, 3, 4, 6, 7, 9}

set1.pop()
# print(set1) #{2, 3, 4, 6, 7, 9}

cp = set1.copy()
# print(cp)  #{1, 2, 4, 6}

cp.clear()
# print(cp) #{1, 2, 4, 6}


## set operations


## $$1
st1 = {1, 2, 3}
st2 = {3, 4, 6}
unionres = st1.union(st2)
# print(unionres)  #{1, 2, 3, 4, 6}

inter_res = st1.intersection(st2)
# print(inter_res)  #{3}

diff_res = st1.difference(st2)
# print(diff_res)  # {1, 2}

sym_diff_set = st1.symmetric_difference(st2)
# print(sym_diff_set) #{1, 2, 4, 6}


s1 = {1, 2}
s2 = {1, 2, 3, 4}
# print(s1.issubset(s2))  # True

# print(s2.issuperset(s1))  #True

# print(s1.isdisjoint(s2)) #False


s3 = {3, 4, 5}
# print(s1.isdisjoint(s3))  #True

## $$$2


set2 = {"e", "h", "i", "a", "r", "g"}
# print(set2) #{'i', 'e', 'h', 'g', 'r', 'a'}

set2.add("y")
# print(set2)  #{'r', 'y', 'i', 'h', 'e', 'g', 'a'}

set2.discard("g")
# print(set2)  #{'i', 'h', 'r', 'e', 'y', 'a'}

set2.remove("h")
# print(set2)  #{'e', 'a', 'i', 'y', 'r'}

set2.pop()
# print(set2)  #{'a', 'e', 'i', 'r'}


st1 = {" Ajay", " Karan", " Raj"}
st2 = {"Nitesh", "Vivek", "Arjun"}

res = st1.union(st2)
# print(res)  #{' Ajay', ' Raj', 'Vivek', 'Arjun', 'Nitesh', ' Karan'}

res1 = st1 | st2  # union with operator
# print(res1)#{' Karan', ' Raj', 'Vivek', 'Nitesh', ' Ajay', 'Arjun'}


intr_res = st1.intersection(st2)
# print(intr_res)  #set()

intr_res1 = st1 & st2  # using operator
# print(intr_res1)    #set()

st1.add("Vivek")
# print(st1)  #{' Karan', ' Ajay', 'Vivek', ' Raj'}
# print(st2)  #{'Nitesh', 'Arjun', 'Vivek'}


res = st1.difference(st2)
# print(res)  #{' Raj', ' Ajay', ' Karan'}

res1 = st1 - st2
# print(res1) #{' Raj', ' Ajay', ' Karan'}


## $$$3

set3 = {"c_lang", "CPP", "Java", "Go-lang"}
# print(set3)  #{'Java', 'c_lang', 'GO-lang', 'CPP'}

set3.add("Python")
# print(set3)  #{'CPP', 'Python', 'c_lang', 'Go-lang', 'Java'}


set3.update(["Javascript", "Kotlin"])
# print(set3)  #{'Python', 'CPP', 'Go-lang', 'Java', 'Kotlin', 'Javascript', 'c_lang'}

set3.remove("Go-lang")
# print(set3) #{'Kotlin', 'Python', 'CPP', 'Javascript', 'Java', 'c_lang'}

set3.discard("Kotlin")
# print(set3) #{'Java', 'Python', 'Javascript', 'CPP', 'c_lang'}

set3.pop()
# print(set3) #{'Javascript', 'Java', 'CPP', 'Python'}

s1 = {"c_lang", "CPP"}
s2 = {"c_lang", "CPP", "Java", "Python"}
# s3 = {"c_lan", "CPP", "Python", "Javascript"}
## Union

# print(s1 | s2 )  # {'Python', 'c_lang', 'Java', 'CPP'}
# print(s1.union(s2))  # {'Python', 'c_lang', 'Java', 'CPP'}

## intersection
# print(s1 & s2)  #{'CPP', 'c_lang'}

# print(s1.intersection(s2)) #{'CPP', 'c_lang'

# difference
# print(s2-s1)    #{'Java', 'Python'}
# print(s2.difference(s1))  #{'Java', 'Python'}


#### Tuple
# ()->representation
# Immutable


tuple = (1, 2, 3, 4, 5)
# print(tuple)  # (1, 2, 3, 4, 5)


# print(dir(tuple))  #'count', 'index'

tuple1 = (2, 3, "java", 4.5, 3.4)
# print(tuple1)  #(2, 3, 'java', 4.5, 3.4)


t1 = 11, 22  # Braces are not necessary
# print(t1)   #(11, 22)


t2 = (11, 22, 33, 44, 33, 22, 44, 55, 44)
# print(t2.count(44))   #3


# print(t2.index(22))  #1


## Nested tuple
t2 = ((1, 2), (11, 22, 33), (4, 5, 6), (7, 8))
# print(t2)  # (('python', {1, 2, 3}, (4, 5, 6)), {8, 7})
# print(t2[1][1]) #22
# print(t2[3][1])  #8


## Tuple packing and unpacking
t3 = (10, 20, 30)
a, b, c = t3
# print(a)  #10
# print(b)  #20
# print(c)  #30


## Immutable
# t4=(10,20,30)
# t4[1]=100  #TypeError: 'tuple' object does not support item assignment
# print(t4)


##### Dictionary
# a dictionary is a built-in data type that allows you to store key-value pairs.
# It is one of the most powerful and flexible data structures in Python, providing fast access to data
# {}->representation
dict = {"name": "Raj", "age": "25", "sub1": "89", "sub2": "79"}
# print(dict)  # {'name': 'Raj', 'age': '25', 'sub1': '89', 'sub2': '79'}

# print(dir(dict))
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# Accessing dict elements

# print(dict["name"]) #Raj
# print(dict["age"])  #25

# Adding new key-value
dict["Avg"] = ["8.9"]
# print(dict)  #{'name': 'Raj', 'age': '25', 'sub1': '89', 'sub2': '79', 'Avg': ['8.9']}

# Updating an Existing Key-Value Pair
dict["name"] = ["Rohan"]
# print(dict)   #{'name': ['Rohan'], 'age': '25', 'sub1': '89', 'sub2': '79', 'Avg': ['8.9']}

# Removing a Key-Value Pair
del dict["sub2"]
# print(dict)   #{'name': ['Rohan'], 'age': '25', 'sub1': '89', 'Avg': ['8.9']}


d = dict.get("name")
# print(d)  #['Rohan']

k = dict.keys()
# print(k)  #dict_keys(['name', 'age', 'sub1', 'Avg'])
v = dict.values()
# print(v)  #dict_values([['Rohan'], '25', '89', ['8.9']])
kv = dict.items()
# print(kv)  #dict_items([('name', ['Rohan']), ('age', '25'), ('sub1', '89'), ('Avg', ['8.9'])])


d1 = dict.pop("sub1")
# print(d1) #89

d2 = dict.popitem()
# print(d2)  #('Avg', ['8.9'])


dict.update({"name": "Abhi", "Avg": "9.7"})
# print(dict) #{'name': 'Abhi', 'age': '25', 'Avg': '9.7'}


# Nested dict

nested_dict = {
    "stud1": {"name": "Ajay", "age": 25},
    "stud2": {"name": "Sanchit", "age": 24},
}

# print(nested_dict["stud1"]["name"])  # Output: Ajay


# fromkeys() method in Python is a built-in method that creates a new dictionary from the given sequence of elements (such as keys) with a specified value for all keys. This method is often used when you want to initialize a dictionary with a set of keys, all mapped to the same initial value.

dict1 = {"a": "10", "b": "20", "c": "30", "d": "40"}
# print(dict1)  # {'a': 0, 'b': 0, 'c': 0, 'd': 0}
int = 2
newdict = dict1.fromkeys(dict1, int)
# print(newdict)  # {'a': 2, 'b': 2, 'c': 2, 'd': 2}

# print(dict1)  # {'a': '10', 'b': '20', 'c': '30', 'd': '40'}


#### Fucntions
# 1. positional Argument function


# def posfn(a, b=30, c=40):
# print("a =", a, "b = ", b, "c =", c)  #a = 22 b =  33 c = 11


# posfn(c=11, a=22,b=33)


# 2. Defaul arguments

# def defaultfun (a ,b,c,d=888):
#     print ("a=", a, "b=",b, "c=", c, "d=", d)
#     print("end of the function")

# print("Inside main function")
# defaultfun(2,3,4)
# for i in range(5):
#     print( defaultfun(11,22,33,44))

# print(" After execution of function")


# 3. Keywod argument

# def keywordfu(val1, val2, val3="Nice day"):
#     print("val1=", val1, "value2=", val2 , "val3=", val3) # val1= hello value2= Rohan val3= Nice day
#     print("end of function")

# print("Before calling function ")
# keywordfu(val2="Rohan", val1="hello")


# 4. variable length argument

# def variablelenfn(*args):
#     print(args, type(args))  #(11, 22, 33, 44, 555, 66, 77, 88, 99) <class 'tuple'>


# print("first statemet")
# #variablelenfn()
# variablelenfn(11,22,33,44,555,66,77,88,99)
# print("After call to a function")

# 5. keyword variable length argument


# def func(**kwargs):
#     print(kwargs, type(kwargs))  #{'name': '10', 'val2': '20', 'val3': '30', 'val4': '40'} <class 'dict'>


# func(name="10", val2="20", val3="30", val4="40")


# def func(a, b, c=30, *args, **kwargs):
#     print("positional: ", a, b)  # 10 20
#     print("default", c)  # 50
#     print("args:", args)  # ()
#     print("kwargs: ", kwargs)  # {}

# func(10, 20, 60, 70, 80, 90, x="value1", y="value2")
# func(10, 20, 50, 60, 70, 80, 90, x="value1", y="value2")
# func(10, 20,  d=70, e=80, f=90, x="value1", y="value2")    #prints c default val

## Decorator
"""
def decor(func):    #   main
    def inner():
        print("#" * 35)
        func()       #  main
        print( "$" * 35)
    return inner


@decor   # decor(main)
def main():  # main--->inner
    print("Transaction steps")

main()

"""

##------------


def special_decor(func):  # operation
    def inner(a, b):
        print("@" * 35)
        func(a, b)
        print("%&" * 35)

    return inner


@special_decor  # special_decor(opertion)
def operation(x, y):  # inner reference
    print("Different Arithmetic operations")
    print("additon", x + y)
    print("subtraction=", x - y)
    print("Multiplication=", x * y)
    print("Division=", x / y)


operation(45, 3)
# p = int(input("enter first val"))

# q = int(input("enter second val"))
# operation(p,q)
