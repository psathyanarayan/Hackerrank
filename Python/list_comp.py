#You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print("[",end="")
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k !=n:
                    if(i+j+k !=x+y+z):
                        print([i,j,k],end=", ")
                    else:
                        print([i,j,k],end="")    
    print("]")
