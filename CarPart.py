import unittest

from carpart import CarPart  # Import the CarPart class from your code

class TestCarPart(unittest.TestCase):
    def setUp(self):
        # Create an instance of CarPart for testing
        self.car_part = CarPart(1, "Engine", "High-performance engine", "ABC Motors", 1500.00)

    def test_car_part_attributes(self):
        self.assertEqual(self.car_part.id, 1)
        self.assertEqual(self.car_part.name, "Engine")
        self.assertEqual(self.car_part.description, "High-performance engine")
        self.assertEqual(self.car_part.manufacturer, "ABC Motors")
        self.assertEqual(self.car_part.price, 1500.00)
        self.assertEqual(self.car_part.modelCompatible, [])

    def test_add_compatible_model(self):
        self.car_part.modelCompatible.append("Model X")
        self.assertIn("Model X", self.car_part.modelCompatible)

if __name__ == '__main__':
    unittest.main()
