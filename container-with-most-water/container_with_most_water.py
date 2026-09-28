from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ### The first version passed 56/65 tests -> got Time Limit Exceeded message. This is a brute force algorithm, just checking all the possible solutions
        """
        current_max = 0
        for i in range(n-1):
            if height[i] * (n-1-i) > current_max:
                for j in range(-1, -n+i, -1):
                    if current_max < min(height[i], height[j]) * (n-i+j):
                        current_max =min(height[i], height[j]) * (n-i+j)
        return current_max
        """
        # Second version passed 60/65 -> Time Limit Exceeded
        """
        indeces = [] #the list if the indeces of the highest numbers in the descending order
        difference = 0 # between 2 heights
        max_v = 0 #result
        current_max_number = max(height)

        while max_v < current_max_number * (n-1):

            current_max_index = height.index(current_max_number)
            height[current_max_index] = 0 # changing to 0 to find the next maximum number on the next iteration

            #finding the biggest distance btw current_max_number and indeces in the list
            for index in indeces:
                difference = max(difference, abs(index - current_max_index))

            max_v = max(max_v, current_max_number*difference) # calculating if a new volume is biggest

            indeces.append(current_max_index)
            difference = 0
            current_max_number = max(height)

        return max_v
        """
        # Third version, 2 pointers approach
        max_v = 0
        s = 0
        e = n-1

        while s < e:
            max_v = max(max_v, min(height[s], height[e]) * (e - s))
            print("max_v: ", max_v)
            if height[s] < height[e]:
                current = height[s]
                while height[s] <= current and s < n:
                    s += 1
            else:
                current = height[e]
                while height[e] <= current and e >= 0:
                    e -= 1
        return max_v
