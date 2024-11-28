#https://leetcode.com/problems/missing-number


#Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = (n * (n + 1)) // 2
        actualSum = 0

        for i in nums:
            actualSum += i

        res = expectedSum - actualSum
        return res

#Golang
func missingNumber(nums []int) int {
    n := len(nums)
    expectedSum := (n * (n+1)) / 2
    actualSum := 0

    for _,i :=  range nums {
        actualSum += i
    }

    return expectedSum - actualSum

}
