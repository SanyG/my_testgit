#coding:utf-8
import xlrd
import unittest

class test_readexcel_demo(unittest.TestCase):
    def test_readexcel_demo(self,index_number,row_number,clo_number):
        data=xlrd.open_workbook('/Users/jin/PycharmProjects/requestDemo/case/test.xlsx')
        table=data.sheet_by_index(index_number)
        #table=data.sheets()[0]
        #clo1=table.col_values(1)
        #row1=table.row_values(1)
        #cell_A1=table.col_values(1)[0]
        cell_B2=table.cell(row_number,clo_number).value

        #print(clo1)
        #print(row1)
        #print(cell_A1)
        #print(cell_B2)
        return cell_B2


#if __name__=='__main__':
    #unittest.main()