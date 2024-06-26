num=int(input("enter the number: "))
flag=False
if num==1:
    print("1 is not a prime")
if num > 1:
    for i in range(2,num):
        if(num % i)==0:
            flag=True
        if flag:
            print(num,"is not a prime")
            break
        else:
            print(num,"is a prime")
            break
