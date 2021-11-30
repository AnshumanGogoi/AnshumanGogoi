from  utilities import  excelUtil

class Test_003_DDT_Login:
    path = "/Users/anshumangogoi/PycharmProjects/TestingFrameWork/TestData/TestData2.xlsx"

    def test_login_ddt(self):
        self.rows = excelUtil.getRowCount(self.path, 'Sheet 1')
        print("Number of rows in Excel:", self.rows)
        for x in range(2,self.rows+1):
            self.user = excelUtil.readData(self.path,'Sheet 1',x,1)
            self.password = excelUtil.readData(self.path, 'Sheet 1', x, 2)
            self.expected = excelUtil.readData(self.path, 'Sheet 1', x, 3)
            print(self.user)
            print(self.password)
            print(self.expected)
