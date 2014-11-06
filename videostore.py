# -*- coding: utf-8 -*-


class Movie(object):
    """
    title -- string
    price_code -- integer
    """

    CODE_CHILDRENS = 2
    CODE_REGULAR = 0
    CODE_NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, price_code):
        self._price_code = price_code

    def get_title(self):
        return self._title


class Rental(object):
    """
    movie -- Movie instance
    days_rented -- number of days rented
    """

    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_movie(self):
        return self._movie


class Customer(object):

    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental):
        """
        rental -- Rental instance
        """
        self._rentals.append(rental)

    def get_name(self):
        return self._name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = 'Rental Record for ' + self.get_name() + '\n';
        for rental in self._rentals:
            this_amount = 0

            this_amount = self._amount_for(rental)

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two-day new release rental
            if ((rental.get_movie().get_price_code() == Movie.CODE_NEW_RELEASE)
                and rental.get_days_rented() > 1):
                frequent_renter_points += 1

            # show figures for this rental
            result += ('\t' + rental.get_movie().get_title() + '\t' +
                str(this_amount) + '\n')
            total_amount += this_amount

        # add footer lines
        result += 'Amount owed is ' + str(total_amount) + '\n'
        result += ('You earned ' + str(frequent_renter_points)
                   + ' frequent renter points')
        return result

    def _amount_for(self, rental):
        result = 0
        price_code = rental.get_movie().get_price_code()
        if price_code == Movie.CODE_REGULAR:
            result += 2
            if rental.get_days_rented() > 2:
                result += (rental.get_days_rented() - 2) * 1.5
        elif price_code == Movie.CODE_NEW_RELEASE:
            result += rental.get_days_rented() * 3
        elif price_code == Movie.CODE_CHILDRENS:
            result += 1.5
            if rental.get_days_rented() > 3:
                result += (rental.get_days_rented() - 3) * 1.5
        return result
