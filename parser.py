from Tree import *

#temp = parseTree.Add_node("const" + "\n" + "  (" + token1 + ")", "cir")
#parseTree.Add_edge(parent, left_child)   # connecting parent to left_child
#parseTree.Add_edge(parent, right_child)  # connecting parent to right_child
# important notes
  #1) make txt file in E directory naming it (input to parser)

token1 = ''    # dah global variable
token2 = ''    # dah global variable
parseTree=Tree()
path='/media/megawer/My Data/python/parser'

def program():
    stmt_seq()

def stmt_seq():
    node1 = statment()        # first if{   # second if{}   NOW , child is the second if
    horizontal_node1 = node1
    #print(token1)
    while(token1 == ';'):
        match(';')
        horizontal_node2 = statment()
        parseTree.connectHorizotal(horizontal_node1, horizontal_node2)   # Horizontal line
        horizontal_node1 = horizontal_node2
    return node1
    # connect statements of the same level

def statment():
    child = 0
    global token1
    #print(token1)
    if(token1 == "if"):
        child = if_stmt()
    elif (token1 == "repeat"):
        child = repeat()
    elif (token1 == 'read'):
    #    print(token1+"r")
        child = read_stmt()
    elif (token1 == "write"):
        child = write()
    else:
        #print(token1)
        child = assign_stmt()

    return child

def if_stmt():
    global token1
    parent_if = parseTree.Add_node(token1, "rec")
    match("if")


    first_child =exp()
    match("then")
    second_child =stmt_seq()

    parseTree.Add_edge(parent_if, first_child)   # connecting parent to first_child
    parseTree.Add_edge(parent_if, second_child)  # connecting parent to second1_child

    if (token1 == "end"):
        match("end")

    elif (token1 == "else"):
        match("else")
        third_child = stmt_seq()
        match("end")
        parseTree.Add_edge(parent_if, third_child)  # connecting parent to left_child

    return parent_if

def repeat():
    token_temp = token1
    match("repeat")
    parent_repeat = parseTree.Add_node(token_temp, "rec")
    left_child = stmt_seq()
    match("until")
    right_child = exp()

    parseTree.Add_edge(parent_repeat, left_child)   # connecting parent to left_child
    parseTree.Add_edge(parent_repeat, right_child)  # connecting parent to right_child

    return parent_repeat

def assign_stmt():
    global token1
#need to revise this function
    t_assign = token1
    match("identifier")

    match(":=")
    child = exp()

    parent = parseTree.Add_node("assign" + "\n" + " (" + t_assign + ")", "rec")
    parseTree.Add_edge(parent, child)  # connecting parent to left_child

    return parent

def read_stmt():
    token_temp = token1
    match('read')
    parent_read = parseTree.Add_node(token_temp + "\n" +"("+token1+")", 'rec')
    match('identifier')
    #parseTree.Add_edge(parent_read, parent_idetifier)
    return parent_read


def write():
    token_temp = token1
    match("write")
    parent_write = parseTree.Add_node(token_temp, "rec")
    child = exp()
    parseTree.Add_edge(parent_write, child)  # connecting parent to left_child
    return parent_write
def exp():
    # here is a logic error this function dosen't handle the case assign fact := 1;
    #temp = Tree()
    #new_temp = Tree()
    left_child = simple_exp()   # x
    parent=0
    flag=0
    while(token1 == "<" or token1 == ">" or token1 == "="):
        flag=1
        parent = comparison_op()   # =
        right_child = simple_exp()

        parseTree.Add_edge(parent, left_child)          # connecting parent to left_child
        parseTree.Add_edge(parent, right_child)         # connecting parent to right_child
        left_child = parent

    if(flag==0):
        return left_child
    return parent


def comparison_op():
    # here is a logic error this function dosen't handle the case assign fact := 1;
    token1_temp=token1
    if (token1 == "<"):
        match("<")
    elif (token1 == ">"):
        match(">")
    elif (token1 == "="):
        match("=")
    else:
        Error()

    temp = parseTree.Add_node("op" + "\n" + " (" + token1_temp + ")", "cir")     # parent
    #parseTree.Add_edge(temp, child_ID)                                       # connecting parent to child
    return temp

def simple_exp():
    #temp = Tree()
    #new_temp = Tree()
    left_child = term()      # 8 # -
    parent=0
    flag=0
    while(token1 == "+" or token1 == "-"):
        flag=1
        parent = addop()        # -   # +
        right_child = term()    # 6   # *
        parseTree.Add_edge(parent, left_child)          # connecting parent to left_child
        parseTree.Add_edge(parent, right_child)         # connecting parent to right_child
        left_child = parent
    if(flag==0):
        return left_child
    return parent


def addop():
    token_temp = token1
    if(token1 == "+"):
        temp = match("+")
    elif (token1 == "-"):
        temp = match("-")

    temp=parseTree.Add_node("op" + "\n" + " (" + token_temp + ")" , "cir")

    return temp

def term():
    #temp = Tree()
    #new_temp = Tree()
    left_child = factor()      # 11
    flag=0
    parent=0
    while (token1 == "*" or token1 == "/"):
        flag=1
        parent = mulop()          # *
        right_child = factor()    # 5
        parseTree.Add_edge(parent, left_child)   # connecting parent to left_child
        parseTree.Add_edge(parent, right_child)  # connecting parent to right_child
        left_child = parent
    if(flag==0):
        return left_child
    return parent

def mulop():
    token1_temp=token1
    if (token1 == "*"):
        match("*")
    elif (token1 == "/"):
        match("/")

    temp = parseTree.Add_node("op" + "\n" + " (" + token1_temp + ")", "cir")

    return temp

def factor():
    #temp = Tree()
    global token1
    global token2
    temp=0
    if (token1 == "("):
        match("(")
        temp = exp()
        match(")")

    elif (token2 == "Number"):
         temp = parseTree.Add_node("const" + "\n" + " (" + token1 + ")" , "cir")
         match("Number")


    elif (token2 == "identifier"):
        temp = parseTree.Add_node("id" + "\n" + " (" + token1 + ")", "cir")
        match("identifier")


    return temp




def match(t):
    global token1
    global token2
    #print(token1)
    #print(token2)
    #temp = Tree()
    if (token1 == t or token2 == t) :
        print('ok  '+token1)
        token1,token2 = next_token()

    else:
        Error()
    #return temp

def is_number(t):
    try:
        val = int(t)
    except ValueError:
        Error()



def next_token():        # this function is used to get the next token in the input to parser file
    t = f.readline()
    index = t.find(',')
    t1 = t[:index]
    t2 = t[index+1:].strip()
    return t1,t2


def Error():  # al function dy al mfrood tw2f al brnamg w ttl3 error message
    print("Syntax Error")


if __name__ == '__main__':

    f = open(path+"/input to parser.txt", "r")
    token1,token2 = next_token()
    #print(token1,token2)
    program()

    parseTree.Draw(path)
