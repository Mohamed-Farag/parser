from xml.etree import ElementTree as ET

# important notes
  #1) make txt file in E directory naming it (input to parser)




token = "start"    # dah global variable


def Error():            # al function dy al mfrood tw2f al brnamg w ttl3 error message
    print("Error")


def read_stmt():
    match("read")
    match("identifier")

def if_stmt():
    global token
    match("if")
    exp()
    match("then")
    stmt_seq()
    if (token == "end"):
        match("end")

    elif (token == "else"):
        match("else")
        stmt_seq()
        match("end")


def term():
    if (token == "term"):
        term()
        mulop()
        factor()

    elif (token == "factor"):
        factor()


def mulop():
    if (token == "*"):
        match("*")

    elif (token == "/"):
        match("/")


def factor():
    global token
    if (token == "("):
        match("(")
        exp()
        match(")")

    elif (token == "number"):
        match("number")



    elif (token == "identifier"):
        match("identifier")


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







