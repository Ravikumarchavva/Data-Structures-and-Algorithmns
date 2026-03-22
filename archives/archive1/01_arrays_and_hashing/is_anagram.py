def is_anagram(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    for char in t:
        if (char not in char_count) or (char_count[char] == 0):
            return False
        char_count[char] -= 1

    return True

if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False