# Any fixture added here in the conftest.py file will be available to all the test files present in that folder
import pytest


@pytest.fixture(scope="class")
# NOTE:
# if we do not add any scope above then it default apply at method level
# once specified with class name then it will get applied on class level
def setup():
    print("This will be executed first.")
    yield  # whatever we write after yield keyword that will be executed in the end of the test case
    print("This will execute at the end post Test case execution.")


# Data driven can be done with return statement in tuple format
@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Abhay", "Thakur", "www.rahulshettyacademy.com"]


# Parameterization in Fixtures : can be done with return statement in tuple format
# @pytest.fixture(params=["chrome", "Firefox", "IE"])

@pytest.fixture(params=[("chrome", "Abhay", "Thakur"), ("Firefox", "Abhay"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
