from xml.etree import ElementTree as ET

# important notes
  #1) make txt file in E directory naming it (input to parser)

token1 = "start"    # dah global variable
token2 = "start"    # dah global variable


def program():
    stmt_seq()

def stmt_seq():
    statment()

    while(token1 == ";"):       
        match(";")
        statment()


def statment():
    if(token1 == "if"):
        if_stmt()
    elif (token1 == "repeat"):
        repeat()
    elif (token1 == "read"):
        read_stmt()
    elif (token1 == "write"):
        write()
    else:
        assign_stmt()


def if_stmt():
    global token1
    match("if")
    exp()
    match("then")
    stmt_seq()
    if (token1 == "end"):
        match("end")

    elif (token1 == "else"):
        match("else")
        stmt_seq()
        match("end")


def repeat():
    match("repeat")
    stmt_seq()
    match("until")
    exp()


def assign_stmt():
    match("identifier")
    match(":=")
    exp()



def read_stmt():
    match("read")
    match("identifier")


def write():
    match("write")
    exp()

def exp():
    simple_exp()
    while(token1 == "<" or token1 == ">" or token1 == "="):
        comparison_op()
        simple_exp()


def comparison_op():
    if (token1 == "<"):
        match("<")
    elif (token1 == ">"):
        match(">")
    elif (token1 == "="):
        match("=")
    else:
        Error()


def simple_exp():
    term()
    while(token1 == "+" or token1 == "-"):
        addop()
        term()

def addop():
    if(token1 == "+"):
        match("+")
    elif (token1 == "-"):
        match("-")


def term():
    factor()
    while (token1 == "*" or token1 == "/"):
        mulop()
        factor()


def mulop():
    if (token1 == "*"):
        match("*")

    elif (token1 == "/"):
        match("/")


def factor():
    global token1
    global token2
    if (token1 == "("):
        match("(")
        exp()
        match(")")

    elif (token2 == "Number"):
        match("Number")

    elif (token2 == "identifier"):
        match("identifier")







def match(t):
    global token1
    global token2
    if (token1 == t or token2 == t):
        token1,token2 = next_token()
    else:
        Error()


def is_number(t):
    try:
        val = int(t)
    except ValueError:
        Error()



def next_token():        # this function is used to get the next token in the input to parser file
    t = f.readline()
    index = t.find(",")
    t1 = t[:index]
    t2 = t[index+1:].strip()
    return t1,t2


def Error():  # al function dy al mfrood tw2f al brnamg w ttl3 error message
    print("Syntax Error")


if __name__ == '__main__':

    f = open("E:\input to parser.txt", "r")
    token1,token2 = next_token()
    #print(token1,token2)
    program()
