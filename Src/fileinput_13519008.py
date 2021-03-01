"""
Nama : Ronggur Mahendra Widya Putra
NIM : 13519008
"""
def inputfile(filename):#input file
    #input file
    text_file = open(filename, "r")
    lines = text_file.readlines()
    arr = []
    for i in range(len(lines)):
        #arr[i].append(lines[i].split(','))
        #print(lines[i].replace('\n','').replace('.','').replace(' ','').split(','))
        temp = lines[i].replace('\n','').replace('.','').replace(' ','').split(',')
        arr.append([])
        for j in range (len(temp)):
            #print (arr)
            
            arr[i].append(temp[j])
        #print(lines[i].replace('\n','').replace('.',''))
    #print (arr)
    #print (len(arr))
    text_file.close()
    return arr