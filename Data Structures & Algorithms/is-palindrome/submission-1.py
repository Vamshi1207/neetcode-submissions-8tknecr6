class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_chars = [char for char in s if char.isalnum()]
        print(clean_chars)
        i = 0
        j = len(clean_chars) - 1       

        while i <= j:

            if clean_chars[i].lower() == clean_chars[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

