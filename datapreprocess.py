import os
import re
from os import path
import shutil

def Convert2Text_Engine1(filename):
    print("Using Text Engine 1(Default)")
    os.system("pdf2txt.py "+filename+" >> workspace/data.txt")

def Convert2Text_Engine2(filename):
    print("Using Text Engine 2(Beta)")
    os.system("pdftotext "+filename+" workspace/data.txt")

def CreateWorkspace():
    os.system("mkdir workspace")

def GetTextData(file):
    branches=[]
    with open("workspace/"+file,"r") as f:
        a = f.readline()
        saweng=0
        print("University: "+a)
        g=open("workspace/data.txt",'r')
        while a:

            #<OPTIONAL>
            if "Exam Centre" in a:
                print(' '.join(a.split()[2:]))
            #</OPTIONAL>

            if re.search("\d{2}/\d{2}/\d{4}",a):
                print("Data Preprocess : Caught Trailing Signature")
                break
            if ("[Full Time]" in a):
                g.close()
                a=a.strip()
                print("Detected:"+a)
                branches.append(a)
                g = open("workspace/"+a+".txt","w")
                saweng=1
            elif saweng==1:
                if ("(Grade)" in a):
                    saweng=2
            elif saweng==2:
                    if a!="\n":
                        g.write(a)
            else:
                pass

            a=f.readline()
        g.close()


        #SUCCESS CHECK
        if path.exists("workspace/data.txt"):
            print("Data Preprocess : Success")
        else:
            print("Data Preprocess : Failed")
        return branches



def CleanUp():
    shutil.rmtree("workspace")
    if not (path.exists("workspace/")):
        print("CleanUp :  Success")
    else:
        print("CleanUp : Failed")


#DEBUG
# Convert2Text("result.pdf")
#GetTextData("result2.txt")
