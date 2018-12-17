from xml.etree import ElementTree as ET

token = "start"    # global variable


def Error():            # al function dy al mfrood tw2f al brnamg w ttl3 error message
    print("Error")


def read-stmt():
    match("read")
    match("identifier")

def if-stmt():
    match("if")
    exp()
    match("then")
    stmt_seq()
    if (token == "end"):
        match("end")

    else if (token == "else"):
        match("else")
        stmt_seq()
        match("end")


def term():
    if (token == "term"):
        term()
        mulop()
        factor()

    else if (token == "factor"):
        factor()


def mulop():
    if (token == "*"):
        match("*")

    else if (token == "/"):
        match("/")


def factor():
    if (token == "("):
        match("(")
        exp()
        match(")")

    else if (token == "number")
    match("number")

    else if (token == "identifier")


def program():
    stmt_seq()

def stmt_seq():
    statment()

#    while(token == "if"  or token == "repeat" or token == "assign" )        # lsa hn3dlha


def statment():
    if(token == "if"):
        IF()
    elif (token == "repeat"):
        repeat()
    elif (token == "assign"):
        assgin()
    elif (token == "read"):
        read()
    elif (token == "write"):
        write()
    else:
        Error()

def read():
    print("read")
def IF():
    print("if")

def exp():
    simple_exp()
    while(token == "<" or token == ">" or token == "="):
        comparison_exp()
        simple_exp()

def comparison_exp():
    if (token == "<"):
        match("<")
    elif (token == ">"):
        match(">")
    elif (token == "="):
        match("=")
    else:
        Error()

def assign_stmt():
    is_identifier()
    match(":=")
    exp()


def simple_exp():
    term()
    while(token == "+" or token == "-"):
        addop()
        term()

def addop():
    if(token == "+"):
        match("+")
    elif (token == "-"):
        match("-")



def repeat():
    match("repeat")
    stmt_seq()
    match("until")
    exp()


def write():
    print("write")


def match(t):
    global token
    if (token == t):
        token = next_token()
    else:
        Error()



def next_token():        # this function is used to get the next token in the input to parser file
    t = f.readline()
    index = t.find(",")
    return t[:index]









if __name__ == '__main__':


    f = open("E:\input to parser.txt", "r")
    token = next_token()
    print(token)
    program()







