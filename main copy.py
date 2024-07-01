import matplotlib.pyplot as plt  # tests
import networkx as nx
import time
import random

print("Вариант №16 ИУ4-23Б Матвеев И.С.\n")
print("Визуализация графа, заданного списком рёбер")
print("Удаление вершин заданного ребра")
print("Пирамидальная сортировка степеней вершин")

class graf(): # класс создает объект граф с набором методов 
    def __init__(self,allvertex, edgess, connect_vertex):
        self.vertex = allvertex
        self.edges = edgess
        self.connect = connect_vertex
    def output(self):
        print(f'Вершины: {self.vertex}')
        print(f'Ребра: {self.edges}')
        print(f'Связь вершин: {self.connect}')

def read_txt(name_of_txt): # считывает данные из файла в строку
    string=""
    for i in open(name_of_txt):
        string+=i
    return string

def split(string): # разделяет строку по пробела и энтарам 
    list_before= string.split("\n")
    del list_before[-1]
    
    for i in range(0,len(list_before)):
        list_before[i] = list_before[i].split(" ")
    return list_before

def edges(list_before): #  преобразует лист бефо в лист афтер 
    list1 = []
    list2 = []
    for i in range(0,len(list_before)):
        if(len(list_before[i])==2):
            list1.append(int(list_before[i][0]))
            list2.append(int(list_before[i][1]))
    print(len(list_before))
    list_after=list(zip(list1,list2))
    return list_after

# def try_find_vertex(list_after, vеrtex1, vertex2):
#     flag=0
#     while flag==0:
#         for i in range(0,len(list_after)):
#             if vеrtex1 in list_after[i]:
#                 if vertex2 in list_after[i]:
#                     flag=1
#         if flag==0:
#             print("Введённого ребра НЕ СУЩЕСТВУЕТ\n")
#             print("Список рёбер:")
#             for i in range(0,len(list_after)-1, 2):
#                 print(list_after[i], list_after[i+1])
#                 if i == len(list_after)-3 :
#                     print(list_after[len(list_after)-1])
#             print()
#             vеrtex1, vertex2 = map(int, input("Задайте ребро: ").split())    
#     vertex12=[vеrtex1, vertex2]
#     print()
#     return vertex12

# def del_vertex(list_after, vertex12):
#     i=0
#     flag=0
#     vеrtex1=vertex12[0]
#     vertex2=vertex12[1]
#     while i<len(list_after):
#         for k in 0,1:
#             if (list_after[i][k]==vеrtex1) or (list_after[i][k]==vertex2):
#                 del list_after[i]
#                 flag=1
#                 break
#         if flag==0:
#             i+=1
#         else:
#             flag=0

#     return list_after

def vertex(list_after): # формирует список вершин (кроме одиночных)
    listvertex =[]
    for i in range(0,len(list_after)):
        listvertex.append(list_after[i][0])
        listvertex.append(list_after[i][1])
    return listvertex

def alonevertex(list_before): # формирует список одиночных вершин
    alonev = []
    for i in range(0,len(list_before)):
        if(len(list_before[i]) == 1 ):
            alonev.append(int(list_before[i][0]))
    return alonev

def allvert(listvertex,alonev): # формирует список всех вершин 
    for i in range(0,len(alonev)):
        listvertex.append(alonev[i])
    return list(set(listvertex))

def connect_of_vertex(list_after,allvertex):
    connect_vertex={}
    list_of_vertex=[]
    for i in allvertex:
        for k in range(0,len(list_after)):
            if i in list_after[k]:
                list_of_vertex.append(list_after[k][0])
                list_of_vertex.append(list_after[k][1])
                list_of_vertex.remove(i)
        if len(list_of_vertex)==0:
            set_of_vertex={}
            connect_vertex[i]=set_of_vertex
            list_of_vertex=[]
        else:
            set_of_vertex=set(list_of_vertex) 
            connect_vertex[i]=set_of_vertex
            list_of_vertex=[]
    return connect_vertex

#функция создаёт список степеней вершин
def list_degree(connect_vertex):
    list_of_degree=[]
    for i in connect_vertex.keys():
        list_of_degree.append(len(connect_vertex[i]))
    return list_of_degree

def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1
 
def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)

def main():

    string = read_txt("two_var_txt/run1.txt")

    list_before = split(string)
    list_after = edges(list_before)
    edgess = list_after

    # print('\nСписок рёбер: ')
    # for i in range(0,len(list_after)-1, 2):
    #     print(list_after[i], list_after[i+1])
    #     if i == len(list_after)-3 :
    #         print(list_after[len(list_after)-1])

    # vеrtex1, vertex2 = map(int, input("\nЗадайте ребро: ").split())

    # vertex12 = try_find_vertex(list_after, vеrtex1, vertex2)
    # list_after = del_vertex(list_after, vertex12)

    listvertex =  vertex(list_after)
    alonev = alonevertex(list_before)

    allvertex = allvert(listvertex,alonev)

    connect_vertex=connect_of_vertex(list_after,allvertex) 

    list_of_degree = list_degree(connect_vertex)

    G = nx.Graph()
    exgraf = graf(allvertex, list_after, connect_vertex)
    G.add_nodes_from(exgraf.vertex)
    G.add_edges_from(exgraf.edges)

    exgraf.output()

    list_of_degree=[]
    for i in range(0,2*10**6):
        list_of_degree.append(random.randint(0, 10))

    start_time = time.perf_counter()
    heapsort(list_of_degree)
    end_time = time.perf_counter()


    # print('\nОтсортированный списк степеней вершин:', list_of_degree)

    print("Время сортировки:", (end_time - start_time)*1000, "мс")
    
    nx.draw(G, with_labels=1)
    plt.show()

main()