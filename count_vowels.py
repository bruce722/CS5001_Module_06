"""
    CS5001-5003 Fall 2022
    Lab 06 -- Coding Practice 6-- Problem 3, count vowels
    (Bruce) Chuanzhao Huang / 
"""


def count_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in words.lower():
        if letter in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(count_vowels("aweqwkehq"))
