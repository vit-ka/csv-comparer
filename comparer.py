
class ComparedListCollection:
    def __init__(self, not_in_first_list, not_in_second_list, in_both_lists):
        self.not_in_first_list = not_in_first_list
        self.not_in_second_list = not_in_second_list
        self.in_both_lists = in_both_lists


class Comparer:
    def __init__(self, first_list, second_list):
        self.first_list = first_list
        self.second_list = second_list

    def compare(self):
        not_in_first_list = []
        not_in_second_list = []
        in_both_lists = []

        for first_list_value in self.first_list:
            if first_list_value not in self.second_list:
                not_in_first_list.append(first_list_value)
            else:
                in_both_lists.append(first_list_value)

        for second_list_value in self.second_list:
            if second_list_value not in self.first_list:
                not_in_second_list.append(second_list_value)

        result = ComparedListCollection(not_in_first_list, not_in_second_list, in_both_lists)

        print("\n\nComparing results:")
        print(" * The count of lines which are not in the second file: {0}, {1:4.2f}%".format(
              len(result.not_in_first_list), len(result.not_in_first_list) / len(self.first_list) * 100.0))
        print(" * The count of lines which are not in the first file: {0}, {1:4.2f}%".format(
              len(result.not_in_second_list), len(result.not_in_second_list) / len(self.first_list) * 100.0))
        print(" * The count of lines which are the same: {0}, {1:4.2f}%".format(
              len(result.in_both_lists), len(result.in_both_lists) / len(self.first_list) * 100.0))

        return result