import argparse
import unittest


class TestHello(unittest.TestCase):
    MSG = "world"

    def test__hello_config(self):
        print(f'hello {self.MSG}')
        self.assertTrue(True)
        print(f'it worked {self.MSG}')



if __name__ == '__main__':
    p = argparse.ArgumentParser(description='hello argparse x unittest')

    p.add_argument('-msg', '-m', dest='msg')

    a = p.parse_args()

    # read config file, optionally for a specific context
    if a.msg:

        TestHello.MSG = a.msg

    unittest.main()
