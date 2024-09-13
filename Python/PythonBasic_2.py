                   # AreaCalculate

# while True:
#     print(""" press 1 to get area of square
#     press 2 to get area of rectangle
#     press 3 to get area of circle
#     press 4 to get area of triangle""")
#
#     choice =int(input("enter a number between 1-4:"))
#
#     if choice==1:
#         while True:
#             side =float(input("enter side:"))
#             area =side**2
#             print("area of square is",area)
#             repeat =input("do you want try again with square?")
#             if repeat =="no" or repeat=="NO":
#                 break
#     if choice==2:
#         while True:
#             length=float(input("enter length:"))
#             width =float(input("enter width:"))
#             area=length*width
#             print("area of rectangle is",area)
#             repeat =input("do you want try again with square?")
#             if repeat =="no" or repeat=="NO":
#                 break
#     if choice==3:
#         while True:
#             radius =float(input("enter radius:"))
#             area = ((22/7)*(radius**2))
#             print("area of circle is",area)
#             repeat =input("do you want try again with square?")
#             if repeat =="no" or repeat=="NO":
#                 break
#
#     if choice==4:
#         while True:
#             base =float(input("enter base:"))
#             height =float(input("enter height:"))
#             area =0.5*base*height
#             print("area of ta is",area)
#             repeat =input("do you want try again with square?")
#             if repeat =="no" or repeat=="NO":
#                 break
#     repeat1 =input("do you want to repeat menu ?")
#     if repeat1=="no":
#         break

                # Largest Among three numbers

# num1 = float(input("enter first number:"))
# num2 = float(input("enter second number:"))
# num3 = float(input("enter third number:"))
#
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3
#
# print("largest number is", largest)

                      # Armstrong Number

# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
#
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")


# leap year


# year =int(input("Enter a year:"))

# if (year % 400 == 0) and (year % 100 ==0):
#     print("{0} is a leap year".format(year))
#
# elif (year % 4 == 0) and (year % 100 !=0):
#     print("{0} is a leap year".format(year))
#
# else:
#     print("{0} is not a leap year".format(year))

