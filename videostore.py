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
        self.set_price_code(price_code)

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, price_code):
        self._price_code = price_code

    def get_title(self):
        return self._title

    def get_charge(self, days_rented):
        result = 0
        price_code = self.get_price_code()
        if price_code == Movie.CODE_REGULAR:
            result += 2
            if days_rented > 2:
                result += (days_rented - 2) * 1.5
        elif price_code == Movie.CODE_NEW_RELEASE:
            result += days_rented * 3
        elif price_code == Movie.CODE_CHILDRENS:
            result += 1.5
            if days_rented > 3:
                result += (days_rented - 3) * 1.5
        return result

    def get_frequent_renter_points(self, days_rented):
        if ((self.get_price_code() == Movie.CODE_NEW_RELEASE)
            and days_rented > 1):
            # add bonus for a two-day new release rental
            return 2
        return 1


class Price(object):

    def get_price_code(self):
        raise NotImplementedError()


class ChildrensPrice(Price):

    def get_price_code(self):
        return Movie.CODE_CHILDRENS


class NewReleasePrice(Price):

    def get_price_code(self):
        return Movie.CODE_NEW_RELEASE


class RegularPrice(Price):

    def get_price_code(self):
        return Movie.CODE_REGULAR


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

    def get_charge(self):
        return self._movie.get_charge(self._days_rented)

    def get_frequent_renter_points(self):
        return self._movie.get_frequent_renter_points(self._days_rented)


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
        result = 'Rental Record for ' + self.get_name() + '\n';
        for rental in self._rentals:

            # show figures for this rental
            result += ('\t' + rental.get_movie().get_title() + '\t' +
                str(rental.get_charge()) + '\n')

        # add footer lines
        result += 'Amount owed is ' + str(self.get_total_charge()) + '\n'
        result += ('You earned ' + str(self.get_total_frequent_renter_points())
                   + ' frequent renter points')
        return result

    def get_total_charge(self):
        return sum(r.get_charge() for r in self._rentals)

    def get_total_frequent_renter_points(self):
        return sum(r.get_frequent_renter_points() for r in self._rentals)
