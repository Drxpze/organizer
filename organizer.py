import os 
import shutil

fromdir = "C:/Users/Usuario/Downloads/"
todir = "C:/Users/Usuario/Pictures/"

listoffiles = os.listdir(fromdir)
print(listoffiles)

for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    if extension in [ '.txt', '.doc', '.docx', '.pdf ' ]:
        print(extension)
        path1 = fromdir + filename
        path2 = todir + "downloads"
        path3 = todir + "downloads/" + filename
        
        if os.path.exists(path2):
            print("movendo",filename) 
            shutil.move(path1,path3)
        else:
            print("criando pasta diretorio")
            os.makedirs(path2)
            print("movendo",filename) 
            shutil.move(path1,path3)
            
        
 