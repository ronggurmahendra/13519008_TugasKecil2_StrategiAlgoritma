"""
Nama : Ronggur Mahendra Widya Putra
NIM : 13519008
"""
def toromawi(decimal):# fungsi untuk konvesrsi int to romawi
    result = ''
    arab = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roma = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i = 12 #mulai dari angka paling besar 'M'
    while (decimal > 0): 
        temp = decimal // arab[i] #div in dengan 1000
        decimal %= arab[i] #mod dengan 1000
        
        while(temp > 0):
            result += roma[i] #tulis hasilnya
            temp = temp -1
        i = i-1
    return result