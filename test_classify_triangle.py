import pytest
from classify_triangle import classify_triangle

def test_equilateral_triangle():
    assert classify_triangle(4,4,4)== "Equilateral Triangle"
def test_isosceles_triangle():
    assert classify_triangle(6,6,4)== "Isosceles Triangle"
def test_scalane_triangle():
    assert classify_triangle(4,5,6)== "Scalane Triangle"
def test_right_triangle():
    assert classify_triangle(3,4,5)=="Right Angled Triangle"
def test_invalid_triangle_zero():
    assert classify_triangle(0,3,4)== "Not a Triangle"
def test_negative_side():
    assert classify_triangle(-3, 4, 5)== "Not a Triangle"
def test_invalid_triangle_inequality():
    assert classify_triangle(1,2,3)== "Not a Triangle"



