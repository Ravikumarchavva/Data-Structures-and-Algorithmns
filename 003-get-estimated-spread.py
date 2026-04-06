from math import ceil
def get_estimated_spread(audiences_followers: list[int]) -> int:
    estimated_followers = 0
    if len(audiences_followers) == 0:
        return estimated_followers
    avg_followers = sum(audiences_followers) / len(audiences_followers)
    estimated_followers = avg_followers * (len(audiences_followers) ** 1.2)
    return ceil(estimated_followers)

if __name__ == "__main__":
    print(get_estimated_spread([]))
    print(get_estimated_spread([2, 3, 2, 19]))
    print(get_estimated_spread([12, 12, 12]))