from typing import List
def concatenate_same_array(arr: List[int]) -> List[int]:
    return arr + arr

if __name__ == "__main__":
    print(concatenate_same_array([1, 2, 3]))  # [1, 2, 3, 1, 2, 3]
    print(concatenate_same_array([4, 5]))     # [4, 5, 4, 5]
