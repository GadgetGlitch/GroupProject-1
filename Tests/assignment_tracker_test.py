import unittest
import Assignment_Tracker
from datetime import datetime

class TestFunctions(unittest.TestCase):

    def test_get_timezone_cities(self):
        cities = ['Paris', 'Riyadh', 'New York']
        time_zones = []
        for i in cities:
            time_zones.append(Assignment_Tracker.get_timezone_from_city(i))
        self.assertEqual(time_zones[0], 'Europe/Paris')
        self.assertEqual(time_zones[1], 'Asia/Riyadh')
        self.assertEqual(time_zones[2], 'America/New_York')

    def test_get_timezone_bad_input(self):
        cities = ['jkashdfj', 'b94ju84f', 'u8hf8jdi']
        time_zones = []
        for i in cities:
            time_zones.append(Assignment_Tracker.get_timezone_from_city(i))
        self.assertEqual(time_zones[0], None)
        self.assertEqual(time_zones[1], None)
        self.assertEqual(time_zones[2], None)

    def test_get_predeadline_dates(self):
        dates = ['2/12/24 23:59:59', '12/12/24 23:59:59','1/1/24 23:59:59']
        predeadline_dates = ['2/11/24 23:59:59', '12/11/24 23:59:59','12/31/23 23:59:59'] #using default buffer days = 1
        date_format = []
        predeadline_expected = []
        predeadline_actual = []
        
        for i in range(3):
            date_format.append(datetime.strptime(dates[i],'%m/%d/%y %H:%M:%S'))
            predeadline_expected.append(datetime.strptime(predeadline_dates[i],'%m/%d/%y %H:%M:%S'))
            
        for j in date_format:
            predeadline_actual.append(Assignment_Tracker.get_predeadline(j))

        self.assertEqual(predeadline_actual[0], predeadline_expected[0])
        self.assertEqual(predeadline_actual[1], predeadline_expected[1])
        self.assertEqual(predeadline_actual[2], predeadline_expected[2])
                                
            

