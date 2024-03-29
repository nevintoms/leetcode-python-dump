'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

'''
O(n) Memory - This question can be done using O(n) memory if both postfix and prefix array are maintained.
O(1) Memory - This question can be done using O(1) memory if prefix and postfix are done on the same array using forward and backward pass. 
'''

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    out = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        out[i] = prefix
        prefix = prefix * nums[i]
    postfix = 1
    for i in range(len(out)-1, -1, -1):
        out[i] = postfix * out[i]
        postfix = postfix * nums[i]

    return out

print(productExceptSelf([1,2,3,4]))
