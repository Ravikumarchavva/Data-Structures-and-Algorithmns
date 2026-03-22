
from typing import List


def count_senior_citizens(details: List[str]) -> int:
    senior_citizens = 0
    for person in details:
        tens = int(person[11])
        ones = int(person[12])
        age = tens*10 + ones
        if age > 60:
            senior_citizens += 1

    return senior_citizens

if __name__ == "__main__":
    print(count_senior_citizens(["7868190130M7522","5303914400F9211","9273338290F4010"]))
    print(count_senior_citizens(["1313579440F2036","2921522980M5644"]))