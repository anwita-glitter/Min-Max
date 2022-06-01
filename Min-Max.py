n=input("Enter the numbers ")
list1=n.split()

def max_num(li):
    m=int(li[0])
    for a in range(1,len(li)):
        if int(li[a])>m:
            m=int(li[a])
    print("The maximum number is",m)

def min_num(li):
    n=int(li[0])
    for a in range(1,len(li)):
        if int(li[a])<n:
            n=int(li[a])
    print("The minimum number is",n)

max_num(list1)
min_num(list1)