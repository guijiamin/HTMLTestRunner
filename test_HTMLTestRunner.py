# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner
import sys,os
class Mydemo(unittest.TestCase):
    def test1(self):
        print("excute test1")

    def test2(self):
        print("excute test2")
        raise AssertionError("test2 fail")

    def test3(self):
        print("excute test3")

    def test4(self):
        print("excute test4")

if __name__ == '__main__':
    module_name=os.path.basename(sys.argv[0]).split(".")[0]
    module=__import__(module_name)
    fp=open("./new.html","wb")
    runner=HTMLTestRunner.HTMLTestRunner(fp, verbosity=2)
    all_suite=unittest.defaultTestLoader.loadTestsFromModule(module)
    runner.run(all_suite)
    fp.close()