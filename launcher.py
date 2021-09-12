import os 
import functions as fun


user = fun.getuser()


fun.scandir(user)
# print(fun.hash_file("C:\\Users\\"+user+"\\AppData\\Roaming\\.minecraft\\resourcepacks\\Xray_Ultimate_1.16_v4.1.0.zip"))
os.system('pause')

fun.launcher()