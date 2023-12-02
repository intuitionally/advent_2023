# with open('input_1.txt') as f:
#     lines = f.readlines()
#     total = 0
#     for l in lines:
#         l = l.strip()
#         number = ''
#         for x in l:
#             if x.isdigit():
#                 number += x
#                 break
#         for y in l[::-1]:
#             if y.isdigit():
#                 number += y
#                 break
#         total += int(number)
#     # print(total)

with open('input_1.txt') as f:
    lines = f.readlines()
    total = 0
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for l in lines:
        number = ''
        l = l.strip()
        for i, x in enumerate(l):
            if x.isdigit():
                number += x
                break
            elif l[i:i + 3] in nums:
                number += nums[l[i:i+3]]
                break
            elif l[i:i + 4] in nums:
                number += nums[l[i:i + 4]]
                break
            elif l[i:i + 5] in nums:
                number += nums[l[i:i + 5]]
                break
        for i, x in enumerate(l[::-1]):
            if x.isdigit():
                number += x
                break
            elif l[::-1][i:i + 3][::-1] in nums:
                number += nums[l[::-1][i:i + 3][::-1]]
                break
            elif l[::-1][i:i + 4][::-1] in nums:
                number += nums[l[::-1][i:i + 4][::-1]]
                break
            elif l[::-1][i:i + 5][::-1] in nums:
                number += nums[l[::-1][i:i + 5][::-1]]
                break
        total += int(number)
    print(total)
    