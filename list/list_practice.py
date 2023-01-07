# jon_snow = ['Jon Snow', 'Winterfell', 30]
#
# for i in range(len(jon_snow)):
#     print(jon_snow[i])
#
# jon_snow[0] = 'Quinn'
# print(len(jon_snow))
# jon_snow[2] += 5
#
# print('After changing:')
# for i in range(len(jon_snow)):
#     print(jon_snow[i])
#
# print("--------")
# num_seq = range(3, 20, 3)
# for num in num_seq:
#     print(num)
#
#
# # list inside another list
# world_cup_winner = [[2006, 'Italy'], [2010, 'Spain'], [2014, 'Germany'], [2018, 'France']]
#
# for i in range(len(world_cup_winner)):
#     print(world_cup_winner[i])
#
# print("--------")
# # 2D array
#
# my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(my_matrix)):
#     for j in range(len(my_matrix[i])):
#         print(my_matrix[i][j], end=" ")
#     print()
#
# print("----------")
#
#
# # merge list
# part_A = [1, 2, 3, 4, 5]
# print("List A: ", part_A)
# part_B = [6, 7, 8, 9, 10]
# print("List B:", part_B)
# merged_list = part_A + part_B
# print("Merged list: ", merged_list)
# print("----------")
#
# my_list = [1, 2, 3, 4]
# print(my_list)
# my_list.append(5)
# my_list.append(6)
# print(my_list)
# my_list.insert(3, 17)
# print(my_list)
#
# my_list.pop()
# print(my_list)
# my_list.remove(3)
# print(my_list)
#
# # list slicing
# print(my_list[-1])
# print(my_list[0:2])
# print(my_list.index(17))
#
# another_list = [2, 5, 9, 10, 15, -9, 100, 250, 69]
# another_list.sort()
# print(another_list)


nums = [10, 20, 30, 40, 50]
nums_doubled = [n * 2 for n in nums]
# for n in nums:
#     nums_doubled.append(n * 2)

print(nums)
print(nums_doubled)