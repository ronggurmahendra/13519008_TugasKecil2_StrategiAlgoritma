"""
Nama : Ronggur Mahendra Widya Putra
NIM : 13519008
"""
from toromawi_13519008 import  *
from writefile_13519008 import  *  
from deleteAllElmt_13519008 import  *  
from fileinput_13519008 import  * 
global Result 

filein = input("Masukan Nama File Masukan: ")
arr = inputfile(filein) # mengambil masukan file
Result = []

while(len(arr)> 0):
    i = 0    
    tobeiterated = [] # inisialisasi array tobeiterated
    found = False
    while(i < len(arr)):
  
        if(len(arr[i]) == 1): #cari kelas yang semua kelas preqnya sudah terpenuhi
            tobeiterated.append(arr.pop(i)[0])
            found = True
        else:
            i = i+1
    if(not(found)): #solusi tidak ada karena ada kasus dimana kelas tidak mungkin diambil
        break
    for j in range(len(tobeiterated)):
        arr = deleteAllElmt(arr,tobeiterated[j]) #hilangkan kelas yang sudah diambil
    Result.append(tobeiterated)
    #print("tobeiterated = ",tobeiterated)
    #print("arr = ", arr)
#membuat output
stringout = ''
if(found): 
    for i in range(len(Result)):
        temp = ''
        for j in range(len(Result[i])):
            temp += Result[i][j]
            if(j != len(Result[i])-1):
                temp += ','
        print("semester",toromawi(i+1), ":",temp)
        stringout += "semester " 
        stringout += toromawi(i+1) 
        stringout += " : " 
        stringout += temp
        stringout += '\n'
else: #solusi tidak ditemukan
    stringout += 'solution not found'
    print(stringout)
fileout = input("Masukan Nama File Keluaran: ")
writefile(fileout,stringout) #write file
