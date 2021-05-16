"""
今天，书店老板有一家店打算试营业customers.length分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
示例：
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner
"""
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
x = 3
customers_error = [2, 4, 1, 4, 1]
grumpy_error = [1, 0, 1, 0, 1]

# customers_error = [2, 4, 1, 4, 1]
# grumpy_error =    [1, 0, 1, 0, 1]

x_error = 2


# 10

def maxSatisfied(customers, grumpy, X):
    all_minutes = len(grumpy)
    max_save = 0
    current_happy = sum([v for i, v in enumerate(customers) if grumpy[i] == 0])
    # for left_index in range(all_minutes - X + 1):
    #     current_list = customers[left_index:left_index + X]
    #     save_guest = sum([v for i, v in enumerate(current_list) if grumpy[i + left_index] == 1])
    #     max_save = max(max_save, save_guest)
    # return current_happy + max_save
    current_unhappy = sum([v for i, v in enumerate(customers[:X]) if grumpy[i] == 1])
    max_save = current_unhappy
    for i in range(X, all_minutes):
        current_unhappy += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
        max_save = max(max_save, current_unhappy)
    # for left_index in range(all_minutes - X + 1):
    return current_happy + max_save


# maxSatisfied(customers, grumpy, x)
# maxSatisfied(customers_error, grumpy_error, x_error)
maxSatisfied(customers_error, grumpy_error, x_error)
