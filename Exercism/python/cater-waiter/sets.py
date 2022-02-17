
from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name: str, dish_ingredients: list[str]) -> tuple[str, set[str]]:
    '''

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item, followed by
    the de-duped `set` of ingredients as the second item.
    '''

    return dish_name, set(dish_ingredients)


def check_drinks(dish_name: str, dish_ingredients: list[str]) -> str:
    '''

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has no
    alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    '''
    drink_type = 'Mocktail' if not ALCOHOLS.intersection(dish_ingredients) \
        else 'Cocktail'
    return f'{dish_name} {drink_type}'


def categorize_dish(dish_name: str, dish_ingredients: list[str]) -> str:
    '''

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the
    dish belongs to). All dishes will "fit" into one of the categories imported from `categories.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    '''
    keys = 'VEGAN', 'VEGETARIAN', 'PALEO', 'KETO', 'OMNIVORE'
    values = VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE

    for key, value in zip(keys, values):
        if set(dish_ingredients).issubset(value):
            return f'{dish_name}: {key}'
    return f'{dish_name}: NO CATEGORY'


def tag_special_ingredients(dish: tuple[str, list[str]]) -> tuple[str, set[str]]:
    '''

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the
    dish description. For the purposes of this exercise, all allergens or special ingredients that
    need to be tracked are in the SPECIAL_INGREDIENTS constant imported from `categories.py`.
    '''

    return dish[0], SPECIAL_INGREDIENTS.intersection(dish[1])


def compile_ingredients(dishes: list[set[str]]) -> set[str]:
    '''

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    '''

    return set.union(*dishes)


def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    '''

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    '''
    return list(set(dishes).difference(appetizers))


def singleton_ingredients(dishes: list[set[str]], intersection: set[str]) -> set[str]:
    '''

    :param intersection: constant - one of (VEGAN_INTERSECTION, VEGETARIAN_INTERSECTION,
                                            PALEO_INTERSECTION, KETO_INTERSECTION,
                                            OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    '''

    return set.union(*dishes).difference(intersection)
