import rigla
import codecs
import comparer
import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: main.py <first_file> <second_file> <output_file> [-e]")
        print("       Use a -e parameter to print errors during parsing.")
        sys.exit(1)

    print_errors = len(sys.argv) > 4 and sys.argv[4] == '-e'

    rigla_parsed_list = parse_file(sys.argv[1], rigla.Parser(), print_errors)
    other_parsed_list = parse_file(sys.argv[2], rigla.Parser(), print_errors)

    list_of_compared_results = comparer.Comparer(rigla_parsed_list, other_parsed_list).compare()

    write_file(sys.argv[3], list_of_compared_results.one_list,
               list_of_compared_results.two_list, list_of_compared_results.zero_list)


def write_file(filename, one_list, two_list, zero_list):
    with codecs.open(filename, mode="w", encoding="cp1251") as f:
        f.write("\n\nThe values that are not in the second file but are in the first file.\n")
        for line in one_list:
            f.write(';'.join(line.other_values) + '\n')

        f.write("\n\nThe values that are not in the first file but are in the second file.\n")
        for line in two_list:
            f.write(';'.join(line.other_values) + '\n')

        f.write("\n\nThe values that are the same in the first and the second files.\n")
        for line in zero_list:
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

if __name__ == '__main__':
    main()