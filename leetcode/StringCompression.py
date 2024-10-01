# https://leetcode.com/problems/string-compression


class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        index = 0
        n = len(chars)

        for i in range(1, n + 1):
            if i < n and chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[index] = chars[i - 1]
                index += 1
                if count > 1:
                    for digit in str(count):
                        chars[index] = digit
                        index += 1
                count = 1
        return index
