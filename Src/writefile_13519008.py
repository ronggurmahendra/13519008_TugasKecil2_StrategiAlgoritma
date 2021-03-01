"""
Nama : Ronggur Mahendra Widya Putra
NIM : 13519008
"""
def writefile(fileout,stringout): #write file
    f = open(fileout, "w")
    f.write(stringout)
    f.close()