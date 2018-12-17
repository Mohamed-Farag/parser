from xml.etree import ElementTree as ET

# important notes
  #1) make txt file in E directory naming it (input to parser)




token1 = "start"    # dah global variable
token2 = "start"    # dah global variable


def Error():            # al function dy al mfrood tw2f al brnamg w ttl3 error message
    print("Syntax Error")


def read_stmt():
    match("read")       # token1
    match("identifier") # token2

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


def term():
    if (token1 == "term"):
        term()
        mulop()
        factor()

    elif (token1 == "factor"):
        factor()


def mulop():
    if (token1 == "*"):
        match("*")

    elif (token1 == "/"):
        match("/")


def factor():
    global token1
    if (token1 == "("):
        match("(")
        exp()
        match(")")

    elif (token2 == "Number"):
        match("Number")

    elif (token2 == "identifier"):
        match("identifier")


def program():
    stmt_seq()

def stmt_seq():
    statment()

    while(token2 == "identifier\n" or token1 == "if"  or token1 == "repeat" or token1 == ":=" or token1 == "read" or token1 == "write"):        # lsa hn3dlha
        statment()


def statment():
    if(token1 == "if"):
        IF()
    elif (token1 == "repeat"):
        repeat()
    elif (token1 == "read"):
        read()
    elif (token1 == "write"):
        write()
    elif (token2 == "identifier\n"):
        match("identifier")
    elif (token1 == ":="):
        match(":=")
    else:
        Error()

def read():
    print("read")
def IF():
    print("if")

def exp():
    simple_exp()
    while(token1 == "<" or token1 == ">" or token1 == "="):
        comparison_exp()
        simple_exp()

def comparison_exp():
    if (token1 == "<"):
        match("<")
    elif (token1 == ">"):
        match(">")
    elif (token1 == "="):
        match("=")
    else:
        Error()

def assign_stmt():
    match("identifier")
    match(":=")
    exp()


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



def repeat():
    match("repeat")
    stmt_seq()
    match("until")
    exp()


def write():
    print("write")


def match(t):
    global token1
    global token2
    if (token1 == t or token2 == t+"\n"):
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
    return t[:index],t[index+1:]








if __name__ == '__main__':



    f = open("E:\input to parser.txt", "r")
    token1,token2 = next_token()
    #print(token1,token2)
    program()







