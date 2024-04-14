import numpy as np


COEFS = np.array([
    [3,  4,  6],
    [4,  5,  7],
    [3,  4,  6],
    [7, 10, 15],
    [5,  7, 10],
    ])

LANGUAGES = np.array([320, 128, 106, 106,
                      90, 64, 53, 53,
                      49, 32, 34, 18,
                      21, 54, 13, 56 ])

def calculate_fp(func_types_matrix: list[list[int]]) -> tuple[list[int], int]:
    func_types_matrix = np.array(func_types_matrix)

    product = COEFS * func_types_matrix
    sums = np.sum(product, 1)

    return sums.tolist(), np.sum(sums)


def adjust_fp(fp: int, complexity_ratios: list[int]) -> float:
    vaf = 0.65 + 0.01 * sum(complexity_ratios)

    return fp * vaf

def get_loc_by_fp(fp: float, language_percentage: list[float]) -> float:
    language_percentage = np.array(language_percentage) / 100
    fps_by_language = fp * language_percentage

    return int(round(np.sum(fps_by_language * LANGUAGES)))


if __name__ == "__main__":
    example = [
            [2, 0, 0],
            [1, 0, 0],
            [2, 0, 0],
            [1, 0, 0],
            [0, 0, 0]
            ]
    complexity = [0, 0, 0, 0, 0, 5, 1, 2, 0, 0, 0, 0, 2, 5]
    languages = [0, 0, 0, 0,
                 0, 0, 100, 0,
                 0, 0, 0, 0,
                 0, 0, 0, 0]

    fp = calculate_fp(example)
    afp = adjust_fp(fp[-1], complexity)
    loc = get_loc_by_fp(afp, languages)
    print(f"{fp}\n{afp}\n{loc}")

    example = [
            [5, 0, 0],
            [2, 0, 0],
            [1, 0, 0],
            [4, 0, 0],
            [1, 0, 0]
            ]
    complexity = [5, 5, 3, 2, 3, 4, 1, 4, 4, 0, 1, 2, 2, 2]
    languages = [0, 0, 0, 0,
                 0, 0, 60, 25,
                 0, 0, 0, 0,
                 0, 0, 15, 0]

    fp = calculate_fp(example)
    afp = adjust_fp(fp[-1], complexity)
    loc = get_loc_by_fp(afp, languages)
    print(f"{fp}\n{afp}\n{loc}")
