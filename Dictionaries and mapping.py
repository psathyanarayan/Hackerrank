# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook ={}
for i in range(n):
    x,y=map(str, input().split())
    phoneBook[x]=y
   
while(True):
    try: 
        z = input()
        if(z in phoneBook):
            print("{}={}".format(z,phoneBook[z]))
        elif(z not in phoneBook and z!=""):
            print("Not found")
        else:
            break
    except EOFError:
        break
