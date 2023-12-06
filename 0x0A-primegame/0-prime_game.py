#!/usr/bin/python3

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    player = 0
    count = [0, 0]
    for _ in range(x):
        if not nums: # check if the nums list is empty
            break
        num = nums.pop(0)
        primes = [i for i in range(2, num + 1) if isPrime(i)]
        if player == 0:
            for prime in primes:
                while prime in nums:
                    nums.remove(prime)
                    for multiple in range(prime + prime, num + 1, prime):
                        if multiple in nums:
                            nums.remove(multiple)
            count[player] += len(nums) > 0
        else:
            nums = [i for i in nums if isPrime(i)]
            count[player] += len(nums) > 0
        player = 1 - player
    return "Maria" if count[0] > count[1] else "Ben" if count[0] < count[1] else None
