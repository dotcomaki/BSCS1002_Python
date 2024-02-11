'''
Accept a sequence of comma-separated integers as input and print the maximum value in the sequence as output.
'''

nums = input()
nums = nums.split(',')

max_num = int(nums[0])
for num in nums:
    num = int(num)
    if num > max_num:
        max_num = num
        
print(max_num)
