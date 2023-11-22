from math import trunc
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
          line = []
          line_length = 0
           
          # Add word to len line until it reaches maxWidth
          while i < len(words) and line_length + len(words[i]) <= maxWidth:
            line.append(words[i])
            line_length += len(words[i]) + 1 # +1 For space between words
            i += 1
            
          # If line has only one word or last line, left justify
          if len(line) == 1 or i == len(words):
            result.append(" ".join(line).ljust(maxWidth))
          else:
            spaces = maxWidth - sum([len(word) for word in line])
            spaces_between_words, extra_spaces = divmod(spaces, len(line) - 1)
            justified_line = line[0]

            for j in range(1, len(line)):
                spaces = spaces_between_words + (extra_spaces > 0)
                justified_line += " " * spaces + line[j]
                extra_spaces -= 1 if extra_spaces > 0 else 0
            
            result.append(justified_line)

        return result
            
# Example 1:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
out = [
    "This    is    an",
    "example  of text",
    "justification.  "
    ]
s = Solution()
result = s.fullJustify(words, maxWidth)
print(result)
print(result == out)

# Example 2:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
out = [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
s = Solution()
result = s.fullJustify(words, maxWidth)
print(result)
print(result == out)

# Example 3:
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
out = [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
s = Solution()
result = s.fullJustify(words, maxWidth)
print(result)
print(result == out)

# Example 4
words = ["Listen","to","many,","speak","to","a","few."]
maxWidth = 6
out = ["Listen","to    ","many, ","speak ","to   a","few.  "]
s = Solution()
result = s.fullJustify(words, maxWidth)
print(result)
print(result == out)

# Example 5
words = ["a"]
maxWidth = 1
out = ["a"]
s = Solution()
result = s.fullJustify(words, maxWidth)
print(result)
print(result == out)

# Example 6
words = ["What","must","be","shall","be."]
maxWidth = 5
out = ["What ","must ","be   ","shall","be.  "]
s = Solution()
result = s.fullJustify(words, maxWidth)
print(result)
print(result == out)