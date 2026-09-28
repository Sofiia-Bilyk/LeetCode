from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #Option 1  Time Limit Exceeded
        '''
        if len(s) == 0:
            return True
        for word in wordDict:
            if word in s:
                position = s.find(word)
                if self.wordBreak(s[0:position], wordDict) and self.wordBreak(s[position+len(word):], wordDict):
                    return True
        return False
        '''
        # Option 2
        '''
        first_letter_dict = {}
        letters_list = []
        for word in wordDict:
            for letter in word:
                if letter not in letters_list:
                    letters_list.append(letter)
            if word[0] not in first_letter_dict:
                first_letter_dict[word[0]] = [word]
            else:
                first_letter_dict[word[0]].append(word)

        print(first_letter_dict)

        for letter in s:
            if letter not in letters_list:
                return False

        def recursive_division(position):
            if s[position] in first_letter_dict:
                for word in first_letter_dict[s[position]]:
                    if word == s[position:position+len(word)]:
                        position = position+len(word)
                        if position >= len(s):
                            return True
                        else:
                            if recursive_division(position):
                                return True
                        position -= len(word)
            return False
        return(recursive_division(0))
        '''
        #Option 3
        '''
        letters = []
        max_length = 0
        short_wordDict = []
        for word in wordDict:
            if word*2 in wordDict:
                continue
            short_wordDict.append(word)
            max_length = max(max_length, len(word))
            for letter in word:
                if letter not in letters:
                    letters.append(letter)

        short_wordDict.reverse()
        print("Shortened: ", short_wordDict)
        for letter in s:
            if letter not in letters:
                return False


        q = deque([s])
        while q:
            i = 1
            s = q.popleft()
            length = len(s)
            while i <= length and i <= max_length:
                if s[:i] in short_wordDict:
                    q.append(s[i:])
                    if i == length:
                        return True
                elif s[:i] in wordDict:
                    q.append(s[i:])
                    if i == length:
                        return True
                i += 1
        return False
        '''
        #Option 4
        # Creating dictionary of words, sorted by the first letter
        first_letter_dict = {}
        for word in wordDict:
            if word[0] not in first_letter_dict:
                first_letter_dict[word[0]] = [word]
            else:
                first_letter_dict[word[0]].append(word)

        dp = [False] * len(s) # the values will be updated to True, if substring[0:True-value] is divisible by words from wordDict
        i = 0
        while i < len(s):
            if dp[i-1] == True or i == 0:
                if s[i] in first_letter_dict:
                    for word in first_letter_dict[s[i]]:
                        if word == s[i:i+len(word)]:
                            dp[i+len(word)-1] = True
            i += 1
        return dp[-1]
