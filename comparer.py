
class ComparedValuesCollection:
    def __init__(self, one_list, two_list, zero_list):
        self.one_list = one_list
        self.two_list = two_list
        self.zero_list = zero_list


class Comparer:
    def __init__(self, left_value, right_value):
        self.left_value = left_value
        self.right_value = right_value

    def compare(self):
        one_list = []
        two_list = []
        zero_list = []

        for left_list_value in self.left_value:
            if left_list_value not in self.right_value:
                one_list.append(left_list_value)
            else:
                zero_list.append(left_list_value)

        for right_list_value in self.right_value:
            if right_list_value not in self.left_value:
                two_list.append(right_list_value)

        result = ComparedValuesCollection(one_list, two_list, zero_list)

        print("\n\nComparing results:")
        print(" * The count of lines which are not in the second list: {0}, {1:4.2f}%".format(
              len(result.one_list), len(result.one_list) / len(self.left_value) * 100.0))
        print(" * The count of lines which are not in the first list: {0}, {1:4.2f}%".format(
              len(result.two_list), len(result.two_list) / len(self.right_value) * 100.0))
        print(" * The count of lines which are the same: {0}, {1:4.2f}%".format(
              len(result.zero_list), len(result.zero_list) / len(self.left_value) * 100.0))

        return result