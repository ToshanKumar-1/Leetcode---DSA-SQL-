class Solution(object):
    def twoSum(self, numbers, target):

        low, high = 0, len(numbers)-1

        while low <= high:
            if numbers[high] + numbers[low] == target:
                return [low+1, high+1]
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                low +=1
        