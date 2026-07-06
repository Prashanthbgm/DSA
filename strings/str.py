# sentence=[["i love that gril very much"],["but she doesnt understand me"],["i also failed to understand her"]]

# for sentens in sentence:
#     maxword=0
#     comp_senc=" "
#     if len(sentens[0].split())>maxword:
#         maxword=len(sentens[0].split())
#         comp_senc=" ".join(sentens)
# print(maxword)
# print(comp_senc)


# """find max unique string"""
# sentence=[
#     ["good","good","bad"],
#     ["good","bad"],
#     ["good"]
#     ]

# for ch in sentence:
#     count=0
#     max_count=0
#     words=" "
#     for char in set(ch):
#         word=set()
#         if char in word:
#             count+=1
#         word.add(char)
#         if count>max_count:
#             words=word
#     print(max_count)
#     print(words)
"""Strings revisions"""
"""reverse string"""
# strs="Prashanth"

# # print(strs[::-1])
# left=0
# right=len(strs)-1

# while left<right:
#     strs[left],strs[right]=strs[right],strs[left]
#     left+=1
#     right-=1
"""reverse the words"""
# sentence="hi Prashanth M"

# left=0
# right=len(sentence)-1

# while left<right:
#     sentence[left],sentence[right]=sentence[right],sentence[left]
#     left+=1
#     right-=1

# print(sentence[0])
# words=sentence.split()

# print(words)

# w=" ".join(words[::-1]) 
# print(w)

# result=""
# current_w=""

# for i in range(len(sentence)-1,-1,-1):
#     char=sentence[i]
#     # print(char,end="")

#     if char !=" ":
#         current_w=char+current_w
#         print(current_w)
#     else:
#         if current_w!="":
#             if result=="":
#                 result=current_w
#             else:
#                 result=result+" "+current_w
#         current_w=""

   
# if current_w!="":
#     if result=="":
#         result=current_w
#     else:
#         result=result+" "+current_w
# print(result)
"""Palindrome or not """
# sentence="AMMA"

# left=0
# right=len(sentence)-1
# is_plan=True
# while left<right:
#     if sentence[left]!=sentence[right]:
#         is_plan=False
#         print("its not a palindrome")
#         break
#     left+=1
#     right-=1
# if is_plan:
#     print("its a palindrome")
"""Count the Vowels"""
# sentence="Appa"
# s=set(sentence.lower())
# check={"a","e","i","o","u"}
# count=0
# for ch in s:
#     if ch in check:
#         count+=1
# print(count)
"""Count the words in sentence"""
# sentence="My appa is my hero"

# count=0

# for ch in range(len(sentence)):
#     if sentence[ch]==" ":
#         count+=1
#     if sentence[ch]==sentence[-1]:
#         count+=1
# print(count)