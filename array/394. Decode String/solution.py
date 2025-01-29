class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c == ']':
                curStr = []
                # `[` にぶつかるまでポップ
                while stack and stack[-1] != '[':
                    curStr.insert(0, stack.pop())  # 逆順を防ぐために前に挿入
                stack.pop()  # `[` を取り除く
                
                # 数字を取得
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num  # 桁の順序を正しく修正
                
                # `curStr` を `int(num)` 回繰り返して `stack` に追加
                stack += curStr * int(num)
            else:
                stack.append(c)
        
        return "".join(stack)
