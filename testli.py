def Realtd():
    with open("/home/edward/projects/python/test.txt","r")as files:
        content=files.readlines()
        return content
def writeltd(x):
    with open("/home/edward/projects/python/test.txt","r")as files:
        f=files.readlines()
        
    with open("/home/edward/projects/python/test.txt","w")as files:
        f.append(x)
        files.writelines(f)
        
    return
def edit_txt(x,a):
    with open("/home/edward/projects/python/test.txt","r")as files:
        f=files.readlines()
        
    with open("/home/edward/projects/python/test.txt","w")as files:
        
        try:
            
            
            asd=f.index(x[0])
            f[asd]=a
            files.writelines(f)
        except ValueError:
            print(ValueError)
            files.writelines(f)
    return 

        
