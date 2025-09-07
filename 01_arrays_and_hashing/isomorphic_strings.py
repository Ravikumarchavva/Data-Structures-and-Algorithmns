from typing import Dict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        set_map_st: Dict[str, str] = {}
        set_map_ts: Dict[str, str] = {}

        for c1, c2 in zip(s, t):
            if c1 in set_map_st and set_map_st[c1] != c2:
                return False
            if c2 in set_map_ts and set_map_ts[c2] != c1:
                return False
            set_map_st[c1] = c2
            set_map_ts[c2] = c1
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("egg", "add"))
    print(s.isIsomorphic("foo", "bar"))
    print(s.isIsomorphic("paper", "title"))
    print(s.isIsomorphic("ab", "aa"))