class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data  # returns the list

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3)

    # test the happy path that we have an integer and want to add it to the list
    def test_init_list_all_ints(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual(3, len(integer.get_data()))  # tests the len of the return of get_data
        self.assertEqual(3, len(integer._IntegerList__data))  # tests the actual private attribute

    # tests the unhappy path if there is a non-integer type added to the list
    def test_init_list_non_integers_added(self):
        integer = IntegerList(4, 5, 6, 7.5)
        self.assertEqual(3, len(integer.get_data()))
        self.assertEqual([4, 5, 6], integer.get_data())

    # separately tests the result of get_data
    def test_get_data_returns_list_with_elements(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    # test the happy path that we add an integer to the list
    def test_add_method_adds_int(self):
        self.assertEqual(3, len(self.int_list.get_data()))

        result = self.int_list.add(5)

        self.assertEqual(4, len(self.int_list.get_data()))  # checks the len
        self.assertIn(5, self.int_list.get_data())  # check if the 5 is in the list
        self.assertEqual([1, 2, 3, 5], result)  # checks the actual data in the list

    # test the unhappy path that a non-integer is added to the list
    def test_add_method_not_int_raises(self):
        # this is the state before the method
        self.assertEqual(3, len(self.int_list.get_data()))

        invalid_data = [4.3, "test", {}, [], False]
        for each_value in invalid_data:
            # capture the error in the with self assert
            with self.assertRaises(ValueError) as ex:
                # actually call the method
                self.int_list.add(each_value)

        # check the error message
        self.assertEqual("Element is not Integer", str(ex.exception))

    # test the happy path that an element with valid idx is being removed
    def test_remove_idx_removes_element(self):
        # check the length in the initial state
        self.assertEqual(3, len(self.int_list.get_data()))
        # check the element at the first idx before calling the remove method
        self.assertEqual(1, self.int_list.get_data()[0])

        # removes the element with idx 0
        result = self.int_list.remove_index(0)

        # checks the returned result
        self.assertEqual(1, result)
        # checks if after the removal the length has changed
        self.assertEqual(2, len(self.int_list.get_data()))
        # checks if the first element is now 2 and not 1
        self.assertEqual(2, self.int_list.get_data()[0])

    # test the unhappy path that the idx is invalid
    def test_remove_method_invalid_idx_raises(self):
        # state before calling the remove method
        self.assertEqual(3, len(self.int_list.get_data()))

        # save the error and call the remove method
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ex.exception))

        # check if the list remains unchanged
        self.assertEqual(3, len(self.int_list.get_data()))

        # test the happy path of the get method
    def test_get_by_idx(self):
        self.assertEqual(3, len(self.int_list.get_data()))

        curr_element = self.int_list.get(1)
        self.assertEqual(1, curr_element)

    # test unhappy path of the get method
    def test_get_invalid_idx_raises(self):
        self.assertEqual(3, len(self.int_list.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.int_list.get(5)

        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(3, len(self.int_list.get_data()))

    # check the happy path of method insert with valid idx
    def test_insert_at_idx_an_element(self):
        # check the state before inserting an element
        self.assertEqual(3, len(self.int_list.get_data()))
        self.assertEqual([1, 2, 3], self.int_list.get_data())
        self.assertEqual([1, 2, 3], self.int_list._IntegerList__data)

        # insert an element
        self.int_list.insert(0, 4)

        # check if after insertion the len has changed,the 4 is in the list and the two lists are equal
        self.assertEqual(4, len(self.int_list.get_data()))
        self.assertEqual([4, 1, 2, 3], self.int_list.get_data())
        self.assertEqual([4, 1, 2, 3], self.int_list._IntegerList__data)

    # check the unhappy path of inserting an element with invalid idx
    def test_insert_element_at_invalid_idx(self):
        self.assertEqual(3, len(self.int_list.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(5, 1)

        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(3, len(self.int_list.get_data()))

    # check the unhappy path of inserting an invalid element with a valid idx
    def test_insert_invalid_element_at_valid_idx(self):
        self.assertEqual(3, len(self.int_list.get_data()))

        invalid_data_types = [4.3, {}, [], False, "test"]

        for curr_data_type in invalid_data_types:
            with self.assertRaises(ValueError) as ex:
                self.int_list.insert(0, curr_data_type)

            self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual(3, len(self.int_list.get_data()))

    def test_get_biggest_method(self):
        # state before sorting
        self.assertEqual([1, 2, 3], self.int_list.get_data())
        result = self.int_list.get_biggest()
        self.assertEqual(3, result)

    def test_get_idx(self):
        # the 0 index element is 1 in the list
        self.assertEqual(self.int_list.get_data()[0], 1)

        # calling the method
        curr_element = self.int_list.get_index(1)

        self.assertEqual(0, curr_element)


if __name__ == "__main__":
    unittest.main()
