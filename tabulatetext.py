import pandas as pd
import re
from os import path
a=[]

def tabulate(a,destination):
    writer = pd.ExcelWriter(destination + '.xlsx', engine='xlsxwriter')
    for x in a:
        cur_student=""
        stud = {}
        breaknext=0
        frame = {}
        df = pd.DataFrame(columns=["Name"])
        print("Processing . . ."+x)
        with open("workspace/"+x+".txt","r") as g:
            line = g.readline()
            while True:
                ls = line.split()
                #Detect RegisterNumbers with pattern AAA12AA123
                reg = re.findall("\w+[1]\d\w\w\d+", line)
                if reg: #found new student
                    reg =reg[0]
                    cur_student=reg

                    #Flush Buffer to FRAME upon new Student
                    df = df.append(frame,ignore_index=True)

                    #set new Student Buffer
                    frame={}
                    frame["Name"]=reg
                # Detect Subjects with Patterns AB123
                subs =re.findall(r"\b\w\w\d\d\d", line)
                for word in subs:
                    start = line.find(word + "(")
                    end = line.find(")", start)
                    frame[word] = line[start + len(word) + 1:end]
                line = g.readline()
                if line=="":
                    #Flush Last Student to Frame
                    df = df.append(frame, ignore_index=True)
                    break


            df=df.fillna("")
            tinytitle=x.split()[0]
        df.to_excel(writer, sheet_name=tinytitle, index=False)
    writer.save()
    return df

    #SUCCESS CHECK
    if path.exists(destination+".xlsx"):
        print("Tabulation : Success")
    else:
        print("Tabulation : Failed")

#DEBUG
#tabulate(["COMPUTER SCIENCE & ENGINEERING[Full Time]"],"abc")

