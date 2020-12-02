from typing import List

import pandas as pd

df = pd.read_csv("input.csv", sep=" ")


def count_char_occurence(password: str, char: str) -> int:
    return password.count(char)


def check_char_position(password: str, char: str, occurence: List[int]) -> bool:
    char_1_check = False
    char_2_check = False
    if password[occurence[0] - 1] == char:
        char_1_check = True
    if password[occurence[1] - 1] == char:
        char_2_check = True

    # XOR -> return true if either check1 or check2 is true
    return char_1_check != char_2_check

correct_passwords = 0
correct_password_2 = 0
for ind in df.index:
    char = df['char'][ind][0]
    min_max = df['number_range'][ind].split("-")
    min_max = [int(x) for x in min_max]
    password = df['password'][ind]

    print(char, min_max, password)
    char_occurences = count_char_occurence(password, char)
    if min_max[0] <= char_occurences <= min_max[1]:
        print("yes")
        correct_passwords += 1
    else:
        print("no")

    if check_char_position(password, char, min_max):
        correct_password_2 += 1

print(f"quiz 2.0 = {correct_passwords}")
print(f"quiz 2.1 = {correct_password_2}")


