'''
Author: Andy Shaw
Date:   10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

This agent is based off the Hill Climbing algorithm found on slide 5 of the Week04b-Optimization 
slides.

Note: Next choice is purely based on the heap's return algorithm.  In the case of a tie, it is not
going to be random.

param: boardsize integer board size
returns: state that is a solution
'''

import heapq
import array
import boardScore as b
import successor as s

def hillClimbingAgent(boardsize, silent=False):
    #create initial state at random if none is presented (useful for testing certain configurations)
    import random
    initial = array.array('i')
    for i in range(boardsize):
        initial.append(random.randint(0, boardsize-1))

    currNode = (b.boardScore(initial), s.copyArr(initial))
    i = 0
    while 1:
        childrenHeap = list()
        
        #find successors
        children = s.successor(currNode[1])
        
        #rate each resulting board and add to heap
        for child in children:
            childrenHeap.append((b.boardScore(child), child))
        
        #sort and pull out next best choice
        nextNode = heapq.heappop(childrenHeap)
        
        #print status
        if not silent: print 'Iteration:{0}\tState:<{1}>\tBest Child Score:{2}'.format(
                        i, arrToString(currNode[1]), nextNode[0])
        
        #check if solution
        if b.boardScore(nextNode[1]) == 0:
            return nextNode[1]
            
        #if currNode is less than, then it is the best solution on the board, heap will assure that
        if currNode[0] >= nextNode[0]:
            return currNode[1]
            
        #try again on the nextNode
        currNode = nextNode
        i+=1
        
def arrToString(arr):
    x = arr.tolist()
    s = ''
    for item in x:
        s += str(item) + ','
    return s[:-1]
        