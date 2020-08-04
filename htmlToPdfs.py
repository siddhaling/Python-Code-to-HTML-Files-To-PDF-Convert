#import pdfkit required for converting a file to PDF file
import pdfkit
import glob
import os

#change the directory to current directory
os.chdir('I:\\BigDataProjects\\My Github\\10.pdfFromHtml\\')

#configure the path where wkhtmltopdf is installed
#If anaconda is used then it is present in anaconda folder then \wkhtmltopdf
#the file pathInfo.txt contains the path of wkhtmltopdf.exe
path_wkhtmltopdf = open('pathInfo.txt').read()
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

#Folder containig html files
pathReports='htmlFiles'
#Folder where pdf files are stored
pathWritePDF='pdfFromHtml'

#Read all the file with html extension
htmlFiles=glob.glob(pathReports+'/*.html')

#Convert html to pdf and save them in the folder pathWritePDF
for htmlF in htmlFiles:
    name=htmlF.split('\\')[-1].split('.html')[0]
    print(name)
    pdfkit.from_file(htmlF, pathWritePDF+'/'+name+'.pdf', configuration=config)
   
