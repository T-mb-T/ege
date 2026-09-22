nums = [0] * 10000000
for n in range(1, 100000):
    b = bin(n)[2:]
    b += bin(n % 4)[2:]
    r = int(b, 2)
    nums[r] = 1
max_value = -float('inf')
for i in range(1, 100000 - 49):
    max_value = max(max_value, nums[i:i+49].count(1))
print(max_value)