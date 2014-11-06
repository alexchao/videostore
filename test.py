import unittest

from videostore import Movie
from videostore import Rental
from videostore import Customer


class TestEmptyCustomerStatement(unittest.TestCase):

    def test_statement_with_no_rentals(self):
        self.assertEqual(
            Customer('Darwin').statement(),
            """Rental Record for Darwin
Amount owed is 0
You earned 0 frequent renter points""")


class TestCustomerStatement(unittest.TestCase):

    def setUp(self):
        self.movie_1 = Movie('John Wick', Movie.CODE_NEW_RELEASE)
        self.movie_2 = Movie('Frozen', Movie.CODE_CHILDRENS)
        self.movie_3 = Movie('The Rock', Movie.CODE_REGULAR)

    def test_statement_with_one_day_rentals(self):
        customer = Customer('Mike')
        customer.add_rental(Rental(self.movie_1, 1))
        customer.add_rental(Rental(self.movie_2, 1))
        customer.add_rental(Rental(self.movie_3, 1))
        self.assertEqual(
            customer.statement(),
            """Rental Record for Mike
\tJohn Wick\t3
\tFrozen\t1.5
\tThe Rock\t2
Amount owed is 6.5
You earned 3 frequent renter points""")

    def test_statement_with_rentals(self):
        customer = Customer('Jeremy')
        customer.add_rental(Rental(self.movie_1, 3))
        customer.add_rental(Rental(self.movie_2, 7))
        customer.add_rental(Rental(self.movie_3, 6))
        self.assertEqual(
            customer.statement(),
            """Rental Record for Jeremy
\tJohn Wick\t9
\tFrozen\t7.5
\tThe Rock\t8.0
Amount owed is 24.5
You earned 4 frequent renter points""")


if __name__ == '__main__':
    unittest.main()
