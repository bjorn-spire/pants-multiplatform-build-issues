import cffi

import library


def test_assert_something_on_cffi():
    assert cffi.__version__ == '1.12.1'
