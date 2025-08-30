from typing import List
def replace_elements(arr: List[int]) -> List[int]:
        len_arr = len(arr)
        for i in range(len_arr):
            if i == len_arr-1:
                arr[i] = -1
                break
            arr[i] = max(arr[i+1:])
        return arr

if __name__ == "__main__":
    print(replace_elements([17, 18, 5, 4, 6, 1]))  # [18, 6, 6, 6, 1, -1]
    print(replace_elements([400]))                  # [-1]
