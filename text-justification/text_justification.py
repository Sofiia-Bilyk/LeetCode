from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        start = 0

        while start < len(words):
            end = start + 1
            word_length = len(words[start])
            while end < len(words) and word_length + len(words[end]) + end - start <= maxWidth:
                word_length += len(words[end])
                end += 1

            line_words = words[start:end]
            gaps = len(line_words) - 1
            if end == len(words) or gaps == 0:
                result.append(" ".join(line_words).ljust(maxWidth))
            else:
                spaces, extra = divmod(maxWidth - word_length, gaps)
                parts = []
                for index, word in enumerate(line_words[:-1]):
                    parts.append(word)
                    parts.append(" " * (spaces + (1 if index < extra else 0)))
                parts.append(line_words[-1])
                result.append("".join(parts))

            start = end

        return result
