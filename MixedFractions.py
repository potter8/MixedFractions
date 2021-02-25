while(True):
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    else:
        whole_num = int(x/y)
        remainder = int(x%y)
        print(str(whole_num) +" "+str(remainder) + " / " + str(y))