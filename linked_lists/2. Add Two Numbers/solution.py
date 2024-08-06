# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # ダミーヘッドノードを作成
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        # l1とl2が両方ともNoneになるまでループ
        while l1 or l2:
            # 各リストからの値を取得、ない場合は0とする
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 合計とキャリーの計算
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10

            # 新しいノードを作成しリストに追加
            current.next = ListNode(new_digit)
            current = current.next

            # l1とl2を次に進める
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 最後にキャリーが残っている場合は追加
        if carry:
            current.next = ListNode(carry)

        # ダミーヘッドの次のノードが実際の開始位置
        return dummy_head.next
