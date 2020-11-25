from math import sqrt
import json
import requests


# Exercise 1
def square(side):
    return [4 * side, side ** 2, round(sqrt(2 * side ** 2), 2)]


# Exercise 2
def season(month):
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    elif month in [9, 10, 11]:
        return 'fall'
    else:
        return 'Month must be in between 1 and 12'


# Exercise 3
def sign_stats(values):
    positive_numbers = 0
    negative_numbers = 0
    zeros = 0
    for i in values:
        if i > 0:
            positive_numbers += 1
        elif i < 0:
            negative_numbers += 1
        else:
            zeros += 1
    return [positive_numbers / len(values) * 100, negative_numbers / len(values) * 100, zeros / len(values) * 100]


# Exercise 4
def seasons_appeared(name):
    response = requests.get('https://www.breakingbadapi.com/api/characters?category=Breaking+Bad')
    characters = json.loads(response.text)
    character_name = ''
    seasons = 0
    return_strings = []
    for character in characters:
        if name.lower() in character['name'].lower():
            character_name = character['name']
            seasons = len(character['appearance'])
            return_strings.append(f'{character_name} appeared in {seasons} seasons')
    return '\n'.join(return_strings) if return_strings else f"Can't find characters with name containing '{name}'"


def main():
    square_input = int(input('Enter side length of a square: '))
    print(square(square_input))

    month = int(input('Enter the month number: '))
    print(season(month))

    values = []
    amount_of_inputs = int(input('Enter the amount of inputs: '))
    for i in range(amount_of_inputs):
        value = int(input(f'Enter the {i + 1}. value: '))
        values.append(value)
    print(sign_stats(values))

    name = input('Who are you looking for? ')
    print(seasons_appeared(name))


if __name__ == '__main__':
    main()