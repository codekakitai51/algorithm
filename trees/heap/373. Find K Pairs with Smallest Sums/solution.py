import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # ヒープの初期化
        heap = [(nums1[0] + nums2[0], 0, 0)]
        res = []
        visited = set()
        visited.add((0, 0))

        while len(res) < k and heap:
            curSum, n1, n2 = heapq.heappop(heap)
            res.append([nums1[n1], nums2[n2]])

            # 次の候補ペアをヒープに追加
            if n1 + 1 < len(nums1) and (n1 + 1, n2) not in visited:
                heapq.heappush(heap, (nums1[n1 + 1] + nums2[n2], n1 + 1, n2))
                visited.add((n1 + 1, n2))

            if n2 + 1 < len(nums2) and (n1, n2 + 1) not in visited:
                heapq.heappush(heap, (nums1[n1] + nums2[n2 + 1], n1, n2 + 1))
                visited.add((n1, n2 + 1))

        return res

# too slow -> O(n * m * log H)
        # sumMap = {} # sum: [pair1, pair2...]
        # sumHeap = []
        # for n1 in nums1:
        #     for n2 in nums2:
        #         curSum = n1 + n2
        #         if curSum in sumMap:
        #             sumMap[curSum].append([n1, n2])
        #         else:
        #             sumMap[curSum] = [[n1, n2]]
        #             heapq.heappush(sumHeap, curSum)
                
        # count = 0
        # res = []
        # while count < k:
        #     curSum = heapq.heappop(sumHeap)

        #     for pair in sumMap[curSum]:
        #         if len(sumMap[curSum]) > 1:
        #             if count >= k:
        #                 return res
        #             res.append(pair)
        #             count += 1
        #         else:
        #             res.append(pair)
        #             count += 1

        # return res


        