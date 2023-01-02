def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return [-1, -1]


# more optimal approach with map
def two_sum_map(nums, target):
    map = {}
    for i in range (0, len(nums)):
        complement = target - nums[i]
        if complement in map:
            return [i, map.get(complement)]
        map[nums[i]] = i
    return [-1, -1]

print(two_sum([1, 2, 3, 4], 6))
print(two_sum_map([1, 2, 3, 4], 6))

# learn about array and for loop

# nums = [1, 2, 3, 4]
#
# for i in range(0, len(nums)):
#     print(nums[i])
