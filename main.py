class Solution:
    def findMedianSortedArrays(self, a, b):
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
                if count == index_1:
                    ele_1 = a[i]
                if count == index_2:
                    ele_2 = a[i]
                count += 1
                i += 1
            else:
                if count == index_1:
                    ele_1 = b[j]
                if count == index_2:
                    ele_2 = b[j]
                count += 1
                j += 1

        while i < n1:
            if count == index_1:
                ele_1 = a[i]
            if count == index_2:
                ele_2 = a[i]
            count += 1
            i += 1

        while j < n2:
            if count == index_1:
                ele_1 = b[j]
            if count == index_2:
                ele_2 = b[j]
            count += 1
            j += 1

        if n % 2 == 0:
            return (ele_1 + ele_2) / 2.0

        return float(ele_2)

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    result = solution.findMedianSortedArrays([1, 3], [2])
    print(result)
