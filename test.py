my_list = [1, 2, 3]
print(id(my_list[0]))  # 1のメモリアドレス（ID）
print(id(my_list[1]))  # 2のメモリアドレス（ID）

print(id(my_list))  # リストのメモリアドレス（ID）

# 1と2のメモリアドレスの差
print(id(my_list[1]) - id(my_list[0])) 