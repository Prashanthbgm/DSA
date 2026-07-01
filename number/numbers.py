"""closet number"""
"""
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
"""
# n=0
# count=0
# while n>=0:
#     val=n%10
#     n=n//10
#     count+=1
#     if n==0:
#         break
#     print(val)
# print(count)

"""consecutive numbers"""
"""brute force"""
"""def consecutive(num):
    
    for i in range(1,num):
        check=0
        for j in range(i,num):
            check+=j
            if check==num:
                print("yes consecutive")
                for k in range(i,j+1):
                    print(k,end=" ")
                return True

            elif check>num:
                break
    return False 

print(consecutive(10))"""

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(60,90))

    