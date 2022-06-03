import pytest

@pytest.fixture()
def setup():
    print("Trial Trial")

def testmenthod(setup):
    print("Trial Trial")

def testmethod2(setup):
    print("Trial Trial")