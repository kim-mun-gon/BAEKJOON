import sys

n = int(input())
nums = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

count = 0
left, right = 0, n-1

while left < right:
    temp = nums[left] + nums[right]

    if temp == x:
        count += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1

print(count)