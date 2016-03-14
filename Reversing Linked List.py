#Reversing Linked List

Given a constant K and a singly linked list L, you are supposed to reverse the links of every K elements on L. 
For example, given L being 1→2→3→4→5→6, if K = 3, then you must output 3→2→1→6→5→4; if K = 4, you must output 4→3→2→1→5→6.

Input Specification:

Each input file contains one test case. For each case, the first line contains the address of the first node, 
a positive  N(<=100000) which is the total number of nodes, and a positive K(<=N) which is the length of the 
sublist to be reversed. The address of a node is a 5-digit nonnegative integer, and NULL is represented by -1.

Then NN lines follow, each describes a node in the format:
          Address Data Next
where Address is the position of the node, Data is an integer, and Next is the position of the next node.

Output Specification:

For each case, output the resulting ordered linked list. Each node occupies a line, and is printed in the same format as in the input.

Sample Input:
00100 6 4
00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218
Sample Output:

00000 4 33218
33218 3 12309
12309 2 00100
00100 1 99999
99999 5 68237
68237 6 -1


#python code maybe slow +.+
class node(object):                             #create a node class
    def __init__(self, address, data, Next):
        self.address = address
        self.data = data
        self.Next = Next
        
    def get_data(self):
        return self.data

    def get_address(self):
        return self.address

    def get_Next(self):
        return self.Next

    def set_Next(self, Next):
        self.Next = Next

def getNode():
    address, data, Next =  input().split(' ')
    address = str(address)
    data = int(data)
    Next = str(Next)
    return node(address, data, Next)
  
def getNodeList():
    header, nodeNum, reverseNum =  input().split(' ')
    header = str(header)
    nodeNum = int(nodeNum)
    reverseNum = int(reverseNum)
    nodeList = []
    for i in range(nodeNum):
        newNode = getNode()
        nodeList.append(newNode)
    orderedList = []
    ansList = []
    for ele in nodeList:
        if ele.get_address() == header:
            orderedList.append(ele)
    while orderedList[0].get_Next() != '-1':
        ansList.append(orderedList[0])
        nextaddress = orderedList.pop().get_Next()
        for ele in nodeList:
            if ele.get_address() == nextaddress:
                orderedList.append(ele)   
    ansList.append(orderedList[0])
    return (ansList, reverseNum)

def reverseLinkedList():
    ans = getNodeList()
    originList = ans[0]
    reverseNum = ans[1]
    reversedList = []
    length = len(originList)
    i = 0
    while i < length:
        if i + reverseNum - 1 < length:
            partList = originList[i:i+reverseNum]
            partList.reverse()
            reversedList += partList
            i += reverseNum
        else:
            partList = originList[i:]
            reversedList += partList
            break
    return reversedList

def adjustNextList():                           ## adjust the next attribute of the element in the list
    originList = reverseLinkedList()
    length = len(originList)
    if length > 1:
        for i in range(length-1):
            originList[i].set_Next(originList[i+1].get_address())
        originList[i+1].set_Next('-1')
    return originList
    
def mainProcedure():    
  b = adjustNextList()        
  for ele in b:
      print(ele.get_address(), ele.get_data(), ele.get_Next())

mainProcedure()
      
