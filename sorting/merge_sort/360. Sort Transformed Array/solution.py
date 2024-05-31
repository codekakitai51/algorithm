class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []
        for n in nums:
            res.append(a * n ** 2 + b * n + c)

        def mergeSort(arr, s, e):
            if e - s + 1 <= 1:
                return arr

            # The middle index of the array
            m = (s + e) // 2

            # Sort the left half
            mergeSort(arr, s, m)

            # Sort the right half
            mergeSort(arr, m + 1, e)

            # Merge sorted halfs
            merge(arr, s, m, e)
            
            return arr

        # Merge in-place
        def merge(arr, s, m, e):
            # Copy the sorted left & right halfs to temp arrays
            L = arr[s: m + 1]
            R = arr[m + 1: e + 1]

            i = 0 # index for L
            j = 0 # index for R
            k = s # index for arr

            # Merge the two sorted halfs into the original array
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # One of the halfs will have elements remaining
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        res = mergeSort(res, 0, len(res) - 1)
        return res


