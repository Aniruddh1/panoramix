import unittest
from datetime import datetime

from dateutil.relativedelta import relativedelta

from caravel.utils import parse_human_datetime_ex


class TimePeriodTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TimePeriodTests, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_custom_periods(self):
        # Testing by running all the examples
        periods = [
            # Between Tusday and Saturday: Wednesday
            [datetime(2016, 4, 6, 10, 20, 10),
                [
                    ['this year', datetime(2016, 1, 1)],
                    ['end of year', datetime(2016, 12, 31)],
                    ['this month', datetime(2016, 4, 1)],
                    ['end of month', datetime(2016, 4, 30)],
                    ['this week', datetime(2016, 4, 4)],
                    ['end of week', datetime(2016, 4, 10)],
                    ['this day', datetime(2016, 4, 6)],
                    ['end of day', datetime(2016, 4, 6, 23, 59, 59)],
                    ['this quarter', datetime(2016, 4, 1)],
                    ['end of quarter', datetime(2016, 6, 30)],
                    ['this monday', datetime(2016, 4, 4)],
                    ['this tuesday', datetime(2016, 4, 5)],
                    ['this wednesday', datetime(2016, 4, 6)],
                    ['this thursday', datetime(2016, 4, 7)],
                    ['this friday', datetime(2016, 4, 8)],
                    ['this saturday', datetime(2016, 4, 9)],
                    ['this sunday', datetime(2016, 4, 10)]
                ]
            ],
        # Monday
            [datetime(2016, 4, 4, 10, 20, 10),
                [
                    ['this year', datetime(2016, 1, 1)],
                    ['end of year', datetime(2016, 12, 31)],
                    ['this month', datetime(2016, 4, 1)],
                    ['end of month', datetime(2016, 4, 30)],
                    ['this week', datetime(2016, 4, 4)],
                    ['end of week', datetime(2016, 4, 10)],
                    ['this day', datetime(2016, 4, 4)],
                    ['end of day', datetime(2016, 4, 4, 23, 59, 59)],
                    ['this quarter', datetime(2016, 4, 1)],
                    ['end of quarter', datetime(2016, 6, 30)],
                    ['this monday', datetime(2016, 4, 4)],
                    ['this tuesday', datetime(2016, 4, 5)],
                    ['this wednesday', datetime(2016, 4, 6)],
                    ['this thursday', datetime(2016, 4, 7)],
                    ['this friday', datetime(2016, 4, 8)],
                    ['this saturday', datetime(2016, 4, 9)],
                    ['this sunday', datetime(2016, 4, 10)]
                ]
            ],
        # Sunday
            [datetime(2016, 4, 10, 10, 20, 10),
                [
                    ['this year', datetime(2016, 1, 1)],
                    ['end of year', datetime(2016, 12, 31)],
                    ['this month', datetime(2016, 4, 1)],
                    ['end of month', datetime(2016, 4, 30)],
                    ['this week', datetime(2016, 4, 4)],
                    ['end of week', datetime(2016, 4, 10)],
                    ['this day', datetime(2016, 4, 10)],
                    ['end of day', datetime(2016, 4, 10, 23, 59, 59)],
                    ['this quarter', datetime(2016, 4, 1)],
                    ['end of quarter', datetime(2016, 6, 30)],
                    ['this monday', datetime(2016, 4, 4)],
                    ['this tuesday', datetime(2016, 4, 5)],
                    ['this wednesday', datetime(2016, 4, 6)],
                    ['this thursday', datetime(2016, 4, 7)],
                    ['this friday', datetime(2016, 4, 8)],
                    ['this saturday', datetime(2016, 4, 9)],
                    ['this sunday', datetime(2016, 4, 10)]
                ]
            ],
            # last - next
            # Between Tusday and Saturday: Wednesday
            [datetime(2016, 4, 6, 10, 20, 10),
                 [
                     ['last year', datetime(2015, 1, 1)],
                     ['next year', datetime(2017, 1, 1)],
                     ['last month', datetime(2016, 3, 1)],
                     ['next month', datetime(2016, 5, 1)],
                     ['last week', datetime(2016, 3, 28)],
                     ['next week', datetime(2016, 4, 11)],
                     ['last day', datetime(2016, 4, 5)],
                     ['next day', datetime(2016, 4, 7)],
                     ['last quarter', datetime(2016, 1, 1)],
                     ['next quarter', datetime(2016, 7, 1)],
                     ['last monday', datetime(2016, 4, 4)],
                     ['last tuesday', datetime(2016, 4, 5)],
                     ['last wednesday', datetime(2016, 3, 30)],
                     ['last thursday', datetime(2016, 3, 31)],
                     ['last friday', datetime(2016, 4, 1)],
                     ['last saturday', datetime(2016, 4, 2)],
                     ['last sunday', datetime(2016, 4, 3)],
                     ['next monday', datetime(2016, 4, 11)],
                     ['next tuesday', datetime(2016, 4, 12)],
                     ['next wednesday', datetime(2016, 4, 13)],
                     ['next thursday', datetime(2016, 4, 7)],
                     ['next friday', datetime(2016, 4, 8)],
                     ['next saturday', datetime(2016, 4, 9)],
                     ['next sunday', datetime(2016, 4, 10)]
                ]
            ],
            # Between Tusday and Saturday: Wednesday with value
            [datetime(2016, 4, 6, 10, 20, 10),
                 [
                     ['last 2 years', datetime(2014, 1, 1)],
                     ['next 2 years', datetime(2018, 1, 1)],
                     ['last 2 months', datetime(2016, 2, 1)],
                     ['next 2 months', datetime(2016, 6, 1)],
                     ['last 2 weeks', datetime(2016, 3, 21)],
                     ['next 2 weeks', datetime(2016, 4, 18)],
                     ['last 2 days', datetime(2016, 4, 4)],
                     ['next 2 days', datetime(2016, 4, 8)],
                     ['last 2 quarters', datetime(2015, 10, 1)],
                     ['next 2 quarters', datetime(2016, 10, 1)],
                     ['last 2 mondays', datetime(2016, 3, 28)],
                     ['last 2 tuesdays', datetime(2016, 3, 29)],
                     ['last 2 wednesdays', datetime(2016, 3, 30)],
                     ['last 2 thursdays', datetime(2016, 3, 24)],
                     ['last 2 fridays', datetime(2016, 3, 25)],
                     ['last 2 saturdays', datetime(2016, 3, 26)],
                     ['last 2 sundays', datetime(2016, 3, 27)],
                     ['next 2 mondays', datetime(2016, 4, 18)],
                     ['next 2 tuesdays', datetime(2016, 4, 19)],
                     ['next 2 wednesdays', datetime(2016, 4, 13)],
                     ['next 2 thursdays', datetime(2016, 4, 14)],
                     ['next 2 fridays', datetime(2016, 4, 15)],
                     ['next 2 saturdays', datetime(2016, 4, 16)],
                     ['next 2 sundays', datetime(2016, 4, 17)]
                ]
            ]
        ]

        for now, dataset in periods:
            for p, d in dataset:
                res = parse_human_datetime_ex(p, now)
                self.assertEqual(res, d, p + ' returned ' + str(res) + ' expected ' + str(d))

            #so far
            for p, d in dataset:
                p += ' so far'
                d += relativedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
                res = parse_human_datetime_ex(p, now)
                self.assertEqual(res, d, p + ' returned ' + str(res) + ' expected ' + str(d))

if __name__ == '__main__':
    unittest.main()
