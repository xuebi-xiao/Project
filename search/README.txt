執行環境:Visual Studio Code
執行版本:Python 3.10.1

設計概念:

DFS:運用Stack的FILO的概念完成
程式碼:
	 explored = set()
    Stack  = util.Stack()#初始化Stack
    List=[] #初始化List
    StartState = problem.getStartState()#設定起始座標位置
    
    StartNode = (StartState, List)#定義起始點用(點座標,行進方向集合)此資料結構儲存
    Stack.push(StartNode)#將起始點放入Stack紀錄起來
    while not Stack.isEmpty():#判斷Stack是否為空
        currentstate,List = Stack.pop()#currentstate儲存pop出的座標，List儲存pop出的方向集合
        if not currentstate in explored:#搜尋過後就不用再回頭搜尋否則會無法往下尋找終點
            explored.add(currentstate)#紀錄未搜尋的座標
        else:
            continue#若當前座標已搜尋過跳過此次探索
        if problem.isGoalState(currentstate):#判斷當前座標是否為目標座標
            print("抵達終點!!")
            print("行進方向集合:",List)
            return List#回傳方向集合
        else:
            successor = problem.getSuccessors(currentstate)#找到當前座標的所有後繼者
            for item in successor:                         
                Stack.push((item[0],List+[item[1]]))#將後繼者座標及方向集合放入Stack中

BFS:運用Queue的FIFO的概念完成
程式碼:
	 explored = set()
    Queue  = util.Queue()#初始化Queue
    List=[] #初始化List
    StartState = problem.getStartState()#設定起始座標位置
    
    StartNode = (StartState, List)#定義起始點用(點座標,行進方向集合)此資料結構儲存
    Queue.push(StartNode)#將起始點放入Queue紀錄起來
    while not Queue.isEmpty():#判斷Queue是否為空
        currentstate,List = Queue.pop()#currentstate儲存pop出的座標，List儲存pop出的方向集合
        if not currentstate in explored:#搜尋過後就不用再回頭搜尋否則會無法往下尋找終點
            explored.add(currentstate)#紀錄未搜尋的座標
        else:
            continue#若當前座標已搜尋過跳過此次探索
        if problem.isGoalState(currentstate):#判斷當前座標是否為目標座標
            print("抵達終點!!")
            print("行進方向集合:",List)
            return List#回傳方向集合
        else:
            successor = problem.getSuccessors(currentstate)#找到當前座標的所有後繼者
            for item in successor:                         
                Queue.push((item[0],List+[item[1]]))#將後繼者座標及方向集合放入Queue中



