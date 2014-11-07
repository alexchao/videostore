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
        return self._price.get_price_code()

    def set_price_code(self, price_code):
        if price_code == Movie.CODE_REGULAR:
            self._price = RegularPrice()
        elif price_code == Movie.CODE_CHILDRENS:
            self._price = ChildrensPrice()
        elif price_code == Movie.CODE_NEW_RELEASE:
            self._price = NewReleasePrice()
        else:
            raise NotImplementedError('Incorrect Price Code')

    def get_title(self):
        return self._title

    def get_charge(self, days_rented):
        return self._price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented):
        return self._price.get_frequent_renter_points(days_rented)


class Price(object):

    def get_price_code(self):
        raise NotImplementedError()

    def get_charge(self, days_rented):
        raise NotImplementedError()

    def get_frequent_renter_points(self, days_rented):
        return 1


class ChildrensPrice(Price):

    def get_price_code(self):
        return Movie.CODE_CHILDRENS

    def get_charge(self, days_rented):
        result = 1.5
        if days_rented > 3:
            result += (days_rented - 3) * 1.5
        return result


class NewReleasePrice(Price):

    def get_price_code(self):
        return Movie.CODE_NEW_RELEASE

    def get_charge(self, days_rented):
        return days_rented * 3

    def get_frequent_renter_points(self, days_rented):
        return 2 if days_rented > 1 else 1


class RegularPrice(Price):

    def get_price_code(self):
        return Movie.CODE_REGULAR

    def get_charge(self, days_rented):
        result = 2
        if days_rented > 2:
            result += (days_rented - 2) * 1.5
        return result


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
