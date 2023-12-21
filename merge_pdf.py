from pathlib import Path
from bs4 import BeautifulSoup
import sys
import requests
from PyPDF2 import  PdfReader, PdfWriter


links = []

def getLinks(url):

    r = requests.get(url)
    contents = r.content

    soup = BeautifulSoup(contents)
    for link in soup.findAll('a'):
        pdf =  link['href'].replace("..", "")
        if not pdf.endswith('.pdf'):
            continue
        links.append("https://ocw.mit.edu"+  pdf)        

if __name__ == "__main__":
    url = "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/resources/lecture-notes/"


    getLinks(url)

    for link in links:
        path = "C:\\Users\\User\\OneDrive\\Desktop\\MIT\\"


        name = link.split('.')[-2].split('_Ses')[-1]
        name = name[:-1] + chr( ord(name[-1]) - 48)

        path += name

        print(link)
        if len(name) > 5:
            continue
        r = requests.get(link)


        print(name)

        with open(path +  ".pdf" , 'wb') as f:
            f.write(r.content)

    files = []
    data = Path("C:\\Users\\User\\OneDrive\\Desktop\\MIT\\")

    output = PdfWriter()

    for file in data.glob("*.pdf"):
        files.append(file)

    files.sort(key=lambda x: int(str(x).split("\\")[-1].split(".")[0]))

    for file in files:
        print(file)
        f = PdfReader(file, 'rb')
        for i in range(len(f.pages) - 1):
            p = f.pages[i]
            output.add_page(p)

    output.write("script.pdf")
            


    sys.exit()