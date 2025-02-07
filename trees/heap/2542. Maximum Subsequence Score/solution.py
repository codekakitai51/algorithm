class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[-1])

        num1Heap = [x[0] for x in pairs[:k]]
        num1Sum = sum(num1Heap)
        heapq.heapify(num1Heap)

        ans = num1Sum * pairs[k - 1][1]

        for i in range(k, len(nums2)):
            num1Sum -= heapq.heappop(num1Heap)
            num1Sum += pairs[i][0]
            heapq.heappush(num1Heap, pairs[i][0])

            ans = max(ans, num1Sum * pairs[i][1])
        
        return ans