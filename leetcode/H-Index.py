class Solution:
    def hIndex(self, citations):
        # def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i in range(n):
            if citations[i] >= n - i:
                return n - i

        return 0


solution = Solution()
print(solution.hIndex([3, 0, 6, 1, 5]))  # Output: 3
