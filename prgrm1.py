def fact(num):
    if num==0 or num==1:
        return 1
    return num *fact(num-1)
num=int(input("Enter a number:"))
print(fact(num))