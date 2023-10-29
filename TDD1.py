import unittest
from car_factory import CarFactory

class TestCarFactory(unittest.TestCase):
    def test_spindler_battery_service_criteria(self):
        # Create a CarFactory instance
        factory = CarFactory()
        
        # Ensure the initial service interval for Spindler battery is 2 years
        spindler_battery = factory.get_spindler_battery()
        self.assertEqual(spindler_battery.get_service_interval(), 2)
        
        # Upgrade the Spindler battery service interval to 3 years
        factory.upgrade_spindler_battery_service_interval(3)
        self.assertEqual(spindler_battery.get_service_interval(), 3)

if __name__ == '__main__':
    unittest.main()
