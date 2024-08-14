import re
from itertools import permutations


def findall(text: str, pattern: str) -> int:
    left = 0
    count = 0
    while True:
        match = re.search(pattern, text[left:])
        if not match:
            break
        count += 1
        left += match.start() + 1
    return count


def starts_with_vowel(word: str) -> bool:
    return True if word[0] in vowels() else False


def vowels() -> set:
    return {"A", "E", "I", "O", "U"}


def get_permutations(word):
    substrings = set()
    for i in range(1, len(word) + 1):
        substrings = substrings.union(set(["".join(p) for p in permutations(word, i)]))

    return substrings


def stuart(word):
    """
    consonants
    """

    score = 0
    substrings = get_permutations(word)
    for substring in substrings:
        if not starts_with_vowel(substring):
            counts = findall(word, substring)
            score += counts
            # if counts > 0:
                # print(f"Stuart {substring} {counts}")

    return score


def kevin(word):
    """
    vowels
    """
    score = 0
    substrings = get_permutations(word)
    for substring in substrings:
        if starts_with_vowel(substring):
            counts = findall(word, substring)
            score += counts
            # if counts > 0:
                # print(f"Kevin {substring} {counts}")

    return score


def minion_game(string):
    kevin_score = kevin(string)
    # print(20 * "-")
    stuart_score = stuart(string)

    if kevin_score == stuart_score:
        print("Draw")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print(f"Stuart {stuart_score}")


if __name__ == '__main__':
    s = input()
    minion_game(s)