# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

def two_sums(nums, target):
    if len(nums) == 0:
        return []

    for ind, num in enumerate(nums):
        for next_ind, new_num in enumerate(nums):
            if ind == next_ind:
                continue
            elif (num + new_num) == target:
                return [ind, next_ind]

questions = ([2, 7, 11, 15], [3, 2, 4], [3, 3])
targets = (9, 6, 6)
answers = ([0, 1], [1, 2], [0, 1])

for i in range(len(questions)):
    print(f'Question {i + 1}: {questions[i]} | Answer: {answers[i]}')
    print(f'My Answer: {two_sums(questions[i], targets[i])}\n')
