# liste islemleri

if __name__ == '__main__':
   
    def ifadeleri_kaydet(dizi):
        parcalar = dizi.split()
        ifadeler = parcalar[0:]  
        return ifadeler
        
    
    N = int(input())
    i = 0
    liste = []
    while i < N :
        M = input()
        k =  ifadeleri_kaydet(M)
        if k[0] == "insert" :
            liste.insert(int(k[1]),int(k[2]))
            
        elif k[0] == "remove" :
            liste.remove(int(k[1]))
            
        elif k[0] == "append" :
            liste.append(int(k[1]))
            
        elif k[0] == "append" :
            liste.append(int(k[1]))
            
        elif k[0] == "sort" :
            liste.sort()
            
        elif k[0] == "pop" :
            liste.pop()
            
        elif k[0] == "reverse" :
            liste.reverse()  
              
        else :
            print(liste[0:])
        i +=1
            