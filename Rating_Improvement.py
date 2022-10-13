for _ in range(int(input())):
    X,Y=map(int,input().split())
    V=X+200
    if V>=Y and Y>=X:
        print("YES")
    else:
        print("NO")
