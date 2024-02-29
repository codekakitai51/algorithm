class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, s, m, e):
            L = arr[s:m+1]
            R = arr[m+1:e+1]

            j, k = 0, 0 # index for L and R arr
            i = s # index for original arr

            while j < len(L) and k < len(R):
                if L[j] <= R[k]:
                    arr[i] = L[j]
                    j += 1
                else:
                    arr[i] = R[k]
                    k += 1
                i += 1

            # for remaining arr
                # do not use slice for merging sorted arrays
                # # arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                # # insert = [0, 0, 0]

                # # arr[2:] = insert[0:]

                # # output -> [2, 3, 0, 0, 0]
            while j < len(L):
                arr[i] = L[j]
                j += 1
                i += 1
            while k < len(R):
                arr[i] = R[k]
                k += 1
                i += 1
            
            return arr

        def mergeSort(arr, s, e):
            if (e - s) + 1 <= 1:
                return arr
            
            m = (s + e) // 2

            mergeSort(arr, s, m)
            mergeSort(arr, m+1, e)
            merge(arr, s, m, e)

            return arr 

        return mergeSort(nums, 0, len(nums)-1)