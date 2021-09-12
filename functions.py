def getuser():
    import getpass
    user = getpass.getuser().format('utf-8')
    
    return user
    
    
def scandir(user):
    import os
    resource = "C:\\Users\\"+user+"\\AppData\\Roaming\\.minecraft\\resourcepacks"
    mods= "C:\\Users\\"+user+"\\AppData\\Roaming\\.minecraft\\mods"
    with os.scandir(resource) as ficheros:
        for fichero in ficheros:
            dir = fichero.name
            if 'Xray' in fichero.name or 'xray' in fichero.name or 'X ray' in fichero.name or 'x ray' in fichero.name or 'ray' in fichero.name or 'ray' in fichero.name or 'XRay' in fichero.name:
                try:
                    os.remove("C:\\Users\\"+user+"\\AppData\\Roaming\\.minecraft\\resourcepacks\\"+fichero.name)
                    os.rmdir("C:\\Users\\"+user+"\\AppData\\Roaming\\.minecraft\\resourcepacks\\"+fichero.name)
                    print("deleted")
                except:
                    pass
    with os.scandir(mods) as ficheros:
        for fichero in ficheros:
            dir = fichero.name
            if 'Xray' in fichero.name or 'xray' in fichero.name or 'X ray' in fichero.name or 'x ray' in fichero.name or 'ray' in fichero.name or 'ray' in fichero.name or 'XRay' in fichero.name:
                try:
                    os.remove("C:\\Users\\"+user+"\\AppData\\Roaming\\.minecraft\\mods\\"+fichero.name)
                    os.rmdir("C:\\Users\\"+user+"\\AppData\\Roaming\\.minecraft\\mods\\"+fichero.name)
                    print("deleted")        
                except:
                    pass


def hash_file(filename):
    import hashlib
    h = hashlib.sha1()

    with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
    hash = h.hexdigest()
    return hash

    

def launcher():
    
    import os
    os.system('C:\\Users\\titi\\Desktop\\minecraft_launcher\\output\\portablemc.exe start')