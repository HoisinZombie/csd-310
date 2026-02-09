import unittest
from city_functions import get_city

class CityTestCase (unittest.TestCase) :
    
    def test_city_country(self):
        location = get_city('Hokkaido', 'Japan', '5,000,000', 'Japanese')
        self.assertEqual (location, 'Hokkaido, Japan - Population 5,000,000, Japanese')

if __name__ == '__main__':
    unittest.main()