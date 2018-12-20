import re
from tkinter import *
from parser import *
path='/media/megawer/My Data/python/parser'
def tsplit(string, delimiters):
    """Behaves str.split but supports multiple delimiters."""

    delimiters = tuple(delimiters)
    stack = [string, ]

    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i + j, _substring)
    return stack
def scan():
    l = Label(font=("Courier", 12),
              text='''Thank You :D \n Scan is done correctly \n and the ouptut file in "E:\\" directory \n and its name is "output.txt"''', fg='white',
              bg='grey', heigh=0, width=0).place(x=360, y=180)
    paragraph = str(input.get("1.0", "end-1c"))
    list_signs_one_char = [',','+','-','*','/','=','&','|','{','}','(',')','<','>',';',':']
    #list_signs_two_char = [':=','==','&&','||',':>']
    pos1=0
    #f1=open("E:\Mohamed\input.txt",'r')

    lines_as_string = paragraph
    lines_as_string = lines_as_string.replace(":=", "?")  # Adding spaces
    for i in list_signs_one_char:
        if i in lines_as_string:
             #pos1=lines_as_string.find(i)
             #if (lines_as_string[pos1 + 1] not in list_signs_one_char and lines_as_string[pos1 - 1] not in list_signs_one_char):
            lines_as_string =lines_as_string.replace(i," " + i + " ")        # Adding spaces

    lines_as_string = lines_as_string.replace( "?" , " := ")

    '''
    for j in list_signs_two_char:
        if j in list_signs_two_char:
            lines_as_string = lines_as_string.replace(j, " " + j + " ")
    '''
    #f1.close()
    paragraph =" "
    #f1=open("E:\Mohamed\input.txt",'w')       # opening file and close it used for delete file
    #f1.close()
    #f1=open("E:\Mohamed\input.txt",'w')
    #f1.write(lines_as_string)
    #f1.close()
    paragraph=lines_as_string
    #print(paragraph)
    # Till here i added spaces before and after every sign

    #f=open("E:\Mohamed\input.txt",'r')
    lines_as_string = paragraph
    #f.seek(0,0)
    lines_as_list = []
    lines_as_list =paragraph.split()
    Numbers = re.findall(r'\d{1,10000}', lines_as_string)
    identifier = re.findall(r'[A-Za-z][A-Za-z0-9_]*', lines_as_string)

    fw =open(path+"/input to parser.txt",'w')
    flag = True
    for i in lines_as_list:
        #print(i,type(i))
        thisline = tsplit(i, (' ', '\n',))

        for j in thisline:
            if j == '{':                          # to ignore comments
                flag = False
            if j == '}':
                flag = True

            if flag == True:
                if j in Numbers:
                    fw.write(j + "," + "Number" +'\n')
                elif (
                        j == "if" or j == "else" or j == "repeat" or j == "read" or j == "write" or j == "then" or j == "until" or j=='end'):  # this if for reserved words
                    fw.write(j + ","  + "reseved word" +'\n')
                elif (
                        j == "<" or j == ">" or j == "=" or j == "<=" or j == ">=" or j == "==" or j == "+" or j == "-" or j == "*" or j == "/" or j == ","):
                    fw.write(j + "," + "special char" +'\n')
                elif (j == ":="):
                    fw.write(j + ","  + "assign" +'\n')
                elif (j == "(") or (j == "["):
                    fw.write(j + ","  + "special char" +'\n')
                elif (j == ")") or (j == "]"):
                    fw.write(j + "," + "special char" +'\n')
                elif (j == ";"):
                    fw.write(j + "," + "special char" +'\n')
                elif j in identifier:
                    fw.write(j + ","  + "identifier" +'\n')


    fw.close()

window =Tk()
window.geometry('800x500')
window.title('Scanner')
scan_button=Button(text="scan",width=10,heigh=3,fg='Blue',bd=7,command=scan).place(x=40,y=400)
parse_button=Button(text="parse",width=10,heigh=3,fg='red',bd=7,command=main).place(x=220,y=400)

input= Text(window,width=40)
input.place(x=5,y=5)
window.mainloop()
