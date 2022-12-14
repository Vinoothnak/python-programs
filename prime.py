n=int(i  nput("enter a number"))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print("not a prime no")
            break
        else:
            print("it is a prime number")
else:
    print("not a prime number")
