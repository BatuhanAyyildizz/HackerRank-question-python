'''Neredeyse dört yılda bir 29 Şubat olarak takvime fazladan bir gün eklenir ve güne artık gün denir. Gezegenimizin güneş etrafında dönmesinin yaklaşık 365,25 gün sürdüğü gerçeğine göre takvimi düzeltir. Artık yıl artık bir gün içerir.

Miladi takvimde, artık yılları belirlemek için üç koşul kullanılır:

Yıl eşit olarak 4'e bölünebilir, aşağıdaki durumlar dışında artık yıldır:
Yıl eşit olarak 100'e bölünebilir, aşağıdaki durumlar dışında artık yıl DEĞİLDİR:
Yıl ayrıca 400'e eşit olarak bölünebilir. O zaman artık yıldır.
Bu, Miladi takvimde 2000 ve 2400 yıllarının artık yıl olduğu, 1800, 1900, 2100, 2200, 2300 ve 2500'ün artık yıl OLMADIĞI anlamına gelir.'''

def is_leap(year):
    leap = False
    if year%4==0:
        leap = True
        if year%100==0:
            
            leap =False
            if year %400==0:
                leap = True
            else :
                leap = False
        else:
            leap = True
    else:
        leap == False
             
            
    return leap

year = int(input())