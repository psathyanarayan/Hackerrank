#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are #given  scores. Store them in a list and find the score of the runner-up.
#The first line contains n . The second line contains an array A[]   of n integers each separated by a space.
#Given list is [2,3,6,6,5] . The maximum score is 6 , second maximum is 5 . Hence, we print 5 as the runner-up score.



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if n in range(2,11) :
            a=sorted(arr)
            na = set(a)
            na.remove(max(a))
            print(max(na))
            break
