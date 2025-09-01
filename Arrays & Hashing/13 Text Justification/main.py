from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        line, length = [], 0
        i = 0

        while i < len(words):
            
            if length + len(line) + len(words[i]) > maxWidth:
                
                total_space = maxWidth-length
                
                space_size = total_space//max(1, len(line)-1)
                reminder = total_space% max(1, len(line)-1)
                
                for j in range(max(1, len(line)-1)):
                    line[j] += " "*space_size
                    if reminder:
                        line[j] += " "
                        reminder -= 1
                res.append("".join(line))

                line, length = [], 0
            
            line.append(words[i])
            length += len(words[i])
            i+=1

        last_line = " ".join(line)
        trail_space = maxWidth-len(last_line)
        res.append(last_line+" "*(trail_space))
        return res



    
    def fullJustify1(self, words: List[str], maxWidth: int) -> List[str]:
        page = []
        line: list[str] = []
        wordCount = 0
        spaces = 0
        wordCountMap = {}

        for word in words:
            wordCount += len(word)
            if wordCount+spaces > maxWidth:
                page.append(line)
                wordCountMap[len(page)-1] = wordCount-len(word)
                line = []
                wordCount = len(word)
                spaces = 0
            
            spaces += 1
            line.append(word)
        if line:
            page.append(line)
            wordCountMap[len(page)-1] = wordCount
            

        res = []

        for i, line in enumerate(page):
            if i == len(page)-1:
                res.append(" ".join(line)+(" "*(maxWidth - (wordCountMap[i] + len(page[i])-1))))
            else:
                res.append(self.justify(line, maxWidth-wordCountMap[i]))
        
        return res
        

    def justify(self, line, space):
        if len(line) == 1:
            return line[0]+(" "*space)
        gaps = len(line)-1
        space_size = space//gaps
        rem = space%gaps

        for i in range(rem):
            line[i] = line[i]+" "
        
        return (" "*space_size).join(line)
            


# Text Justification
# You are given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
# Example 1:

# Input: words = ["This","is","an","example","of","text","justification."], maxWidth = 16

# Output: [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16

# Output: [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be " instead of "shall be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:

# Input: words = 

# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20

# Output: [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
# Constraints:

# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
