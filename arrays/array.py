"""find the second largest"""
arr=[10,6,7,8,19]

# new=sorted(arr)
# print(new[-2])
lar=arr[0]
sec=arr[0]
for num in arr:
    if num > lar:
        sec=lar
        lar=num
        

# print(lar)
print(sec)