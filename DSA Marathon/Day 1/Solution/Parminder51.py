from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())+1
    nums = tuple(map(int, stdin.readline().split()))
    numbers = {}
    for i in range(n):
        if numbers.get(nums[i], False)==False:
            numbers[nums[i]] = True
        else:
            p = nums[i]
            break
    stdout.write(str(p)+'\n')