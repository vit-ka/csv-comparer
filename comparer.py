
class ComparedValue:
    def __init__(self, status, value):
        self.status = status
        self.value = value

    def __str__(self):
        return '[' + str(self.status) + ': ' + str(self.value) + ']'


class ComparedValuesCollection:
    def __init__(self, list_of_values):
        self.one_list = []
        self.two_list = []
        for i in list_of_values:
            if i.status == 1:
                self.one_list.append(i)
            elif i.status == 2:
                self.two_list.append(i)


class Comparer:
    def __init__(self, left_value, right_value):
        self.left_value = left_value
        self.right_value = right_value

    def compare(self):
        list_to_return = []

        for left_list_value in self.left_value:
            if left_list_value not in self.right_value:
                list_to_return.append(ComparedValue(1, left_list_value))

        for right_list_value in self.right_value:
            if right_list_value not in self.left_value:
                list_to_return.append(ComparedValue(2, right_list_value))

        return ComparedValuesCollection(list_to_return)