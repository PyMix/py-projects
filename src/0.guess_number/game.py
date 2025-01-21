import numpy as np


def random_predict_num(number: int = 1) -> int:
    """guess number

    Args:
        number (int, optional): guessed number. Defaults to 1.

    Returns:
        int: number of tries
    """

    count = 0
    while (True):
        count += 1
        predict_number = np.random.randint(1, 100)
        if predict_number == number:
            break
    return count


def score_game(random_predict) -> int:
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=1000)
    count_ls = []
    for n in random_array:
        count_ls.append(random_predict(n))
    score = int(np.mean(count_ls))

    return score


if __name__ == '__main__':
    score_game(random_predict_num)
