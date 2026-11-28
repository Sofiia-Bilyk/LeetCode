class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        if not negative:
            x = -x

        # Accumulate a nonpositive result so -2**31 stays representable.
        last_digit_limit = -8 if negative else -7
        result = 0
        while x:
            quotient, digit = divmod(x, -10)
            x = -quotient
            if result < -214_748_364 or (
                result == -214_748_364 and digit < last_digit_limit
            ):
                return 0
            result = result * 10 + digit

        return result if negative else -result
