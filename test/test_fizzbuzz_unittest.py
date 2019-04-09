import unittest
from src import fizzbuzz
from src.captured_output import captured_output
from enum import Enum


@unittest.skip
class fizzbuzzUnitTestCase(unittest.TestCase):
    def setUp(self):
        class Expected(Enum):
            fizzbuzz = 'fizzBuzz'
            fizz = 'fizz'
            buzz = 'buzz'
        self.fizzbuzz = Expected.fizzbuzz.value
        self.fizz = Expected.fizz.value
        self.buzz = Expected.buzz.value

    def test_fizzBuzz_0(self):
        expected = self.fizzbuzz
        with captured_output() as (out, _err):
            fizzbuzz.fizzBuzz(0)
        self.assertEqual(out.getvalue().strip(), expected)

    def test_fizzBuzz_1(self):
        expected = '1'
        with captured_output() as (out, _err):
            fizzbuzz.fizzBuzz(1)
        self.assertEqual(out.getvalue().strip(), expected)

    def test_fizzBuzz_3(self):
        expected = self.fizz
        with captured_output() as (out, _err):
            fizzbuzz.fizzBuzz(3)
        self.assertEqual(out.getvalue().strip(), expected)

    def test_fizzBuzz_5(self):
        expected = self.buzz
        with captured_output() as (out, _err):
            fizzbuzz.fizzBuzz(5)
        self.assertEqual(out.getvalue().strip(), expected)

    def test_fizzBuzz_15(self):
        expected = self.fizzbuzz
        with captured_output() as (out, _err):
            fizzbuzz.fizzBuzz(15)
        self.assertEqual(out.getvalue().strip(), expected)

    def test_fizzBuzz_30(self):
        expected = self.fizzbuzz
        with captured_output() as (out, _err):
            fizzbuzz.fizzBuzz(30)
        self.assertEqual(out.getvalue().strip(), expected)

if __name__ == "__main__":
    unittest.main()
