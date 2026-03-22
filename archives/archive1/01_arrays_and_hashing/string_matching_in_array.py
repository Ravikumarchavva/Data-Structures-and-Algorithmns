
from typing import List


def string_matching_in_array(words: List[str]) -> List[str]:
    res = []
    n = len(words)
    for i in range(n):
        for j in range(n):
            if i != j and words[i] in words[j]:
                res.append(words[i])
                break
    return res