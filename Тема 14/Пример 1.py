x = 7 * 512 ** 120 - 6 * 64 * 100 + 8 ** 210 - 255
count = 0
while x > 0:
    if x % 8 == 0:
        count += 1
    x //= 8
print(count)

# II способ
print(oct(7 * 512 ** 120 - 6 * 64 * 100 + 8 ** 210 - 255)[2:].count('0'))