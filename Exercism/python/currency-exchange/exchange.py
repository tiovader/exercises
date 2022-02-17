def exchange_money(budget: float, exchange_rate: float) -> float:
    '''

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - estimated value of the foreign currency you can receive
                     based on your budget and the current exchange rate.

    '''

    return round(budget / exchange_rate, 2)


def get_change(budget: float, exchanging_value: float) -> float:
    '''

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want
                                   to exchange now.
    :return: float - the amount left of your starting currency
                                   after exchanging.

    '''

    return round(budget - exchanging_value, 2)


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    '''

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - the total value of bills you now have.

    '''

    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    '''

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - the number of bills after exchanging all your money.
    '''

    return budget // denomination


def new_exchange_rate(exchange_rate: float, spread: int) -> float:
    '''

    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :return: float - the updated value of exchange_rate based on
                     the spread rate.
    '''
    return exchange_rate * (1 + spread / 100)


def exchangeable_value(budget: float, exchange_rate: float,
                       spread: int, denomination: int) -> int:
    '''

    :param budget: float - the amount of your money you are planning
                           to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - the maximum value you can get considering the budget,
                   exchange_rate, spread, & denomination.

    '''
    total_value = estimate_value(
        budget, new_exchange_rate(exchange_rate, spread))
    number_of_bills = get_number_of_bills(total_value, denomination)

    return get_value(denomination, number_of_bills)


def non_exchangeable_value(budget: float, exchange_rate: float,
                         spread: int, denomination: int) -> int:
    '''
    :param budget: float - the amount of your money you are planning
                           to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - the unexchangeable value considering the budget,
                   exchange_rate, spread, & denomination.

    '''
    total_value = estimate_value(
        budget, new_exchange_rate(exchange_rate, spread))
    exchangeable_value_ = exchangeable_value(
        budget, exchange_rate, spread, denomination)

    return int(total_value - exchangeable_value_)
