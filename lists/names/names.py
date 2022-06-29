import random

from .first_names_male import first_names_male
from .first_names_female import first_names_female
from .last_names import last_names

def get_weights(num, popularity:int=1):
    return [(num-i)**popularity for i in range(0, num)]

def get_name(gender=None, popularity=1):
    if gender is None:
        gender = random.choice(['male', 'female'])

    if gender == 'male':
        weights = get_weights(len(first_names_male), popularity)
        first = random.choices(first_names_male, weights)[0]
    if gender == 'female':
        weights = get_weights(len(first_names_female), popularity)
        first = random.choices(first_names_female, weights)[0]
    
    weights = get_weights(len(last_names), popularity)
    last = random.choices(last_names, weights)[0]

    return first.capitalize(), last.capitalize()

# print(get_name(popularity=100))
# print(get_name(popularity=100))
# print(get_name(popularity=100))
# print(get_name(popularity=100))
# print(get_name(popularity=100))
# print(get_name(popularity=100))