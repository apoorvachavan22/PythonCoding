Minimum Element After Replacement With Digit Sum:

You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

 

Example 1:

Input: nums = [10,12,13,14]

Output: 1

Explanation:

nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

Example 2:

Input: nums = [1,2,3,4]

Output: 1

Explanation:

nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

Example 3:

Input: nums = [999,19,199]

Output: 10

Explanation:

nums becomes [27, 10, 19] after all replacements, with minimum element 10.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 104

-----------------------------------------------------------------------------------------------------------------------
class Solution:
    def  minElementAfterSumOfDigits(self, nums:list[int])->int:
        min_sum=float('inf')
        for i in range(len(nums)):
            sum = 0
            while nums[i] > 0:
                dig_sum += nums[i] % 10
                nums[i] //= 10
            min_sum=min(min_sum,dig_sum)
        return min_sum
if __name__ == "__main__":
    sol = Solution()
    nums = []
    input_size = int(input("Enter the size of the array: "))
    for i in range(input_size):
        nums.append(int(input("Enter the element: ")))
#    nums = [999,13,9,56,11]
    print(f"The minimum element after sum of digits is: {sol.minElementAfterSumOfDigits(nums)}")
