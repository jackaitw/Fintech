import os
import subprocess

current_dir = os.getcwd()
#ali_basename = os.listdir(current_dir)
ft = ""
dbname = ''
mdf_list = []
ldf_list = []
print(current_dir)
f = open("attach.sql","w+")
filenames = os.listdir()
for filename in filenames:
        upname = filename.upper()
        if upname.endswith('.MDF'):
            dbname=upname.split('.MDF')            
            mdf_list.append(dbname[0])
        elif upname.endswith('.LDF'):            
            ldf_list.append(upname)
        else:
            print("未處理的檔名如下:"+ upname)
#db.sort(key=None,reverse=True)
#print(mdf_list,ldf_list)
mdf_len = len(mdf_list)
ldf_len = len(ldf_list)
#print(mdf_len)
a = 'USE [master]\nGO\n'
f.write(a)
if mdf_len == ldf_len:
    for db in range(0,mdf_len):
        ft = "CREATE DATABASE ["+ mdf_list[db] + "] ON (FILENAME = N'" + current_dir +"\\" + mdf_list[db] + ".MDF'),(FILENAME = N'" + current_dir + "\\" + ldf_list[db] + "') FOR ATTACH" + "\n" + "GO\n"
        f.write(ft)
else:
    f.write("MDF的檔案數量與LDF的檔案數量不符合，請檢察檔案後再度執行本程式，謝謝!")
f.close()
#sql_cmd = "sqlcmd  -i " + current_dir + "\attach.sql"
os.system("sqlcmd  -i " + current_dir + "\select.sql")

