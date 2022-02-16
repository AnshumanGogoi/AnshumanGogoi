import pytest
input_total = 100

def test_total_div_by_5():
    assert input_total%5==0

def test_total_div_by_9():
    assert input_total % 9 == 0

def test_total_div_by_10():
    assert input_total % 10 == 0
