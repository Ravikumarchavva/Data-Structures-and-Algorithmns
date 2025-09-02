def isSubsequence(s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        l1 = len(s)
        l2 = len(t)
        while p1 < l1 and p2 < l2:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        if p1 == l1:
            return True
        return False

if __name__ == "__main__":
    print(isSubsequence("abc", "ahbgdc"))
    print(isSubsequence("axc", "ahbgdc"))