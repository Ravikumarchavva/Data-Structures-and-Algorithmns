from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    # Find the minimum length string in the list
    min_str = min(strs, key=len)

    # Check each character of the minimum string
    for i in range(len(min_str)):
        for s in strs:
            if s[i] != min_str[i]:
                return min_str[:i]

    return min_str

if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix(["dog", "racecar", "car"]))