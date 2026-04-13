from typing import Literal
def get_follower_prediction(follower_count: int, influencer_type: Literal['fitness', 'cosmetics', 'others'], num_months: int) -> int:
    if influencer_type == 'fitness':
        factor = 4
    elif influencer_type == 'cosmetics':
        factor = 3
    else:
        factor = 2

    predicted_followers = follower_count * (factor ** num_months)
    return int(predicted_followers)

if __name__ == "__main__":
    print(get_follower_prediction(1000, 'fitness', 3))
    print(get_follower_prediction(500, 'cosmetics', 4))
    print(get_follower_prediction(200, 'others', 5))