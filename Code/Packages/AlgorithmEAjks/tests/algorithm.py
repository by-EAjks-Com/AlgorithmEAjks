#   Copyright (C) 2020-2023 Andrea and Eric DELAGE <Contact@by-EAjks.Com>
#   See the file "LICENSE" for the full license governing this code.

import unittest

from algorithmeajks.algorithm import add_one

class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)

if __name__ == '__main__':
    unittest.main()
