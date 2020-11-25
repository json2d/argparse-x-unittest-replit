import argparse
import unittest
import sys


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='hello argparse x unittest')

    p.add_argument('-msg', '-m', dest='msg')

    a = p.parse_args()

    class TestHello(unittest.TestCase):
        MSG = "world"

        def test__hello_config(self):
            print(f'hello {self.MSG}')
            self.assertTrue(True)
            print(f'it worked {self.MSG}')

    if a.msg:
        TestHello.MSG = a.msg

        # workaround how both argparse and unittest both try to read argv: 
        # - pop off args for argparse before running unittest.main() which is when unittest reads from argv
        # - careful w/ arg name conflict w/ ones expected by unittest
        sys.argv.pop()
        sys.argv.pop()

    unittest.main()
