import random # generate file
file = open('two_var_txt/run1.txt','w')
for i in range (0,10):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    string = str(a) + ' ' + str(b)+'\n'
    file.write(string)
file.close()

#Удалить вершины, которые смежны с заданным ребром, и отсортировать оставшиеся по возоастанию степени вершины 