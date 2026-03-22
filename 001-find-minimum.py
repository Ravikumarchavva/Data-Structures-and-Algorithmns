def get_minimum(arr: list) -> int:
    if len(arr) == 0:
        return None
    max = float("inf")
    for i in arr:
        if i < max:
            max = i

    return max

if __name__ == '__main__':
    print(get_minimum([1,2,3]))
    print(get_minimum([]))