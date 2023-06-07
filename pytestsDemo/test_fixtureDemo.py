# Fixtures :
# These are kind of prerequisite which we want to run before and after any test case executes everytime.
import pytest


@pytest.mark.usefixtures("setup")
class TestFixturesExample:

    def test_fixtureDemo(self):
        print("This will execute steps in fixtureDemo method.")

    def test_fixtureDemo1(self):
        print("This will execute steps in fixtureDemo1 method.")

    def test_fixtureDemo2(self):
        print("This will execute steps in fixtureDem2 method.")

    def test_fixtureDemo3(self):
        print("This will execute steps in fixtureDemo3 method.")
