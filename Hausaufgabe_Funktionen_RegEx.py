import re
import os
import glob


os.chdir(r"D:\Dokumente\Uni\Python\Hausaufgaben")

def organize(titles):
    org_titles = re.sub("[^A-Za-z ]", "-", str(titles))
    return org_titles

def text_spl(file):
    content = file.read()
    poems = content.split('##')[1:]
    return poems

def checkfordir(name):
    target = os.path.join(os.getcwd(), name)

os.makedirs("split", exist_ok=True)


dirlist = glob.glob("*.txt")

for sourcef in dirlist:
    name = sourcef.split(".")[0]
    target = checkfordir(name)
    with open (sourcef, "r", encoding="utf-8") as new_file:
        poems = text_spl(new_file)
        
        for headings in poems:
            titles_p = headings.split("\n")[0]
            titles = organize(titles_p)
            
            filename = "{0}_{1}".format(name, titles)
            
            target = (r"D:\Dokumente\Uni\Python\Hausaufgaben\splitDocs")
            
            filepath = os.path.join(target + "\\" + filename)
            filepath = re.sub("\.", "", filepath).strip("[],()*")
            
            with open (filepath + ".txt", "w", encoding = "utf-8") as new_file:
                new_file.write(headings)
