import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
from Ui_main import Ui_MainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import QStringListModel

rdUrl = './RD_HS.txt'

# 判断list中所有元素是否都在集合set中
def listInSet(li, se):
    for i in li:
        if i not in se:
            return False
    return True

def getRules():
    with open(rdUrl, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        p = []
        q = []
        for i in lines:
            i = i.split(' ')
            q.append(i[len(i)-1])
            p.append(i[:len(i)-1])
        return p, q

def getP():
    with open(rdUrl, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        p = set([])
        for i in lines:
            i = i.split(' ')
            for j in i[:len(i)-1]:
                p.add(j)
        return p

# 前向推理
def inference(p, q, input):
    DB = set(input)
    process = []
    animal = []
    flag = 0
    i = 0
    pUsed = []
    while i < len(p):
        if listInSet(p[i], DB) and i not in pUsed:
            DB.add(q[i]) # 将结论放入条件
            animal.append(q[i])
            process.append("{} --> {}".format(p[i], q[i]))
            flag = 1
            pUsed.append(i)
        i += 1
        if i == len(p) and flag == 1 : # 结果加入条件的顺序问题
            i = 0
            flag = 0
    return process, '、'.join(animal)

# 反向推理
def backInference(p, q, input):
    DB = set(input)
    process = set([])
    flag = 0
    i = 0
    pUsed = []
    while i < len(q):
        if q[i] in DB and i not in pUsed:
            for item in p[i]:
                DB.add(item)
            pUsed.append(i)
            process.add("{} --> {}".format(q[i], p[i]))
            flag = 1
        i += 1
        if i == len(q) and flag == 1 :
            i = 0
            flag = 0
    return process

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        #p,q
        self.p, self.q = getRules()

        # 加载P
        self.pSet = list(getP())
        self.pModel=QStringListModel(self)
        self.pModel.setStringList(self.pSet)
        self.pList.setModel(self.pModel)

        self.inputSet = []
        self.inputModel=QStringListModel(self)
        self.inputModel.setStringList(self.inputSet)
        self.inputList.setModel(self.inputModel)

        self.addToInputButton.clicked.connect(self.addToInput)
        self.deleteFromInputButton.clicked.connect(self.deleteFromInput)
        self.pushButton.clicked.connect(self.infer)

    def insertIntoList(self, listItem, content):
        row = listItem.rowCount()
        listItem.insertRow(row)
        listItem.setData(listItem.index(row), content)
    
    # button's function
    def addToInput(self):
        indexes = self.pList.selectedIndexes()
        for index in indexes:
            index = index.row()
            self.insertIntoList(self.inputModel, self.pSet[index])
            self.pModel.removeRow(index)
            # 更新数据
            self.inputSet.append(self.pSet[index])
            self.pSet.remove(self.pSet[index])
    
    def deleteFromInput(self):
        indexes = self.inputList.selectedIndexes()
        for index in indexes:
            index = index.row()
            self.insertIntoList(self.pModel, self.inputSet[index])
            self.inputModel.removeRow(index)
            # 更新数据
            self.pSet.append(self.inputSet[index])
            self.inputSet.remove(self.inputSet[index])
    
    def infer(self):
        if self.radioButton.isChecked():
            if self.inputSet != []:
                routes, answer = inference(self.p, self.q, self.inputSet)
                if answer=="":
                    answer = "404找不到（o´・ェ・｀o）"

                self.routeModel=QStringListModel(self)
                self.routeModel.setStringList(routes)
                self.listView.setModel(self.routeModel)
                
                self.textEdit.setText(answer)
            else:
                reply = QMessageBox.warning(self,
                                    "警告",  
                                    "请输入事实",  
                                    QMessageBox.Yes)
        else:
            if self.textEdit.toPlainText() != '':
                routes = backInference(self.p, self.q, [self.textEdit.toPlainText()])
                self.routeModel=QStringListModel(self)
                self.routeModel.setStringList(routes)
                self.listView.setModel(self.routeModel)
            else:
                reply = QMessageBox.warning(self,
                                    "警告",  
                                    "请输入结论",  
                                    QMessageBox.Yes)
    
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
