# ! py -3
# -*- coding: utf8 -*-


guess = 0
secret = 7
times = 1

print("-----------------欢迎参加猜数字游戏，请开始-------------------")
while guess != secret:
    guess = int(input("@数字区间0-9，请输入你猜的数字："))
    print("你猜的数字是：", guess)
    if guess == secret:
        print("你猜了{}次，猜对了，好腻害".format(times))
    else:
        if guess < secret:
            print("你猜的数字小于正确答案")
        else:
            print("你猜的数字大于正确答案")

    times += 1

print("游戏结束")