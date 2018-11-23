#coding:utf-8
import unittest
import readexcel



class test_demo_test1(unittest.TestCase):
    def test_demo2(self):
        a=str(readexcel.test_readexcel_demo.test_readexcel_demo(self,0,3,2))
        #print(a)
        self.assertEqual(a,u'男')



