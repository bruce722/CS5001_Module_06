"""
    CS5001-5003 Fall 2022
    Lab 06 -- Coding Practice 6-- Problem 1, print multiples of 5
    (Bruce) Chuanzhao Huang / 
"""


def main():
    num = int(input("Enter a positive integer: "))
    times = num // 5
    if num > 0:
        for time in range(1, times + 1):
            result = 5 * time
            print(result)
    return result


if __name__ == "__main__":
    main()
