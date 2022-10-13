for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    cost1=x1+y1
    cost2=x2+y2
    if cost1>cost2:
        print(cost2)
    else:
        print(cost1)