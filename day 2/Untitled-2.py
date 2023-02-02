def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = 10
y = 20
x, y = swap_with_temp(x, y)
print("x =", x)
print("y =", y)
#swap_with_temp(6, 15)




'''def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

x = 10
y = 20
x, y = swap_without_temp(x, y)
print("x =", x)
print("y =", y)'''


'''x = 10
y = 20
temp = x
x = y
y = temp
print("x =", x)
print("y =", y)'''


'''l,b = input("enter length,breath:").split(",")
print("area of rect is:",int(l)*int(b))
print("perimeter of the rectangle:",2*(int(l)+int(b)))
l,b=b,l
print(l,b)'''