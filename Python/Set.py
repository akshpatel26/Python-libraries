
                          #SETS....

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

# copy

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


# function

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

