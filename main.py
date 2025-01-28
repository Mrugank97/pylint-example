"""
Module for finding the median of two sorted arrays.

This module provides a solution to the problem of finding the median
of two sorted arrays. The `find_median_sorted_arrays` method combines
the arrays and finds the median value.
"""

class Solution:
    """
    Class to find the median of two sorted arrays.

    This class contains the method `find_median_sorted_arrays` which
    takes in two sorted arrays and returns their median.
    """
    
    def __init__(self):
        pass

    def find_median_sorted_arrays(self, a, b):
        """
        Find the median of two sorted arrays.

        This method merges two sorted arrays and returns the median value.
        
        Parameters:
        a (list): The first sorted array.
        b (list): The second sorted array.
        
        Returns:
        float: The median value of the two sorted arrays.
        """
        n1 = len(a)
        n2 = len(b)

        n = n1 + n2
        index_1 = n // 2 - 1
        index_2 = n // 2

        ele_1 = -1
        ele_2 = -1

        i = 0
        j = 0

        count = 0

        while i < n1 and j < n2:
            if a[i] < b[j]:
                ele_1, ele_2, count = self.update_elements(ele_1, ele_2, count, index_1, index_2, a[i])
                i += 1
            else:
                ele_1, ele_2, count = self.update_elements(ele_1, ele_2, count, index_1, index_2, b[j])
                j += 1

        while i < n1:
            ele_1, ele_2, count = self.update_elements(ele_1, ele_2, count, index_1, index_2, a[i])
            i += 1

        while j < n2:
            ele_1, ele_2, count = self.update_elements(ele_1, ele_2, count, index_1, index_2, b[j])
            j += 1

        if n % 2 == 0:
            return (ele_1 + ele_2) / 2.0

        return float(ele_2)

    def update_elements(self, ele_1, ele_2, count, index_1, index_2, val):
        """
        Helper method to update the elements based on count.
        
        Parameters:
        ele_1 (int): Previous first element.
        ele_2 (int): Previous second element.
        count (int): Current count.
        index_1 (int): Index of the first element.
        index_2 (int): Index of the second element.
        val (int): The value to be considered.
        
        Returns:
        tuple: Updated values of ele_1, ele_2, and count.
        """
        if count == index_1:
            ele_1 = val
        if count == index_2:
            ele_2 = val
        count += 1
        return ele_1, ele_2, count


# Example usage
if __name__ == "__main__":
    solution = Solution()
    result = solution.find_median_sorted_arrays([1, 3], [2])
    print(result)
