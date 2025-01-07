import zipfile
import pathlib

def make_archive(filepath,destination,res):
    dest_path=pathlib.Path(destination,res+".zip")
    try:
        
    
        with zipfile.ZipFile(dest_path,'w') as archive:
            for file in filepath:
                file=pathlib.Path(file)
                archive.write(file,arcname=file.name) 
        return True
    except :
        return False