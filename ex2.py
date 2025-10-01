total=0

for i in range(5):  # 循环 5 次，因为用户要输入 5 个数字
    num = int(input(f"Enter number{i+1}:"))
    # 提示用户输入数字，并转成整数保存到 num
    # 注意这里用 {i+1} 来显示当前是第几个数字（从1开始）
    include = input("Do you want to include this number? (y/n):").lower()

    if include == "y":
        total += num

print("The total is:", total)
