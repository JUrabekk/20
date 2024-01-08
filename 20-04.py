#На вход вашей программы передаётся текст файла с программой на языке Python.
#Ваша задача – посчитать и напечатать число строк кода, содержащих только
#комментарий (т.е. в которых первый непробельный символ – символ решётки #).

#import sys
#data = sys.stdin.read()
#count = list(map(lambda x: x.lstrip().startswith("#"), data.split("\n"))).count(True)
#print(count)

import sys
data = sys.stdin.read()
count = list(map(lambda x: x.lstrip().startswith("#"), data.split("\n"))).count(True)
print(count)