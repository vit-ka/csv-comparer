import math


class ParsedValueToCompare:
    def __init__(self, arrival_date, item_number, price, other_values):
        self.arrival_date = arrival_date
        self.item_number = item_number
        self.price = price
        self.other_values = other_values

    def __str__(self):
        return '[' + self.arrival_date.strftime('%Y-%m-%d') + ', ' \
               + str(self.item_number) + ', ' + str(self.price) \
               + ': ' + str(self.other_values) + ']'

    def __eq__(self, other):
        return self.arrival_date == other.arrival_date and math.fabs(self.price - other.price) < 1