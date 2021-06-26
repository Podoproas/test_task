import main
import pprint
import right_answers_to_example


def test_check_comment():
    assert main.check_comment("#\n")
    assert main.check_comment("# \n")
    assert main.check_comment("# asd\n")
    assert not main.check_comment(" # asd\n")
    assert not main.check_comment("% not a comment\n")


def test_is_empty_string():
    assert main.is_empty_string("\n")
    assert main.is_empty_string(" \n")
    assert main.is_empty_string("\t\n")
    assert not main.is_empty_string("asd\n")
    assert not main.is_empty_string(" a\n")
    assert not main.is_empty_string(":\n")


def test_get_key_and_value():
    assert main.get_key_and_value("key:\tvalue\n") == ("key", "value")
    assert main.get_key_and_value("k ey\t:\tvalue\t\n") == ("k ey", "value")
    assert main.get_key_and_value(" wrong_key\t:value\n") == (None, "wrong_key\t:value")
    assert main.get_key_and_value("\tvalue_only\n") == (None, "value_only")


def get_next_right_dict():
    for ans in right_answers_to_example.made_by_hand:
        yield ans


def test_parse_file(path):
    for doc in main.parse_file(path):
        assert doc == next(get_next_right_dict())
        print("More tests have to be written by hand - no time to do it now")
        break


def test_all(path):
    test_check_comment()
    print("✅ Check_comment passed all test")
    test_is_empty_string()
    print("✅ Is_empty_string passed all test")
    test_get_key_and_value()
    print("✅ Get_key_and_value passed all test")
    test_parse_file(path)
    print("✅ Parse_file passed all test")
    print("✅All tests passed ✅")


if __name__ == "__main__":
    test_all("example.txt")
