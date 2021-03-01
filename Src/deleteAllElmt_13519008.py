"""
Nama : Ronggur Mahendra Widya Putra
NIM : 13519008
"""
def deleteAllElmt(arr,elmt): #mendelete semua elmt yang bernilai elmt pada matriks
    for k in range(len(arr)):
        arr[k] = [s for s  in arr[k] if s != elmt]
        #print("arr[k] = ",arr[k])
    arr = [s for s in arr if s != []]
    return arr