import datetime


class ParsedValueToCompare:
    def __init__(self, arrival_date, item_number, one_more_number):
        self.arrival_date = arrival_date
        self.item_number = item_number
        self.one_more_number = one_more_number

    def __str__(self):
        return '[' + self.arrival_date.strftime('%Y-%m-%d') + ', ' \
               + str(self.item_number) + ', ' + str(self.one_more_number) + ']'