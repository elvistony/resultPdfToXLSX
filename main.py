
import os
import re
from os import path
from datapreprocess import *
from tabulatetext import *

print("\t\t(PYTHON 3) PDF TO XLSX CONVERTER\n")
try:
        import pandas
        import xlsxwriter
        import pdfminer
        import openpyxl
        
        
        filename = input("Source File Name[PDF]: ")
	#check workspace directory is present
        print("\t\t\nCREATING WORKSPACE\n")
        if os.path.isdir("workspace/")!=True:
                CreateWorkspace()
                print("Workspace : Created")


        #converting PDF to text as data1.txt
        print("\t\tPDF TO TEXT - 2 Engines Available\n1.PDFMiner(Python Based)\n2.PDFtoText(Linux Based)")
        if(int(input("Specify option number:"))==2):
            Convert2Text_Engine2(filename)
        else:
            Convert2Text_Engine1(filename)
        
        print("Conversion : Success")
        
        



        #Split Text data to branch specific files
        #[branches] - holds list of detected Branches
        print("\t\t\nCREATING WORKSPACE\n")
        branches = GetTextData("data.txt")

        print("\t\t\nFINISHING UP\n")
        destination = input("Destination File Name[XLSX]: ")
        #Convert Text to [branch].xlsx
        tabulate(branches,destination)


        #Ask for Cleanup
        print("\n\t\tOPTIONAL")
        choice = input("CleanUp : Clear Cached Files? y/n : ")
        if choice in "yesYes":
                CleanUp()

except ImportError:
	print("Please Make sure you have the Dependencies\n"+"""
	1.Pandas
	2.XlsxWriter
	3.Openpyxl
	4.Numpy""")
	print('Attempt to instal/update dependencies? y/n')
	if(input()=='y'):
                print("Installation/Update Started")
                os.system('pip3 install pdfminer pandas xlsxwriter openpyxl')
                print("Installation/Update Completed\n Rerun the Software to see changes")
                
print("\t\tCOMPLETE\n")

