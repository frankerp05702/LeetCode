from typing import List


class Solution:
    def registerWords(self, s: str, current: int, start: int, ml: int, word_occurrences):
        r_occ = {}
        # Register words
        while current >= start:
            word = self.getWordByIndex(s, current, ml)
            current -= ml
            if word in word_occurrences:
                if word in r_occ: r_occ[word] += 1
                else: r_occ[word] = 1
        return r_occ
    def getWordByIndex(self, s: str, current: int, ml: int) -> str:
        word = ""
        for i in range(current, current + ml):
            word += s[i]
        return word
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        ml = len(words[0])
        substr_len = m * ml

        if substr_len > n or not s or not words or ml < 1: 
            return []
        
        # Register word occurrences
        word_occurrences = {}
        for word in words:
            if word in word_occurrences: word_occurrences[word] += 1
            else: word_occurrences[word] = 1

        result = []
        r_occ = {}
        for end in range(n - 1, substr_len - 2, -1):
            start = end - substr_len + 1
            if end == n-1:
                # Register words
                r_occ = self.registerWords(s, end + 1 - ml, start, ml, word_occurrences)
            else:
                word = self.getWordByIndex(s, start, ml)
                if word in word_occurrences:
                    # Register words
                    r_occ = self.registerWords(s, end + 1 - ml, start, ml, word_occurrences)
            # If all occurrences match, append start to result
            match = True
            for key in word_occurrences.keys():
                if key not in r_occ or r_occ[key] < word_occurrences[key]:
                    match = False
                    break
            if match:
                result.append(start)
            # Unregister word that will be out of range in next iteration
            to_delete = self.getWordByIndex(s, end - ml + 1, ml)
            if to_delete in r_occ:
                if r_occ[to_delete] > 1:
                    r_occ[to_delete] -= 1
                else:
                    del r_occ[to_delete]

        result.sort()
        return result

# Example 1:
s = "barfoothefoobarman"
words = ["foo","bar"]
# Output: [0,9]
# Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
# The output order does not matter. Returning [9,0] is fine too.
sol = Solution()
result = sol.findSubstring(s, words)
print(result)
print(result == [0,9])

# Example 2:
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
# Output: []
# Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
# There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
# We return an empty array.
sol = Solution()
result = sol.findSubstring(s, words)
print(result)
print(result == [])

# Example 3:
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# Output: [6,9,12]
# Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
sol = Solution()
result = sol.findSubstring(s, words)
print(result)
print(result == [6,9,12])

# Example 4:
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
# Output: [8]
# Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
sol = Solution()
result = sol.findSubstring(s, words)
print(result)
print(result == [8])

# Example 5:
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
# Output: [13]
# Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
sol = Solution()
result = sol.findSubstring(s, words)
print(result)
print(result == [13])

# Example 6:
s = "ababababab"
words = ["ababa","babab"]
# Output: [0]
# Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
sol = Solution()
result = sol.findSubstring(s, words)
print(result)
print(result == [0])

# Example 7:
s = "ababaab"
words = ["ab","ba","ba"]
# Output: [1]
# Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
sol = Solution()
result = sol.findSubstring(s, words)
print(result)
print(result == [1])