###########  Assignment-2

######  I- Variables Types

####### i- Local variables


### $$  1
# def message():
#     a, b = 5, 3
#     add = a + b
#     print(" Hi, I'm  in function body")
#     print("addition=", add)
#     print("End of function")


# print("Hi, I'm  in main function ")
# message()
# print("Back to main function")


# ### $$  2
# def addition():
#     x, y = 10, 20
#     addition = x + y
#     print("Addition=", addition)


# print("Main function")
# addition()


### $$  3
# def mul(x, y):
#     result = x + y
#     return result


# print(mul(2, 3))


### $$  4


# def msg():
#     print("In function body")
#     x = int(input("enter x value"))
#     print("x value", x)  # 100


# print("In main fuction")
# x = int(input("enter x value"))
# print("x value", x)  # 10
# msg()
# print("End of main ")


### $$  5


# def list_fun(list1):
#     list1.append(4)  # using append adding new ele to list
#     return list1


# list = [1, 2, 3]
# print(list)  # [1,2,3]
# print(list_fun(list))  # [1, 2, 3, 4]
# print(list)  #  [1, 2, 3, 4]


### $$  6


# def list_fun(list1):
#     list1.pop(1)  # using pop deleting ele from the list
#     list1.extend(10)
#     return list1


# list = [1, 2, 3]
# print(list)  # [1,2,3]
# print(list_fun(list))  # [1,3]
# print(list)  #  [1, 3]


### $$  7


# def list_fun(list1):
#     list2 = [6, 7, 8, 9]
#     print(list2)  # [6, 7, 8, 9]
#     list1.extend(list2)
#     return list1


# list = [1, 2, 3, 4, 5]
# print(list)  # [1, 2, 3, 4, 5]
# print(list_fun(list))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list)  #  [1, 2, 3, 4, 5, 6, 7, 8, 9]


### $$  8
# def dict_fun(dict1):
#     keys = dict1.keys()  # keys is a local variable
#     for key, value in dict1.items():
#         print("Key:", key, ", Value:", value)


# dict_fun({"name": "AA", "age": 12, "Marks": 83})


##########3 Global variables in fucntions


######  $$ 1

# global_var = 10


# def fun1():
#     print("Hii in function ")
#     print("global_var=", global_var)  # 10


# print("In main ")
# print("global_var=", global_var)  # 10
# fun1()


######  $$ 2

# x = 100


# def fun1():
#     x = 10
#     print("x=", x)  # 10

#     print("Local x=", x)  # 10


# print("In main")
# print("x=", x)  # 100
# fun1()
# x = 1
# print("x=", x)  # Reassignment of x=1


######  $$ 3

# x = 1000


# def fun1():
#     print("In function ")
#     print("x=", x)  # 1000


# print("In main")
# print("x=", x)  # 1000
# fun1()
# x = 1
# print("x=", x)  # Reassignment of x=1


######  $$ 4

# x = 100


# def fun1():

#     global x
#     x = 200
#     print("In fun")
#     print("x=", x)  # 200


# print("In main")
# print("x", x)  #  100
# fun1()
# print("In main")
# print("x==", x)  #  200


######  $$ 5
# x=100

# def fun1():
#     print("Inside fun1")
#     print("x=", x)     # 100


# print("In main")
# print("x=", x)  #100
# fun1()
# x=10
# print("x=====", x)  #10


###### For loop
### $1
# rows = 5

# for i in range(1, rows+1):
#     print('*' * i)


### $2
# rows = 7

# for i in range(rows - 1, 0, -1):
#     print("*" * i)


"""
******
*****
****
***
**
*
 """

### $3
# rows =7

# for i in range(rows-1, 0, -1):
#     print('*' * 2*i)

"""  OUTPUT
************
**********
********
******
****
**
"""

### $4
# rows = 7

# for i in range(1, rows+1):
#     print(' ' * (rows - i) + '*' * (2*i - 1))

"""
      *
     ***
    *****
   *******
  *********
 ***********
*************

"""
### $5
# rows = 7

# for i in range(rows - 1, 0, -1):
#     print(" " * (rows - i) + "&" * (2 * i - 1))

"""
&&&&&&&&&&&
  &&&&&&&&&
   &&&&&&&
    &&&&&
     &&&
      &

"""

### $5

# rows = 7

# for i in range(1, rows+1):
#     print(' ' * (rows - i) + '*' * (2*i - 1))

# for i in range(rows - 1, 0, -1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))


### $6

# rows = 7

# for i in range(rows, 0, -1):
#     print('$' * i)

### Using While loop
##### $1
# rows = 6
# i = 1

# while i <= rows:
#     print("*" * i)
#     i += 1

"""
*
**
***
****
*****
******
"""

##### $2
# rows = 7
# i = 7

# while i > 0:
#     print("&" * i)
#     i -= 1

"""
&&&&&&&
&&&&&&
&&&&&
&&&&
&&&
&&
&
"""

##### $3
# rows = 5
# i = 1

# while i <= rows:
#     print("@" * 5)
#     i += 1

"""
@@@@@
@@@@@
@@@@@
@@@@@
@@@@@


"""
##### $4
# rows=5
# i=1

# while i<=rows:
#     print("1" * i*2)
#     i+=1

"""
11
1111
111111
11111111
1111111111

"""

##### $5
# rows = 5
# i = 1

# while i <= 5:
#     print("3" * 5*i)
#     i += 1


#  ##### Using List

##### $1

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("List elements in forward direction ")
# for i in list:
#     print(i)
# print("List elements in reverse direction")
# for i in list[::-1]:
#     print(i)
# #print(dir(list))
# for i in reversed(list):   # using reversed()
#     print(i)


##### $2

