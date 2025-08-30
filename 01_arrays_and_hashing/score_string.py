def score_string(s: str) -> int:
    score = 0
    for char_index in range(len(s) - 1):
        score += abs(ord(s[char_index+1]) - ord(s[char_index]))
    return score

if __name__ == "__main__":
    print(score_string("abc"))  # 2
    print(score_string("xyz"))  # 2
