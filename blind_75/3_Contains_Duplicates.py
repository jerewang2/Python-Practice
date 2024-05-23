# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def containsDuplicate(nums):
    duplicates = {}

    for num in nums:
        if num in duplicates:
            return True
        else:
            duplicates[num] = 1
    return False

questions = ([1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
answers = (True, False, True)

for i in range(len(questions)):
    print(f'Question {i + 1}: {questions[i]} | Answer: {answers[i]}')
    print(f'My Answer: {containsDuplicate(questions[i])}')
