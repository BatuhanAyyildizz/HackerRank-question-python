# girilen sayıları a ve b olarak tanımlayıp a/b ifadesinin ilk önce tam kısmını döndürecek ve sonra a/b ifadesinin float kısmını döndürecek bir code dizisi
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c= float(a/b)
    def k (o):
        if int(o)> o:
            return int(o -0.4999999)
        else :
            return int(o)
    print(k(c))
    
    print(c)
