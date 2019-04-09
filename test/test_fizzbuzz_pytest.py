import pytest
from src import fizzbuzz


class Testfizzbuzz():
    def test_fizzBuzz_0(self, capsys, result):
        fizzbuzz.fizzBuzz(0)
        assert capsys.readouterr().out.strip() == result.fizzbuzz.value

    def test_fizzBuzz_1(self, capsys):
        fizzbuzz.fizzBuzz(1)
        assert capsys.readouterr().out.strip() == '1'

    def test_fizzBuzz_3(self, capsys, result):
        fizzbuzz.fizzBuzz(3)
        assert capsys.readouterr().out.strip() == result.fizz.value

    def test_fizzBuzz_5(self, capsys, result):
        fizzbuzz.fizzBuzz(5)
        assert capsys.readouterr().out.strip() == result.buzz.value

    def test_fizzBuzz_15(self, capsys, result):
        fizzbuzz.fizzBuzz(15)
        assert capsys.readouterr().out.strip() == result.fizzbuzz.value

    def test_fizzBuzz_30(self, capsys, result):
        fizzbuzz.fizzBuzz(30)
        assert capsys.readouterr().out.strip() == result.fizzbuzz.value

if __name__ == "__main__":
    pytest.main()
