def pattern1(n):
    s=2*n-2
    for i in range(0,n):
        for j in range(0,s):
            print(end=" ")
        s=s-2
        for j in range(0,i+1):
            print ("* ",end="")
        print("\r")

def pattern2(n):
    c=65
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(c),end=" ")
            c=c+1
        print('\r')
pattern1(5)
pattern2(5)




