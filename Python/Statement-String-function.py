# '''a= 23
# b=200
# if b>a :
#     print("b is grater than a")'''
#
#
# a=12
# if a%2==0:
#     print("even number")
#     print("welcome ")
# else:
#     print("odd number")
#
#
# mark= int(input("enter the number:"))
# if mark >=90:
#     print("grand A+")
# elif mark>=80 and mark < 90:
#     print("grand A")
# elif mark>=70 and mark < 80:
#     print("grand B")
# elif mark>=60 and mark< 70:
#     print("grand B+")
# else:
#     print("grand c")
#

# make calculator
# num1=int(input("enter the value1:"))
# num2=int(input("enter the value2:"))
# opr =input("enter the opr..")
# if opr =="+":
#     print(num1+num2)
# elif opr =="-":
#     print(num1-num2)
# elif opr =="*":
#     print(num2*num1)
# else:
#     print("invalid opr..")
#
#
'''FOR LOOP'''
# for i in range(1,6):
#     print(i)
# for p in range(1,10,2):
#     print(p)
#
# for a in range(1,11):
#     print("2*",a,"=",2*a)
#
#
# for a in range(10,0,-1):   #reverse number
#     print(a)
# for k in range(10,-1,-2):
#     print(k)
#
#
'''WHILE LOOP'''
# n=0
# while n<=5:
#     print(n,"Welcome RCB")
#     n+=1
#
# i=1
# a=7
# while i<=10:
#     print(a,"x",i,"=",i*a)
#     i+=1
# print(i)

'''Set'''

# a={"Ironman","Hulk","THor","America"}

# print(type(a))
#
# a.add("Spiderman")
# print(a)

# a.pop()
# print(a)

# remove

# a.remove("Hulk")
# print(a)
# discard
# a.discard("THor")
# print(a)

# b=a.copy()
# print(b)

# m={"abc","xyz","pqr","poi"}
# n={"fgf","dsa","rvf"}
# o={"abc","pqr"}
#
# print(m.isdisjoint(n))
#
# print(o.issubset(m))
#
# print(m.issuperset(n))
#
# m.update(n)
# print(m)
#
# o.clear()
# print(o)
#
# print(m.union(n))
#
# print(m.difference(n))
#
# m.difference_update(o)
# print(m)

# x=(m.intersection(o))
# print(x)
#
# m.intersection_update(o)
# print(m)

# y=m.symmetric_difference(o)
# print(y)
# m.symmetric_difference_update(o)
# print(m)


'''function'''

# def max_num(val1,val2,val3):
#     if val1 >val2 and val1>val3:
#         print(val1,"is greatest number")
#     elif val2>val1 and val2>val3:
#         print(val2,"is greatest number")
#     else:
#         print(val3,"is greatest number")
#
# max_num(11,34,5)
#
#
# def list():
#     l=[]
#     for i in range(1,31):
#         l.append(i**2)
#     return l
# print(list())


# def prime(num):
#     if num ==1:
#         print("not prime number")
#     if num ==2:
#         print(" prime number")
#     if num >2:
#        for i in range(2,num):
#         if num % i==0:
#             print("not prime number")
#             break
#     else:
#         print(" prime number")
# prime(37)

# def add(numbers):
#     total =0
#     for i in numbers:
#         total = total+i
#     return(total)
#
# print(add([2,34,56,677,88,99,2,456]))

# def add(nums):
#     if len(nums)==1:
#         return  (nums[0])
#     else:
#         return (nums[0]) + add(nums[1:])
#
# print (add([2,34,56,677,88,99,2,456]))


# def fs(num):
#     if num ==1:
#         return 0
#     elif num ==2:
#         return 1
#     else:
#         return (fs(num-1)+fs(num-2))
# print(fs(7))


'''String '''


# a="welcome to Gandhinagar"

# print(a[6])
# print(a[-6])

'''slicing '''
# print(a[0:7])
# print((a[0:]))
# print(a[0::2])
# print(a[::-1]) #reverse
# print(a[-1::])
# print(a[-1::-2])

'''iteration'''
# t=len(a)
# print(t)
# for i in range(t): #22
#     print(a[i])

# s = "Hello, World!"
# for i in range(len(s)):
#     print(s[i])

# s = "Hello, World!"
# for char in s:      #Using a for loop without indexing
#     print(char)


'''Using enumerate for Index Access'''

# s = "hello"
# for i, char in enumerate(s):
#     print(f"Index {i}: {char}")


# a ="python with data science"
# print(len(a))
#
# print(a.count("o"))
#
# print(a.lower())   #lower all char
#
# print(a.upper())   #upper all char
# print(a.title())   #first letter capitalize
# print(a.capitalize()) #only P

'''find'''
# d="Welcome to bro"
# print(d.find("o"))
# print(d.find('o',5))
# print(d.find('u'))   #unaviable

'''center'''

# name="john"
# print(name.center(30))

'''casefold'''  #convert to lower case

# v="WelCome TO LDrp"
# print(v.casefold())

'''isalnum ,isalpha,isdecimal,isdigit'''

# a="Welcome 1123"
# print(a.isalnum())   #all character then true
# b="patel"
# print(b.isalpha())    #only alphabet
# c="12222222"
# print(c.isdecimal())   #only decimal
# d="1334322"
# print(d.isdigit())


'''chr and ord'''

# a=65
# print(chr(a)) # take integer and converts to character
#
# b='h'
# print(ord(b))    # take single unicode character and converts integer

# c='H'
# print(ord(c))

'''string format'''

# name ="aksh"
# age=21
# a="My Name is {} and My Age is {}"
# print(a.format(name,age))


# a='Harry potter'
# print(a.swapcase())   #lower to upper and upper to lower swap
# print(a.strip())
#
#
# m='odd#brc#icc'
# print(m.split('#'))  #separator string
#
# d="my name is Aksh"
# print(d.replace("aksh","dv"))



