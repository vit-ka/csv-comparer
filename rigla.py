import common
import datetime


class Parser:

    def parse(self, csv_string):
        splitted_string = [x.strip() for x in csv_string.split(';')]

        if len(splitted_string) < 8:
            return common.ParsedValueToCompare(datetime.date(datetime.MINYEAR, 1, 1), 0, 0, splitted_string)

        try:
            parsed_date = datetime.datetime.strptime(splitted_string[2], '%d.%m.%y')

            return common.ParsedValueToCompare(parsed_date, int(splitted_string[5]), int(splitted_string[7]), splitted_string)
        except ValueError as e:
            value_to_return = common.ParsedValueToCompare(datetime.date(datetime.MINYEAR, 1, 1), 0, 0, splitted_string)
            value_to_return.error_message = e
            return value_to_return
