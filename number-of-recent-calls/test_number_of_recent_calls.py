import unittest

from number_of_recent_calls import RecentCounter


class TestRecentCounter(unittest.TestCase):
    def test_example_1(self):
        counter = RecentCounter()
        self.assertEqual([counter.ping(t) for t in [1, 100, 3001, 3002]], [1, 2, 3, 3])

    def test_boundary_is_inclusive(self):
        counter = RecentCounter()
        self.assertEqual([counter.ping(t) for t in [1000, 4000, 4001]], [1, 2, 2])

    def test_old_calls_expire(self):
        counter = RecentCounter()
        self.assertEqual([counter.ping(t) for t in [1, 2, 3, 10000]], [1, 2, 3, 1])


if __name__ == "__main__":
    unittest.main()
