import unittest
from classify_triangle import classify_triangle


class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral Triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(4, 4, 5), "Isosceles Triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(6, 7, 8), "Scalene Triangle")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right Angled Triangle")

    def test_not_triangle_zero(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Not a Triangle")

    def test_not_triangle_negative(self):
        self.assertEqual(classify_triangle(-1, 4, 5), "Not a Triangle")

    def test_not_triangle_rule(self):
        self.assertEqual(classify_triangle(3, 5, 9), "Not a Triangle")


if __name__ == "__main__":
    unittest.main()


