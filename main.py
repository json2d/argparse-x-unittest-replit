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

    if a.msg:

        TestHello.MSG = a.msg

    # bypass unittest reading the arguments and skip ahead to running tests
    # from: https://stackoverflow.com/a/20266206
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestHello)
    runner.run(itersuite)
