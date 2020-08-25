class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

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


#--------
import unittest


class TestIntegerList(unittest.TestCase):
    def _test_inteferListWnenNotInteger_raise(self):
        with self.assertRaises(Exception) as context:
            IntegerList(1,2,3,4,5)

        self.assertIsNotNone(context.exception)

    def test_integerListWhenOnlyIntegerShouldStore(self):
        values = [1,2,3,4,5]
        l = IntegerList(*values)

        self.assertListEqual(values, l.get_data())

    def test_integerListAddWhenValueisInteger_ShouldBeAdded(self):
        test = IntegerList()
        test.add(1)

        self.assertEqual([1], test.get_data())


    def test_integerListAddWhenValueisNotIntererRaiseException(self):
        test = IntegerList()

        with self.assertRaises(Exception) as context:
            test.add('TEST')

        self.assertIsNotNone(context.exception)

    def test_removeIndex_whenIndexIsValid_ShouldRemoveElement_andreturn(self):
        test = IntegerList(1,2,3,4,5,6,7)
        returned = test.remove_index(3)
        expected = 4
        self.assertEqual(returned, expected)
        self.assertListEqual([1,2,3,5,6,7], test.get_data())

    def test_removeIndex_whenIndexIsNotValie_RaiseException(self):
        test = IntegerList(1,2,3,4,5,6,7)

        with self.assertRaises(Exception) as context:
            test.remove_index(len(test.get_data()))

        self.assertIsNotNone(context.exception)

    def test_getIndex_whenIndexIsValid_ShouldReturn(self):
        test = IntegerList(1,2,3,4,5,6,7)
        returned = test.get(3)
        expected = 4
        self.assertEqual(returned, expected)


    def test_getIndex_whenIndexIsNotValie_RaiseException(self):
        test = IntegerList(1,2,3,4,5,6,7)

        with self.assertRaises(Exception) as context:
            test.get(len(test.get_data()))

        self.assertIsNotNone(context.exception)

    def test_getBiggestShouldReturnBigest(self):
        test = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = test.get_biggest()

        self.assertEqual(7, returned)

    def test_getIndexShouldReturnIndex(self):
        test = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = test.get_index(4)
        expected = 3

        self.assertEqual(expected, returned)


    def test_insertWhenIndexIsValidShouldReturnIndex(self):
        test = IntegerList(1, 2, 3, 4, 5, 6, 7)
        test.insert(2, -1)
        self.assertEqual([1, 2, -1, 3, 4 ,5 ,6 ,7], test.get_data())

    def test_insertWhenIndexIsInValidShouldShouldReturnRaise(self):
        test = IntegerList(1, 2, 3, 4, 5, 6, 7)
        with self.assertRaises(Exception) as context:
            test.insert(len(test.get_data()), -1)

        self.assertIsNotNone(context.exception)

    def test_insertWhenvalueisNotIntegerRaiseException(self):
        test = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            test.insert(0, True)

        self.assertIsNotNone(context.exception)

if __name__ == '__main__':
    unittest.main()