"""Find the largest and second largest"""

arr=[2,4,5,6,7,10,9]
largest=0
second_largest=0
for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
    
print(second_largest)

"""first unique element in array"""
arr=[1,2,3,1,3,4]
left=0
for i in range(len(arr)):
    if arr[left]!=arr[i]:
        print("unique element",arr[left])
    
    left+=1
print("not")

"""find hcf and lcm """
ans=0
def hcf(a,b):
    ans=0
    lcm=0
    if a==0 or b==0:
        return 0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            ans=i
    lcm=(a*b)//ans
    return ans,lcm
print(hcf(6,12))

"""Amstrong numbers"""
number=153
num=number
lens=len(str(number))
print(lens)
total=0

while number>0:
    digit=number%10
    print(digit**lens)
    total+=digit**lens
    number=number//10

print(total)
print(number)
if num==total:
    print("yes")
"""palindrome or not"""
strs="byym"
left=0
right=len(strs)-1

while left<right:
    if strs[left]==strs[right]:
        left+=1
        right-=1
    else:
        print("not")
        break
print("palindrome")     
    
strs="amma"

strs.lower()

if strs[::-1]==strs:
    print("plaindrome")
else:
    print("not")
"""find the min and max value in an array"""
arr=list(map(int,input("enter ele with space:  ").split()))

# """ minmum and maximum in arr
arr=[1,2,3,4,5]
mins=arr[0]
maxs=arr[0]

for i in range(len(arr)):
    if arr[i]>maxs:
        maxs=arr[i]
    if arr[i]<mins:
        mins=arr[i]
print(mins)
print(maxs)
# """
# """ array rotation
left=0
right=len(arr)-1

while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1

print(str(arr))
# """
# """array rotation for n numbers
left=0
right=len(arr)-1
n_rotat=2

while left<n_rotat:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)
"""array running sums"""


for i in range(1,len(arr)):
    arr[i]=arr[i]+arr[i-1]
print(arr)


def max_response(days):
    freq = {}

    for day in days:
        unique_responses = set(day)   # remove duplicates in same day
   
        for response in unique_responses:
            freq[response] = freq.get(response, 0) + 1

    return max(freq, key=freq.get)



responses = [
    ["good", "good", "bad"],
    ["good", "ok", "ok"],
    ["good", "bad"]
]

print(max_response(responses))

