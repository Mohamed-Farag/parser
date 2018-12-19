import pygraphviz as pgv



class Tree:
    G=pgv.AGraph()
    nodeId=0
    def __init__(self):
        self.G=pgv.AGraph(strict=False,directed=True)
        self.nodeId=0

        '''
        Add_node(node_name,CircleOrRec,IsDublicate)
        this how this function works ....
        this function create a node in the tree using the following parameters
        node_name -> node name like if,op,x,y etc..
        CircleOrRec -> pass 1 if you want that node to be drawn as rectancle anything else for Circle
        IsDublicate -> pass 1 if you need to create multiple nodes in the tree with the same node name ,the function will return then the id of that node ,so you can use it after to distinguish that node
        '''
    def Add_node(self,node_name,CircleOrRec):
        if(CircleOrRec=='rec'):#that means the node will be shown as a rectancle such as read or write statm.
            self.G.add_node(self.nodeId,label=node_name,shape='rectangle')
            self.newDuplicateNode()
            return self.nodeId-1
        else:
            self.G.add_node(self.nodeId,label=node_name,shape='circle')
            self.newDuplicateNode()
            return self.nodeId-1
    def Add_edge(self,first_node,Second_node):
        self.G.add_edge(first_node,Second_node)
    def newDuplicateNode(self):
        self.nodeId+=1
    def Draw(self,path):
        self.G.layout()
        self.G.draw(path+'/ParseTree.png')

'''
########## test ##################################
tree=Tree()
tree.Add_node('assign x',1,0)
tree.Add_node('assign y',1,0)
tree.Add_node('assign z',1,0)
tree.Add_node('assign a',1,0)
                                    #node1stIfid=tree.Add_node('if',0,1)
node2ndIfid=tree.Add_node('if',0,1)
                                    #node2Wid=tree.Add_node('write',1,1)
                                    #node3Wid=tree.Add_node('write',1,1)
nodeWid=tree.Add_node('write',1,1)
                                    #tree.Add_node('read b',1,0)
                                    #tree.Add_node('repeat',1,0)
tree.Add_node('op =',1,0)
tree.Add_node('write',1,0)
node2id=tree.Add_node('2',0,1)
node3id=tree.Add_node('3',0,1)
node5id=tree.Add_node('5',0,1)
plusopid=tree.Add_node('op +',0,1)
plus2opid=tree.Add_node('op +',0,1)
plus3opid=tree.Add_node('op +',0,1)
tree.Add_node('op -',0,0)
nodeZid=tree.Add_node('z',0,1)
nodexid=tree.Add_node('x',0,1)
nodeyid=tree.Add_node('y',0,1)
node2xid=tree.Add_node('x',0,1)
node2yid=tree.Add_node('y',0,1)
nodebid=tree.Add_node('b',0,1)
node2bid=tree.Add_node('b',0,1)
tree.Add_node('-1',0,0)
tree.Add_node('a',0,0)
tree.Add_edge('assign x',node2id)
tree.Add_edge('assign x','assign y')
tree.Add_edge('assign y',node3id)
tree.Add_edge('assign y','assign z')
tree.Add_edge('assign z',node5id)
tree.Add_edge('assign z','assign a')
tree.Add_edge('assign a',plusopid)
tree.Add_edge(plusopid,nodeZid)
tree.Add_edge(plusopid,plus2opid)
tree.Add_edge(plus2opid,nodexid)
tree.Add_edge(plus2opid,nodeyid)
tree.Add_edge('assign a',node2ndIfid)
tree.Add_edge(node2ndIfid,'op =')
tree.Add_edge(node2ndIfid,'write')
tree.Add_edge(node2ndIfid,nodeWid)
tree.Add_edge('op =',nodebid)
tree.Add_edge('op =','-1')
tree.Add_edge('write','a')
tree.Add_edge(nodeWid,plus3opid)
tree.Add_edge(plus3opid,node2bid)
tree.Add_edge(plus3opid,'op -')
tree.Add_edge('op -',node2xid)
tree.Add_edge('op -',node2yid)
tree.Draw()
####### test ################
'''
