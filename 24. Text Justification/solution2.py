from math import trunc
from typing import List


class Solution:
    def last_line(self, words: List[str], maxWidth: int, start: int) -> str:
        line = ""
        line = " ".join(words[start:])
        if line: line += " "*(maxWidth - len(line))
        return line
    def create_line(self, words: List[str], maxWidth: int, line_letters: int, tabs: int, start: int, end: int) -> str:
        line = ""
        line_spaces = 0
        # Calculate spaces per tab
        total_spaces = maxWidth - line_letters
        if tabs > 0: 
            spaces_per_tab = trunc(total_spaces / tabs)
            remain = total_spaces % tabs
        else:
            spaces_per_tab = 0
            remain = 0
        for i in range(start, end):
            line += words[i]
            if tabs and spaces_per_tab > 0:
                line += " "*spaces_per_tab
                line_spaces += spaces_per_tab
                tabs -= 1
            if remain > 0:
                line += " "
                line_spaces += 1
                remain -= 1
        n = line_letters + line_spaces
        if n < maxWidth: line += " "*(maxWidth - n)
        return line
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_letters, word_count, tabs = 0, 0, 0

        if len(words) == 0: return ""
        if len(words) == 1:
            if maxWidth < len(words[0]): return ""
            else: 
                # Complete the last line, left-justified plus spaces till maxWidth
                last = self.last_line(words, maxWidth, 0)
                if last: 
                    result.append(last)
                    return result

        for i, word in enumerate(words):
            n = len(word)
            
            if line_letters + n + (tabs + 1) > maxWidth:
                line = self.create_line(words, maxWidth, line_letters, tabs, i - word_count, i)
                if line_letters > 0: result.append(line)
                line_letters = 0
                word_count = 0
                tabs = 0
            line_letters += n
            word_count += 1
            tabs = word_count - 1
            
        # Complete the last line, left-justified plus spaces till maxWidth
        last = self.last_line(words, maxWidth, i - word_count + 1)
        if last: result.append(last)
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