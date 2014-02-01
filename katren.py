import common
import datetime


class Parser:
    def __init__(self):
        self.type = 'Katren'

    def parse(self, csv_string):
        splitted_string = [x.strip() for x in csv_string.split(';')]

        if len(splitted_string) < 3:
            return common.ParsedValueToCompare(datetime.date(datetime.MINYEAR, 1, 1), 0, 0, splitted_string)

        try:
            parsed_date = datetime.datetime.strptime(splitted_string[0], '%d/%m/%y')
            parsed_price = float(splitted_string[2].replace(',', '.').replace('К', ''))
            parsed_number = int(splitted_string[1])

            parsed_value = common.ParsedValueToCompare(parsed_date, parsed_number, parsed_price, splitted_string)
            return parsed_value
        except ValueError as e:
            value_to_return = common.ParsedValueToCompare(datetime.date(datetime.MINYEAR, 1, 1), 0, 0, splitted_string)
            value_to_return.error_message = e
            return value_to_return
