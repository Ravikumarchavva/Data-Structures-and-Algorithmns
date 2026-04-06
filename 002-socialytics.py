def sum(nums: int) -> int:
    total = 0
    for num in nums:
        total += num

    return total

if __name__ == "__main__":
    print(sum([]))
    print(sum([1, 2]))