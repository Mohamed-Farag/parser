import pygraphviz as pgv



class Tree:
    G=pgv.AGraph()
    nodeId=0
    def __init__(self):
        self.G=pgv.AGraph(strict=False,directed=False)
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
    def connectHorizotal(self,firstNode,secondNode):
        self.G.subgraph(nbunch=[firstNode,secondNode],rank='same')
        self.Add_edge(firstNode,secondNode)
    def newDuplicateNode(self):
        self.nodeId+=1
    def getGraph(self):
        return self.G
    def Draw(self,path):
        self.G.layout(prog='dot')
        self.G.draw(path+'/ParseTree.png')


########## test ##################################
'''
path='/media/megawer/My Data/python/parser'
tree=Tree()
xid=tree.Add_node('assign x','rec')
yid=tree.Add_node('assign y','rec')
zid=tree.Add_node('assign z','rec')
nodeaid=tree.Add_node('assign a','rec')

tree.Add_edge(yid,zid)
tree.Add_edge(zid,nodeaid)
                                    #node1stIfid=tree.Add_node('if',0,1)
node2ndIfid=tree.Add_node('if','')
                                    #node2Wid=tree.Add_node('write',1,1)
                                    #node3Wid=tree.Add_node('write',1,1)
nodeWid=tree.Add_node('write','')
                                    #tree.Add_node('read b',1,0)
                                    #tree.Add_node('repeat',1,0)
tree.Add_edge(nodeWid,xid)
opeqid=tree.Add_node('op =','')
nodeW2id=tree.Add_node('write','rec')
node2id=tree.Add_node('2','')
node3id=tree.Add_node('3','')
node5id=tree.Add_node('5','')
plusopid=tree.Add_node('op +','')
plus2opid=tree.Add_node('op +','')
plus3opid=tree.Add_node('op +','')
opminid=tree.Add_node('op -','')
nodeZid=tree.Add_node('z','')
nodexid=tree.Add_node('x','')
nodeyid=tree.Add_node('y','')
node2xid=tree.Add_node('x','')
node2yid=tree.Add_node('y','')
nodebid=tree.Add_node('b','')
node2bid=tree.Add_node('b','')
neq1id=tree.Add_node('-1','')
aid=tree.Add_node('a','')
tree.Add_edge(xid,node2id)
#tree.Add_edge('assign x','assign y')
tree.Add_edge(yid,node3id)
#tree.Add_edge('assign y','assign z')
tree.Add_edge(zid,node5id)
#tree.Add_edge('assign z','assign a')
tree.Add_edge(nodeaid,plusopid)
tree.Add_edge(plusopid,nodeZid)
tree.Add_edge(plusopid,plus2opid)
tree.Add_edge(plus2opid,nodexid)
tree.Add_edge(plus2opid,nodeyid)
tree.Add_edge(nodeaid,node2ndIfid)
tree.Add_edge(node2ndIfid,opeqid)
tree.Add_edge(node2ndIfid,nodeW2id)
tree.Add_edge(node2ndIfid,nodeWid)
tree.Add_edge(opeqid,nodebid)
tree.Add_edge(opeqid,neq1id)
tree.Add_edge(nodeW2id,aid)
tree.Add_edge(nodeWid,plus3opid)
tree.Add_edge(plus3opid,node2bid)
tree.Add_edge(plus3opid,opminid)
tree.Add_edge(opminid,node2xid)
tree.Add_edge(opminid,node2yid)
g=tree.getGraph()
g1=g.subgraph(nbunch=[zid,yid,nodeaid],rank='same')
g2=g.subgraph(nbunch=[xid,nodeWid],rank='same')
tree.Draw(path)
'''
####### test ################
