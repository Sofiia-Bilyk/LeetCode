class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for character in s:
            if character.isalnum():
                new_s += character
        new_s=new_s.lower()
        print(new_s)
        length = len(new_s) // 2
        for i in range(length):
            print(new_s[i],new_s[i*(-1)-1])
            if new_s[i] != new_s[i*(-1)-1]:
                return False
        return True