# list1 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# print("list elements in Forward Access:")
# for i in list1:
#     print(i)

# print("\nList elements in Reverse Access using slicing:")
# for i in list1[::-1]:
#     print(i)

# print("\nReverse Access using reversed() function:")
# for i in reversed(list1):
#     print(i)


##### $3

# mobile_lst = ['iPhone', 'Samsung Galaxy', 'Google Pixel', 'OnePlus']
# print("--Forward access ---")
# for mobile in mobile_lst:
#     print(mobile)
# print("--Reverse access---")
# for mobile in reversed(mobile_lst):
#     print(mobile)


##### $4
#### Using while loop 
# list = ["a", "b", "c", "d", "e"]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1




##### $5

# list = ["a", "b", "c", "d", "e"]
# i = len(list)
# print("len=", i)
# i -=1   # i is initialized to index 4 
# while i >= 0 :
#     print(list[i])
#     i -= 1


#  ## --------------------------

#  # Bank Application
'''
import getpass


class Bank:
    def __init__(self, acc_no, atm_pin, balance=5000):
        self.cust_acc_no = acc_no
        self.cust_atm_pin = atm_pin
        self.cust_acc_balance = balance

    def check_balance(self):
        print(f"Total Available balance in your account:{self.cust_acc_balance}")

    def deposit(self, amount):
        self.cust_acc_balance += amount
        print("Amount deposited successfully")
        self.check_balance()

    def withdraw(self, amount):
        if self.cust_acc_balance >= amount:
            self.cust_acc_balance -= amount
            print("Amount debited successfully:(amount)")
            self.check_balance()
        else:
            print("Insufficient balance ")

    def loan(self, loan_amt):
        # total_balance = 5 * (self.cust_acc_balance)
        # print(total_balance)
        min_balance = 5000
        total_loan_amt = 5 * self.cust_acc_balance
        if self.cust_acc_balance >= min_balance:
            print("User can apply for loan")
            if loan_amt <= total_loan_amt:
                print("Loan can be approved")
                self.deposit(loan_amt)
            else:
                print("Not elgible for loan")
        else:
            print("Not eligible for loan ")

           

obj = Bank(1010, 4567, 20000)
# obj.check_balance()
# obj.deposit(2000)
# obj.withdraw(5000)

while True:
    print("Welcome to ICICI ATM")
    user_atm_pin = int(getpass.getpass("Enter atm_pin"))
    # print(user_atm_pin)
    print("Password entered:", "*" * len(str(user_atm_pin)))
    if user_atm_pin != obj.cust_atm_pin:
        print("Invalid atm_pin entered")
        break
    print(
        """ !--- Your choices are: 
          C -- Check Balance
          D -- Deposit Amount
          W -- Withdraw Amount
          L -- Loan 
          E -- Exit 
          ---"""
    )
    counter = 0
    user_input = input("Enter your choice").lower()
    if user_input == "c":
        obj.check_balance()
    elif user_input == "d":
        amt = int(input("Enter the amount to be deposited"))
        obj.deposit(amt)
    elif user_input == "w":
        amt = int(input("Enter the amount to be deposited"))

        obj.withdraw(amt)
    elif user_input == "l":
        loan_amount = int(input("Enter the loan amount"))
        obj.loan(loan_amount)
    elif user_input == "e":
        print("Thank for Banking with us: Visit Again---")
        break
    else:
        print("Invalid choice")
        counter += 1
        if counter == 3:
            print(" Too amny transactions: ")
            break

            '''


# ---------------------------------------

#  ########### OOP's CURD operation

"""
class Mobile:
    mobile_lst = []  # class_level variable

    def __init__(self, m_id: int, mnane: str, price: int, version: str):
        self.MID = m_id
        self.mob_name = mnane
        self.mob_pri = price
        self.mob_ver = version

    def __str__(self):
        return f"\n { self.__dict__}"

    def __repr__(self):
        return str(self)

    @classmethod  # class method
    def add_mobile(cls, brand):
        cls.mobile_lst.append(brand)
        return "New mobile added successfully"

    @classmethod
    def get_all_mobile(cls):
        return cls.mobile_lst

    @classmethod
    def get_mobiles(cls, m_id):
        for m in cls.mobile_lst:
            if m_id == m.MID:
                return m
        return " Mobile not found"

    @classmethod
    def update_price(cls, m_id, updated_price):
        # for m in cls.mobile_lst:
        #     if m_id == m.MID:
        mobile = cls.get_mobiles(m_id)
        if isinstance(
            mobile, Mobile):  
            # isinstance is a built-in function  used to check if an object is an instance
            mobile.mob_pri = updated_price
            return (
                f"Price updated successfully for mobile ID {m_id,updated_price }price"
            )
        else:
            return "Mobile not found"

    @classmethod
    def delete_mobile(cls, m_id):    

        for i, m in enumerate(cls.mobile_lst): 
            #enumerate with class attr  help to easily access both the indices & values of the list elements. This is particularly useful for tasks like displaying list elements with their positions,
            if m.MID == m_id:
                del cls.mobile_lst[i]
                return f"Mobile with ID {m_id} deleted successfully"
        return "Mobile not found"


m1 = Mobile(100, "Samsung", 15000, "M100")
m2 = Mobile(200, "Redmi", 12000, "X100")
m3 = Mobile(300, "iPhone", 55000, "A300")
m4 = Mobile(400, "Realme", 14000, "M11Pro")

Mobile.add_mobile(m1)
Mobile.add_mobile(m2)
Mobile.add_mobile(m3)
Mobile.add_mobile(m4)

# print(Mobile.get_all_mobile())
# print(Mobile.update_price(100, 22000))
print(Mobile.delete_mobile(100))

print(Mobile.get_mobiles(100))

"""
