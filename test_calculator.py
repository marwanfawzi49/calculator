from calculator.calculator import add,subtract,divide,multipy

def test_addition():
    assert add(2,3,) == 5

def test_subtraction():
    assert subtract(5,2) == 3

def test_multiply():
    assert multipy(4,3) == 12

def test_division():
    assert divide(10,2) == 5

def test_dividing_by_zero():
   assert divide(5,0) == "Error: dividing by zero"
