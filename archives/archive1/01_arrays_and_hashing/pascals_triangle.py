from typing import List

def generate_row(prev_row: List) -> List[int]:
    line = [1]

    for i in range(1, len(prev_row)):
        line.append(prev_row[i-1] + prev_row[i])
    line.append(1)

    return line

def generate(numRows: int) -> List[List[int]]:
    lists = [[1]]
    for i in range(1, numRows):
        lists.append(generate_row(lists[i-1]))

    return lists

if __name__ == "__main__":
    print(generate(5))