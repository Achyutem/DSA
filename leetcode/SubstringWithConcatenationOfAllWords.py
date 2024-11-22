# https://leetcode.com/problems/substring-with-concatenation-of-all-words


# Two-pointer Solution


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        word_count = len(words)
        word_map = collections.Counter(words)
        result = []

        total_length = word_length * word_count

        for i in range(word_length):
            left = i
            right = i
            current_map = collections.Counter()

            while right + word_length <= len(s):
                word = s[right : right + word_length]
                right += word_length

                if word in word_map:
                    current_map[word] += 1

                    while current_map[word] > word_map[word]:
                        left_word = s[left : left + word_length]
                        current_map[left_word] -= 1
                        left += word_length

                    if right - left == total_length:
                        result.append(left)
                else:
                    left = right
                    current_map.clear()

        return result


# Bruteforce solution


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        wordLen = len("".join(words))
        start = 0
        res = []
        word = len(words[0])
        wordCount = len(words)

        while start + wordLen <= len(s):
            current_slice = s[start : start + wordLen]
            words_copy = words[:]
            localcount = 0

            for i in range(0, wordLen, word):
                current_word = current_slice[i : i + word]
                if current_word in words_copy:
                    words_copy.remove(current_word)
                    localcount += 1
                else:
                    break

            if localcount == wordCount:
                res.append(start)

            start += 1

        return res
