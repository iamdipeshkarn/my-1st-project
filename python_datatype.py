# python inbuild datatype
# 1.List
a = [2,2,6.7,'sda']
print(type(a))
b = 3
print(a,b)
# a = [] #empty list
print(a[0])
print(a[1])
print(a[2])
# method of adding item in list
# append
a.append("sudden")
print(a)
x = [-1]
print(x)
print(a[-1])

colors = input("enter a colors")
colors1 = input("enter a colors")
colors2 = input("enter a colors")

empty_list = []
print(empty_list)
empty_list.append(colors)
empty_list.append(colors1)
empty_list.append(colors2)
print(empty_list)
print(len(empty_list))

# insert
empty_list.insert(1,"sudden")
empty_list.insert(66,"abcd")
empty_list.append("testing")
print(empty_list)

# concat
x = [1,2,3,4]
y = [5,6,7,8]
z = x+y
print(z)

# extend
a = [1,2,3]
b = [2,55,77]
a.extend(b)
print(a)


