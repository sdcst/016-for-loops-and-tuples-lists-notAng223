#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
nums = (5,-2,12,-8,14,16)

for i in range(0, len(nums)):
    num = nums[i]
    if num>=0:
        print("the number "+str(num)+" square root is ",round(num**0.5, 3))