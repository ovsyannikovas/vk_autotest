import pytest


class TestStr:
    def test_str_1(self):
        string = "vk"
        assert string.title() == "Vk"

    @pytest.mark.parametrize("test_input_s, test_expected",
                             [("Hello" + "World", "HelloWorld"), ("VK" * 5, "VKVKVKVKVK"),
                              ("test".upper(), "TEST")])
    def test_str_2(self, test_input_s, test_expected):
        assert test_input_s == test_expected

    def test_str_3(self):
        test_string = "string"
        try:
            test_string.append(666)
            assert test_string[-1] == 666
        except AttributeError:
            pass


class TestList:
    def test_list_1(self):
        test_list = list()
        test_list.append(666)
        assert test_list[-1] == 666

    @pytest.mark.parametrize("test_input_l, test_expected",
                             [([1, 2, 3], [3, 2, 1]), ([666], [666]),
                              ([7, 8, 9, 10], [10, 9, 8, 7])])
    def test_list_2(self, test_input_l, test_expected):
        assert list(reversed(test_input_l)) == test_expected

    def test_list_3(self):
        test_list = [1, 2, 3]
        try:
            test_list.add(666)
            assert 666 in test_list
        except AttributeError:
            pass
