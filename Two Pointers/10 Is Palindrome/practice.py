import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i =0
        j = len(s) - 1
        
        all_letters = string.ascii_letters + string.digits
        while (i <= j):
             
            if s[i] not in all_letters:
                i+=1
                continue
            elif s[j] not in all_letters :
                j-=1
                continue
            else:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            
        return True
        

solution = Solution()
print(solution.isPalindrome("Was it a car or a cat I saw?"))
print(solution.isPalindrome("tab a cat"))
print(solution.isPalindrome("0P"))


# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true

# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false

# Explanation: "tabacat" is not a palindrome.