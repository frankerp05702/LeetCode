from math import trunc
from typing import List


class Solution:
    def line_format(self, words: List[str], maxWidth: int):
        format = []
        line_words, line_letters, line_spaces = 0, 0, 0
        for w in words:
            line_spaces = line_words - 1
            if line_letters + len(w) + (line_spaces + 1) > maxWidth:
                total_spaces = maxWidth - line_letters
                if line_spaces > 0: 
                    spaces_per_tab = trunc(total_spaces / line_spaces)
                    remain = total_spaces % line_spaces
                else: 
                    spaces_per_tab = total_spaces
                    remain = 0
                format.append({
                    "line_words": line_words,
                    "line_letters": line_letters,
                    "line_spaces": line_spaces,
                    "spaces_per_tab": spaces_per_tab,
                    "remain": remain
                })
                line_letters = 0
                line_words = 0
            line_letters += len(w)
            line_words += 1
        return format
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        format = self.line_format(words, maxWidth)
        index = 0
        n = len(format) + 1
        result = [""]*n
        word_count = 0
        for line_count, line in enumerate(format):
            tabs = line["line_spaces"]
            remain = line["remain"]
            for times in range(line["line_words"]):
                result[line_count] += words[word_count]
                if tabs > 0:
                    result[line_count] += " "*line["spaces_per_tab"]
                    tabs -= 1
                if remain > 0:
                    result[line_count] += " "
                    remain -= 1 
                word_count += 1
            result[line_count] += " "*(maxWidth-len(result[line_count]))
        result[n-1] += " ".join(words[word_count:])
        result[n-1] += " "*(maxWidth-len(result[n-1]))
        print(format)
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