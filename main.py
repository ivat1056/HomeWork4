import matplotlib.pyplot as plt
import networkx as nx

print("Вариант №16 ИУ4-23Б Матвеев И.С.")
print("Визуализация графа, заданного списком рёбер")

class graf(): # класс создает объект граф с набором методов 
    def __init__(self,allvertex,edgess):
        self.vertex = allvertex
        self.edges = edgess
    def output(self):
        print(f'Вершины: {self.vertex}')
        print(f'Ребра: {self.edges}')

def read_txt(name_of_txt): # считывает данные из файла в строку
    string=""
    for i in open(name_of_txt):
        string+=i
    return string

def split(string): # разделяет строку по пробела и энтарам 
    list_before= string.split("\n")
    del list_before[-1]

    # vеrtex1, vertex2 = map(int, input("Задайте ребро: ").split())

    # i=0
    # while i<len(list_before):
    #     if (list_before[i][0]==str(vеrtex1)) or (list_before[i][1]==str(vertex2)):
    #         del list_before[i]
    #     i+=1
    
    for i in range(0,len(list_before)):
        list_before[i] = list_before[i].split(" ")
    return list_before

def edges(list_before, vеrtex1, vertex2): #  преобразует лист бефо в лист афтер 
    list1 = []
    list2 = []
    for i in range(0,len(list_before)):
        if(len(list_before[i])==2):
            list1.append(int(list_before[i][0]))
            list2.append(int(list_before[i][1]))
    list_after=list(set(zip(list1,list2)))

    flag=0
    while flag==0:
        for i in range(0,len(list_after)):
            if vеrtex1 in list_after[i]:
                if vertex2 in list_after[i]:
                    flag=1
        if flag==0:
            print("Введённого ребра не существует")
            print("Список рёбер:")
            for i in range(0,len(list_after)):
                print(list_after[i])
            print()
            vеrtex1, vertex2 = map(int, input("Задайте ребро: ").split())

        
    i=0
    flag=0
    while i<len(list_after):
        for k in 0,1:
            if (list_after[i][k]==vеrtex1) or (list_after[i][k]==vertex2):
                del list_after[i]
                flag=1
                break
        if flag==0:
            i+=1
        else:
            flag=0

    return list_after

def vertex(list_after): # формирует список вершин (кроме одиночных)
    listvertex =[]
    for i in range(0,len(list_after)):
        listvertex.append(list_after[i][0])
        listvertex.append(list_after[i][1])
    return listvertex

def alonevertex(list_before, vertex1, vertex2): # формирует список одиночных вершин
    alonev = []
    for i in range(0,len(list_before)):
        if(len(list_before[i]) == 1 ):
            alonev.append(int(list_before[i][0]))
    i=0
    while i<len(alonev):
        if (alonev[i]==vertex1) or (alonev[i]==vertex2):
            del alonev[i]
        else:
            i+=1
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

def sort_degree(connect_vertex):
    # Создаем пустой список для хранения отсортированных вершин
    sorted_vertices = []
    
    # Проходим по всем вершинам
    for vertex in connect_vertex:
        # Подсчитываем количество связей каждой вершины
        degree = len(connect_vertex[vertex])
        
        # Добавляем вершину в список с учетом ее степени
        sorted_vertices.append((degree, vertex))
    
    # Сортируем список вершин, по убыванию степени
    # вызов сортировки
    # sorted_vertices.sort(key=lambda x: x[0], reverse=True)
    
    # Возвращаем список вершин, отсортированных по возрастанию степени
    return [vertex for degree, vertex in sorted_vertices]

string = read_txt("list_of_edges199.txt")

vеrtex1, vertex2 = map(int, input("Задайте ребро: ").split())

list_before = split(string)
list_after = edges(list_before, vеrtex1, vertex2)
edgess = list_after
listvertex =  vertex(list_after)
alonev = alonevertex(list_before, vеrtex1, vertex2)

allvertex = allvert(listvertex,alonev)

connect_vertex=connect_of_vertex(list_after,allvertex) 
G = nx.Graph()
exgraf = graf(allvertex, list_after)
G.add_nodes_from(exgraf.vertex)
G.add_edges_from(exgraf.edges)
exgraf.output()
print(connect_vertex)

print(sort_degree(connect_vertex))

nx.draw(G, with_labels=1)
plt.show()


# def heapify(arr, n, i):
#     # Преобразование поддерева с корнем в max-heap
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2

#     # Проверка наличия левого дочернего узла
#     if l < n and arr[i] < arr[l]:
#         largest = l

#     # Проверка наличия правого дочернего узла
#     if r < n and arr[largest] < arr[r]:
#         largest = r

#     # Перемещение элемента вверх, если он больше родительского
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]

#         # Применение heapify на перемещенном элементе
#         heapify(arr, n, largest)

# def heapSort(arr):
#     n = len(arr)

#     # Построение max-heap
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)

#     # Один за другим извлекаем элементы
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # меняем местами
#         heapify(arr, i, 0)

# # Пример использования
# arr = [12, 3, 8, 10, 5, 7]
# heapSort(arr)
# print(arr)

# # Предположим, что give_edge - это индекс заданного ребра в списке ребер.
# # Сначала найдем все вершины, смежные с этим ребром.
# edge = list_after[give_edge]
# adjacent_vertices = [edge[0], edge[1]]

# # Теперь удалим эти вершины из списка всех вершин.
# for vertex in adjacent_vertices:
#     if vertex in allvertex:
#         allvertex.remove(vertex)

# # Отсортируем оставшийся список вершин по возрастанию степени.
# # Для этого сначала создадим словарь, где ключом будет вершина, а значением - степень этой вершины.
# degree_dict = {}
# for vertex in allvertex:
#     degree_dict[vertex] = G.degree(vertex)

# # Затем отсортируем ключи этого словаря по возрастанию значения степени.
# sorted_vertices = sorted(degree_dict, key=lambda k: degree_dict[k])

# # Наконец, отсортируем оставшиеся вершины согласно полученному порядку.
# sorted_allvertex = []
# for vertex in sorted_vertices:
#     sorted_allvertex.append(vertex)

# # Обновим список вершин графа.
# allvertex = sorted_allvertex

def sort_degree(connect_vertex):
    # Создаем пустой список для хранения отсортированных вершин
    sorted_vertices = []
    
    # Проходим по всем вершинам
    for vertex in connect_vertex:
        # Подсчитываем количество связей каждой вершины
        degree = len(connect_vertex[vertex])
        
        # Добавляем вершину в список с учетом ее степени
        sorted_vertices.append((degree, vertex))
    
    # Сортируем список вершин, по убыванию степени
    sorted_vertices.sort(key=lambda x: x[0], reverse=True)
    
    # Возвращаем список вершин, отсортированных по возрастанию степени
    return [vertex for degree, vertex in sorted_vertices]

# Пример использования функции

sorted_vertices = sort_degree(connect_vertex)
print(sorted_vertices)
print(sorted_vertices)  # Вывод: [3, 2, 1]