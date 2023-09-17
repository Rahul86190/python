def add():
    n=int(input("enter a number to find its factorial addition"))
    s=0
    while n>0:
        s=s+n
        n=n-1
    print(s)

add()