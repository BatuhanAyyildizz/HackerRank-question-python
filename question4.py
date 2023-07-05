# girilen sayıya kadan olan ifadelerin 0'dan başlayıp karesini alma

if __name__ == '__main__':
    n = int(input())
    k=[]
    i=0
    while i < n :
        k.append(i*i)
        print(k[i])
        i+=1