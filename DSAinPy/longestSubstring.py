# def subString(s):
#     last_seen = {}
#     left = 0
#     max_length = 0

#     for right, ch in enumerate(s):
#         if ch in last_seen and last_seen[ch] >= left:
#             left = last_seen[ch] + 1
        
#         last_seen[ch] = right
#         max_length = max(max_length, right - left + 1)

#     return max_length

# result = subString("abcdaa")
# print(result)


#----------------------------- With Input function --------------------------------
sttring = input("Enter a String: ")

last_nodiddu = {}
lefft = 0
max_len = 0

for rght, chr in enumerate(sttring):
    if chr in last_nodiddu and last_nodiddu[chr] >= lefft:
        lefft = last_nodiddu[chr] + 1

    last_nodiddu[chr] = rght
    max_len = max(max_len, rght - lefft + 1)

print(max_len)



