
import random

key = [random.randint(1,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]

# 将输入的数字分解成一个列表
def splitdigit(num):
    j = 1000
    digits = [0,0,0,0]
    for i in range(0,4):
        digits[i] = int(num/j)
        num = num%j
        j = j/10 
    return digits

#def comparedigit(key,digits):
#    a = 0
#    b = 0
#    for i in range(0,4):
#        for j in range(0,4):
#            if key[i] == digits[j]:
#                if i == j:
#                    a += 1
#                    break
#                else:
#                    b += 1
#                    break
#    print("%dA%dB"%(a,b))     
#    return (a,b)

#将输入数字和答案进行逐一比较
def comparedigit(key,digits):
    a = 0
    b = 0
    for i in range(0,4):
        if key[i] == digits[i]:
            a += 1
        else:
            for j in range(0,4):
                if key[i] == digits[j]:
                    b += 1
                    break
    print("%dA%dB"%(a,b))     
    return (a,b)


i = 10

print("答案是",key)

while True:
    num =input("请输入数字")
    if num.isdigit() != 1:
        print("输入的不是数字，请输入数字")
        continue
    else:
        num = int(num)
        num = splitdigit(num)
        print(num)
        i-=1
        a,b =  comparedigit(key,num)
        if a == 4:
            print("答案完全正确\n结束")
            exit(0)
        else:
            print("答案不正确\n你还有 %d次机会"%i)
 
        if i == 0:
           print("结束")
           exit(0)


    
    






