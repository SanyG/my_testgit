# -*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner
import time

#获取测试用例路径
test_dir=os.path.dirname(os.path.realpath(__file__))

testcase_dir=os.path.join(test_dir,'common')

#获取测试报告地址
report_dir=os.path.dirname(os.path.realpath(__file__))

testreport_dir=os.path.join(report_dir,'report')

#print(testcase_dir)
#print(testreport_dir)


#自动搜索指定目录下的cas，构造测试集, 执行顺序是命名顺序：先执行test_add，再执行test_sub
#自动执行测试用例
def run_case():

    rule='demo_test*.py'
    discover=unittest.defaultTestLoader.discover(testcase_dir,rule)
    print(discover)
    return (discover)



if __name__ == '__main__':
    #获取当前时间
    now=time.strftime('%Y-%y-%d-%H_%m_%s',time.localtime(time.time()))

    #报告文件路径
    report_basepath=os.path.join(testreport_dir,'result_'+now+'.html')


#打开一个文件，将result写入此file中
    fp=open(report_basepath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'接口测试报告，测试结果如下：',
                                         description=u'用例执行情况如下：')

    #批量执行用例
    runner.run(run_case())

    #关闭文件
    fp.close()
