# NOTE : Any pytest file name should start with "test_" or end with "_test"
# pytest method names must start with test
# Any code should be wrapped in method only
# Multiple test method with same name are not allowed in pytest, it will override it with latest one

###############################################

# Important Terminal Commands to know for pytest :
# To run a specific file with py.test <filename>
# To run a specific pytest file via terminal/command line : "py.test test_demo2.py -v -s"
# To run a specific pytest which has some particular text in pytest method : "py.test -k <text_that_match_pytest_methodName> -v -s" ---> e.g : "py.test -k secondProgram -v -s"
# -k stands for methods names execution
# -s stands for logs in output
# -v stands for more infor metadata

import pytest


def test_firstProgram():
    print("Hi! There")


def test_secondProgram():
    print("This is a Abhay Thakur.")
