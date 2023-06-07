import pytest


@pytest.mark.smoke # Marked the below test case as smoke test
def test_firstProgram():
    message = "Hello"
    assert message == "Hi", "Test failed because strings do not match"


def test_secondProgram():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"
