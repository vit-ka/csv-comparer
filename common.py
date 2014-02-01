import math
import codecs


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
        return self.arrival_date == other.arrival_date \
            and math.fabs(self.price - other.price) < 2 \
            and self.item_number == other.item_number


def write_file(filename, not_in_first_list, not_in_second_list, in_both_lists):
    with codecs.open(filename, mode="w", encoding="cp1251") as f:
        f.write("\n\nThe values that are not in the second file but are in the first file.\n")
        for line in not_in_first_list:
            f.write(';'.join(line.other_values) + '\n')

        f.write("\n\nThe values that are not in the first file but are in the second file.\n")
        for line in not_in_second_list:
            f.write(';'.join(line.other_values) + '\n')

        f.write("\n\nThe values that are the same in the first and the second files.\n")
        for line in in_both_lists:
            f.write(';'.join(line.other_values) + '\n')


def parse_file(filename, parser, print_errors):
    with codecs.open(filename, encoding='cp1251') as f:
        content = f.readlines()

    list_to_return = []
    failed_to_parse = []

    parsed_counter = 0

    for line in content:
        parsed_value = parser.parse(line)

        parsed_counter += 1
        if parsed_value.arrival_date.year != 1:
            list_to_return.append(parsed_value)
        else:
            failed_to_parse.append(parsed_value)

    print('\n\nFile "{0}" has been processed. Total lines: {1}. Parsed lines: {2}. Parsing success rate: {3:4.2f}%'.
          format(filename, parsed_counter, len(list_to_return), len(list_to_return)/parsed_counter * 100.0))

    if print_errors:
        print('The following {0} lines could not be parsed:'.format(len(failed_to_parse)))
        for i in failed_to_parse:
            print('         * Message: "' + str(i.error_message) + '". Line: ' + ';'.join(i.other_values))

    return list_to_return