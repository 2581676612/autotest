# """
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
# 返回仅包含 1 的最长（连续）子数组的长度。
# """
# k = 3
test_list = [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# l = [2, 2, 2, 3, 1, 2, 3, 4]
# distance_list = [2, 2, 1, 3]
# count_list = [2, 3, 2, 4]
# # 2 + 2(3) + 3 + 1(3) + 2
# # new_list = list(enumerate(test_list))
# # print(new_list)
# new_list = []
# count = 1
# for t in range(len(test_list) - 1):
#     if test_list[t] == test_list[t + 1]:
#         count += 1
#     else:
#         new_list.append(count)
#         count = 1
# new_list.append(count)
# if test_list[0] == 0:
#     begin_0 = new_list[::2]
#     begin_1 = new_list[1::2]
#     print(begin_0)
#     print(begin_1)
#     max_count = 0
#     for i in range(len(begin_1)):
#         k = 3
#         current_count = begin_1[i]
#         for j in range(i, len(begin_0)):
#             if begin_0[j] < k:
#                 k -= begin_0[j]
#                 if i == 0:
#                     current_count += begin_0[j]
#                 else:
#                     current_count += (begin_0[j] + begin_1[i - 1])
#             elif begin_0[j] > k:
#                 current_count += k
#                 break
#             elif begin_0[j] == k:
#                 current_count += (k + begin_1[i - 1])
#                 break
#         max_count = max_count if current_count < max_count else current_count
# else:
#     begin_0 = new_list[1::2]
#     begin_1 = new_list[::2]
#     max_count = 0
#     for i in range(len(begin_1)):
#         k = 3
#         current_count = begin_1[i]
#         for j in range(len(begin_0)):
#             if begin_0[j] < k:
#                 k -= begin_0[j]
#                 current_count += begin_0[j]
#             else:
#                 current_count += k
#                 break
#         max_count = max_count if current_count < max_count else current_count
# print(max_count)

"""重点：题意转换。把「最多可以把 K 个 0 变成 1，求仅包含 1 的最长子数组的长度」转换为 「找出一个最长的子数组，该子数组内最多允许有 K 个 0 」。"""

left_index, zeros, max_count = 0, 0, 0
for i in range(len(test_list)):
    if test_list[i] == 0:
        zeros += 1
    while zeros > 3:
        if test_list[left_index] == 0:
            zeros -= 1
        left_index += 1
    max_count = max(max_count, i - left_index + 1)
print(max_count)
