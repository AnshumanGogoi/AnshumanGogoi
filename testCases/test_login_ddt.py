from  utilities import  excelUtil

class Test_002_DDT_Login:
    path = "/Users/anshumangogoi/PycharmProjects/TestingFrameWork/TestData/TestData3.xlsx"

    def test_login_ddt(self):
        self.rows = excelUtil.getRowCount(self.path, 'Sheet 1')
        self.title = excelUtil.writeData(self.path,'Sheet 1',1,4,'Actual Result')
        print("Number of rows in Excel:", self.rows)
        for x in range(2,self.rows+1):
            self.user = excelUtil.readData(self.path,'Sheet 1',x,1)
            self.password = excelUtil.readData(self.path, 'Sheet 1', x, 2)
            self.expected = excelUtil.readData(self.path, 'Sheet 1', x, 3)
            self.actual = excelUtil.writeData(self.path, 'Sheet 1',x, 4,'Pass')

            print(self.user)
            print(self.password)
            print(self.expected)

