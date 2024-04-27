import unittest

import eightbdkbd
from eightbdkbd import keys


class TestMappings(unittest.TestCase):

    def test_hwkeys_in_usage(self):
        self.assertListEqual(
            [], [key for key in keys.HWKEY if key not in keys.USAGE],
            msg="These should be aliased in keys.USAGE")


if __name__ == '__main__':
    unittest.main()
