# Решение
nums = list(map(int, open("Задание 1701.txt").readlines()))
minnum = -9999
for num in nums:
    if num < 0 and abs(num) % 9 == 0 and len(str(num)) == 5 and num > minnum:
        minnum = num

count = 0
m = 100000000
for i in range(len(nums) - 1):
    if ((nums[i] < 0 and nums[i + 1] >= 0) or (nums[i] >= 0 and nums[i + 1] < 0)) and nums[i] + nums[i + 1] > minnum:
        count += 1
        m1 = nums[i] ** 2 + nums[i + 1] ** 2
        if m1 < m:
            m = m1
print(count)
print(m)


answer1 = 2627
answer2 = 504410

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1701, f'{answer1} {answer2}', 'b73de31c02e01cfc4508d15f2cf61e69'))