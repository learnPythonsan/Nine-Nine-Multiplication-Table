
# hi 九九乘法表

x = 1
sum = 0
while x <=9:
    y = 1
    while y <=9:
        sum = x * y
        print(x,"*",y,"=",sum)
        y+=1
    x+=1
