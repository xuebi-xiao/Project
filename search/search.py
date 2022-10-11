# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from ast import For
from inspect import stack
from this import s
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    ################## My DFS code ######################
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
        ###################################################
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
     ################## My BFS code ######################
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
        ###################################################
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
