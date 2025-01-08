import os

if not os.path.exists('test.txt'):
    with open("test.txt","w") as file:
        pass


def Realtd():
    with open("/home/edward/projects/python/test.txt","r")as files:
        content=files.readlines()
        return content
def writeltd(x):
    with open("/home/edward/projects/python/test.txt","r")as files:
        f=files.readlines()
           
    with open("/home/edward/projects/python/test.txt","w")as files:
        try:
        
            f.append(x)
            files.writelines(f)
        except:
            
            files.writelines    
    return
def edit_txt(x,a):
    with open("/home/edward/projects/python/test.txt","r")as files:
        f=files.readlines()
        
    with open("/home/edward/projects/python/test.txt","w")as files:
        
        try:
            
            
            asd=f.index(x[0]+"\n")
            f[asd]=a
            files.writelines(f)
        except:
           
            files.writelines(f)
       
    return
def complete(u):
    with open("/home/edward/projects/python/test.txt","r")as files:
        f=files.readlines()
        
    with open("/home/edward/projects/python/test.txt","w")as files:
        try:                  
            f.remove(u)
        finally:
            files.writelines(f)
    

        
