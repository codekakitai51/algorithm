# 言い換えるのが鍵

n = int(input())
n -= 1
box = []

while n:
  box.append(n % 5)
  n //= 5
  
if not box:
  box.append(0)
  
box.reverse()
for ele in box:
  print(ele * 2, end="")