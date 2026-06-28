"""closet number"""

def closest(n,m):
    close=0
    minmum=float('inf')

    for i in range(n-abs(m),n+abs(m)+1):
        if i%m==0:
            minn=abs(n-i)
            print(minn)
            if minn<minmum or minn==minmum:
                minmum=minn
                close=i 
    return close
print(closest(13,4))