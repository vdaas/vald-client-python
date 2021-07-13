import unittest

from tests import test_e2e


class SequentialTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        testcase_methods = list(testCaseClass.__dict__.keys())
        test_names.sort(key=testcase_methods.index)
        return test_names


if __name__ == "__main__":
    unittest.main(test_e2e, testLoader=SequentialTestLoader())
