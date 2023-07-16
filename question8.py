##metindeki "&&"  ifadesini "and" ifadesine ve "||" ifadesini "or" ifadesine donusturme

import re

 
satir = int(input())
i = 0
lines =[]
while i < satir:
    line = input()
    lines.append(line)
    i +=1


k = '\n'.join(lines)
pattern = r" \|\| "
 
k = re.sub(' && ',' and ' , k)
k = re.sub(' && ',' and ' , k)
k = re.sub(pattern,' or ' , k)
k = re.sub(pattern,' or ' , k)
print(k)