direction = input("Please enter your direction (up/down):")

if direction == "up":
    num = int(input("Please enter your top number:"))
    for i in range(1, num + 1):
        print(i)

elif direction == "down":
    num = int(input("Please enter your number below 20:"))
    for i in range(20, num - 1,-1):
        print(i)

else:
    print("I don't understand")
