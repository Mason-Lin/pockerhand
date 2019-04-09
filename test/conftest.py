import pytest
from enum import Enum


@pytest.fixture(scope='module')
def result():
    class Expected(Enum):
        fizzbuzz = 'fizzBuzz'
        fizz = 'fizz'
        buzz = 'buzz'
    return Expected
