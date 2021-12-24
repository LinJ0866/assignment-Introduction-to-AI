import copy
import time

expandCount = 0
newCount = 0

class grid:
    def __init__(self, stat):
        self.pre = None
        self.stat = stat
        self.target = [[1, 2, 3, 4], [5, 6 ,7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        self.update()
    def update(self): #个更新f(n)， f(n)=g(n)+h(n)
        self.g = self.updateG()
        self.h = self.updateH1()
        self.f = self.g + self.h
    
    # 实际代价（深度deep）
    def updateG(self):
        if self.pre != None:
            return self.pre.g + 1
        else:
            return 0

    # h(1) 不在位数
    def updateH1(self):
        count = 0
        for i in range(len(self.stat)):
            for j in range(len(self.stat[i])):
                if self.stat[i][j] != self.target[i][j]:
                    count += 1
        return count
    
    # h(2) 和目标状态距离
    def updateH2(self):
        count = 0
        for i in range(4):
            for j in range(4):
                targetX=self.target[i][j]
                nowP_Y, nowP_X=self.findX(targetX)
                #曼哈顿距离之和
                count += abs(nowP_X-i)+abs(nowP_Y-j)
        return count
    
    # h(3) 宽度优先搜索(=0)
    def updateH3(self):
        return 0

    # 寻找任意数
    def findX(self, x):
        for i in range(len(self.stat)):
                for j in range(len(self.stat[i])):
                    if self.stat[i][j] == x:
                        return j, i
    
    # 寻找空白格
    def find0(self):
        for i in range(len(self.stat)):
                for j in range(len(self.stat[i])):
                    if self.stat[i][j] == 0:
                        return j, i
    # 扩展当前状态
    def expand(self):
        global expandCount
        expandCount += 1
        gridList = []
        self.zero_x, self.zero_y = self.find0() # 空白格的位置
        if self.zero_x > 0:
            gridList.append(self.left())
        if self.zero_x < 3:
            gridList.append(self.right())
        if self.zero_y > 0:
            gridList.append(self.up())
        if self.zero_y < 3:
            gridList.append(self.down())
        return gridList
    
    def left(self):
        return self.move(-1, 0)
    def right(self):
        return self.move(1, 0)
    def up(self):
        return self.move(0, -1)
    def down(self):
        return self.move(0, 1)
    
    def move(self, x, y):
        newStat = copy.deepcopy(self.stat) #deepcopy多维列表的复制，防止指针赋值将原列表改变
        tmp = newStat[self.zero_y+y][self.zero_x+x]
        newStat[self.zero_y+y][self.zero_x+x] = 0
        newStat[self.zero_y][self.zero_x] = tmp # 交换空白格
        return newStat

    # 获取最短路径
    def getMoves(self):
        moves = []
        while self.pre != None:
            moves.append(self.stat)
            self = self.pre
        moves.append(self.stat)
        moves.reverse()
        self.beautify(moves)
    # 美化输出
    def beautify(self, moves):
        for i in range(len(moves)):
            print('-----------------')
            print('     Step {:0>2}'.format(i+1))
            print('-----------------')
            for j in moves[i]:
                print(' '.join([str(x) for x in j]))

# 逆数对个数计算
def inver(stat):
    stat1 = []
    for i in stat:
        stat1 += i
    count = 0
    for i in range(len(stat1)):
        if stat1[i] != 0:
            for j in range(i):
                if stat1[j]>stat1[i]:
                    count += 1
    return count


# 八数码问题有解的条件
# stat逆数对 奇偶性 ＝ target逆数对 奇偶性

def judge(stat, target):
    numInver1 = inver(stat)
    numInver2 = inver(target)
    if numInver1%2 == numInver2%2:
        return True
    return False

# 判断状态是否在状态集合gList中，返回index
def isIn(g, gList):
    for i in range(len(gList)):
        if g.stat == gList[i].stat:
            return i
    return -1


def Astar(startStat):
    opened = []
    closed = []
    # 初始化
    g = grid(startStat)
    # 判断是否有解
    if judge(startStat, g.target) != True:
        print('该八数码无解，请重新输入')
        exit(1)
    opened.append(g) # open表中记录所有已生成而未展开的状态

    while(opened):
        print(len(opened))
        opened.sort(key=lambda g:g.f)
        # 按f排序
        
        minFStat=opened[0]
        # 检查是否为目的状态
        if minFStat.stat == g.target:
            minFStat.getMoves()
            break
            
        # 若没找到解
        expandGrid = minFStat.expand() # 拓展
        opened.pop(0) # open[0]已展开
        closed.append(minFStat) # close中存放已扩展过的状态
        for gridOne in expandGrid:
            temG = grid(gridOne)
            temG.pre = minFStat
            temG.update()

            gInOpen = isIn(temG, opened)
            gInClosed = isIn(temG, closed)

            if gInOpen > -1 and temG.g < opened[gInOpen].g:
                opened[gInOpen] = temG
                
            if gInClosed > -1 and temG.g < closed[gInClosed].g:
                # closed.remove(temG) # 将子状态从closed表移至opened表
                closed[gInClosed] = temG
                opened.append(temG)
            # 既不在opened表也不在closed表
            if gInOpen == -1 and gInClosed == -1:
                global newCount
                newCount += 1
                opened.append(temG)


            

# stat=[[2, 8, 3], [1, 6 ,4], [7, 0, 5]]
stat=[[5, 1, 2, 4], [9, 6 ,3, 8], [13, 15, 10, 11], [14, 0, 7, 12]]
startTime = time.time()
Astar(stat)
endTime = time.time()
print('time:', endTime-startTime)
print('expandCount: ', expandCount)
print('newCount: ', newCount)