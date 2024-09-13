# print("hello world!")


# sum=0
# for i in range(1,51):
#     if i %2 == 0:
#        sum += i
# print("sum of all even number:",sum)
#

# for i in range(1,21):
#     print(i,i**2)

# sum = 0
# n = 0
# while n <=20:
#     if n %2 != 0:
#         sum += n
#      n +=1
#    print ('sum of first 10 odd num is',sum)
#

#  while True  :
#     name =input("enter name")
#     total =0
#         while True :
#        print ("enter amount and quantity:")
#        amount =float(input("enter amount :"))
#        quantity =float(input("enter quantity:"))
#        total += amount*quantity
#        repeat = input("do you want to add more iteams?")
#        if repeat =="no" or repeat =="NO":
#            break
#        print ("name:",name)
#        print ("amount to paid",total)
#        print ("-" * 40)
#        print ("-"*40)
#
#        repeat1 =input("do yoy want to go next customer?")
#        if repeat1 == "no" or repeat1 == "NO":
#            break


# for i in range (1,6):
#     for j in range (1,i+1):
#         print(j, end = " ")
#     print()

# for i in range (1,6):
#     for j in range (1,i+1):
#         print(i, end = " ")
#     print()

# for i in range(1,6):
#     for j in range(5,i,-1):
#         print("",end=" ")
#     for k in range(i):
#         print("*" ,end="")
#     print()

# for i in range (1,6):
#     for j in range (1,i+1):
#         print(i, end = " ")
#     print()


         # best pattern this

# for i in range (1,6):
#     for j in range (1,i+1):
#         print("*", end = " ")
#     print()
# for i in range(5,0,-1):
#     for k in range(0,i-1):
#         print("*",end =" ")
#     print()
#


# for i in range(1,11):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print()
#
           # fibonacci series

# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,11):
#     c=a+b
#     a=b
#     b=c
#     print(c , end=" ")
#

# a = 0
# b = 1
# n=int(input("enter a number :"))
# if n ==1:
#     print(1)
# else:
#      print(a)
#      print(b)
#      for i in range(2,n):
#          c = a+b
#          a = b
#          b = c
#          print(c,end=" ")


                 # prime number

# num=int(input("enter a number here:"))
#
# if num<=1:
#     print("not prime number")
# else:
#     for i in range(2,num):
#         if num%i ==0:
#             print("not a prime number")
#             break
#     else:
#         print("prime number")
#
                  # palindrome number

# num=int(input("enter a number:"))
# temp=num
# rev=0
#
# while num >0:
#     dig =num%10
#     rev =rev*10 + dig
#     num =num//10
# if rev == temp:
#     print("it is palindrome")
# else:
#     print("not a palidrome number")



   # Using if...elif...else Number is Positive, Negative or 0

# num = float(input("Enter a number: "))
# if num > 0:
#    print("Positive number")
# elif num == 0:
#    print("Zero")
# else:
#    print("Negative number")


   #  Using Nested if Number is Positive, Negative or 0

# num = float(input("Enter a number: "))
# if num >= 0:
#    if num == 0:
#        print("Zero")
#    else:
#        print("Positive number")
# else:
#    print("Negative number")



# factorial of number


#    num = int(input("Enter a number:"))

#    if num<0:
#    print("factorial does not exist for negative number")
#    elif num ==0:
#    print("factorial of 0 is 1")
#   else:
#   for i in range(1,num + 1):
#       factorial=factorial*i
#    print("factorial of ",num ,"is",factorial)
#factorial

#using recursion

#   def factorial(x):
#   if x == 1:
#        return 1
#  else:
#        return (x * factorial(x-1))

# num1= int(input("enter a number:"))
# result= factorial(num1)
# print("factorial of ",num1 ,"is",result


  
