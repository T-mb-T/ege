nums = list(map(int, open('Пример 1.txt').readlines()))
count32 = 0
for num in nums:
    if abs(num) % 32 == 0:
        count32 += 1

count = 0
m = -100000
for i in range(len(nums) - 1):
    if (nums[i] < 0 or nums[i + 1] < 0) and nums[i] + nums[i + 1] < count32:
        count += 1
        if nums[i] + nums[i + 1] > m:
            m = nums[i] + nums[i + 1]
print(count, m) # 5897 357