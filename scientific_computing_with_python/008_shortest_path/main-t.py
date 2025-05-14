from colors import Colors
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    # ['A', 'B', 'C', 'D', 'E', 'F']
    distances = {node: 0 if node == start else float('inf') for node in graph}
    # {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
    paths = {node: [] for node in graph}
    # {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
    while unvisited:
        # Бид эндээс тооцоолсон зайнуудаас хамгийн бага зайтайг олно .
        current = min(unvisited, key=distances.get)
             # node нь энд 'B' г.м. 
            # distance нь энд 5
            # Энэ нь манай одоогийн зангилаанаас тухайн зангилаа, зайг node болон distance хэмээх хувьсагчид хадгалж байна . 
        for node, distance in graph[current]:
                # Хэрвээ 
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
            # print('')ыы
        unvisited.remove(current)
    print('COUNTER:',counter)
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    print('DISTANCES:',distances)
    print('PATHS:',paths)
    return distances, paths
    
# shortest_path(my_graph, 'A','F')
# step1 
# Өөрчлөгдөж болохгүй хэмээхийг та юу гэж ойлгосон вэ ? 
# Javascript хэлэнд та хувьсагчийг let болон const ашиглан хоёр янзаар заралж болдог . const оор зарласан хувьсагчид та утга оноож болохгүй бол let тохиолдолд утга оноож болохгүй . Тэгвэл Python хэлэнд let болон const байдаггүй тул юу гэсэн үг юм бол ? 
# Компьютерийн дурсамжид утгуудыг хадгалан эдгээрийн байршилыг хувьсагчид оноодог ажээ . Хэдүүлээ Python хэлэнд number хэмээх хувьсагч зарлан 5 хэмээх утга оноолоо гэж бодоё . Манай 5 хэмээх утга компьютерийн дурсамжинд нэгэн байршилаар хадгалагдсан байгаа . Тэгвэл бид number хэмээх хувьсагчид 1 тоо нэмэхэд манай анхны 5 ийг хадгалсан байршил дээр 1 ийг нэмээд уг байршилдаа 6 хэмээх утга хадгалах бус харин 6 хэмээх утгыг өөр байршилд хадгалдаг ажээ .  Үүнийг бидний байршил дахь утга хувьсдаггүй хэмээхийг илэрхийлж байгаа болуу хэмээн бодож байна . 
def experimentTupleTraversing():
    testDictionary={
        'name':[('1first','1second','1third'),('2first','2second','2third')]
    }
    for first,second,third in testDictionary['name']:
        print('first:',first)
        print('second:',second)
        print('third:',third)
experimentTupleTraversing()
def experimentMin():
    # minNumber=min(12,2,1)  minNumber is 1.
    
    
    # strings = ["apple", "banana", "cherry", "date"]
    # smallest_string = min(strings)
    # print(f"The lexicographically smallest string is: {smallest_string}")  # Output: The lexicographically smallest string is: apple
    
    students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 78},
    {'name': 'Charlie', 'score': 92}
    ]
    letters=['a','b','c']
    testDictionary={ 'a':10,"b":20,"c":5}
    least_score_letter=min(letters,key=testDictionary.get())
    print(least_score_letter)
def understandImmutableNumber():
    number=5
    print('NUMBER FIRST TIME:',number)
    number=2
    print('NUMBER SECOND TIME:',number)
def understandMutableList():
    first_list_ref=[1,2,3]
    second_list_ref=first_list_ref
    print('first list ref:',first_list_ref)
    print('second list ref:',second_list_ref)
    first_list_ref.append(2)
    print('after adding an element:')
    print('first list ref:',first_list_ref)
    print('second list ref:',second_list_ref)
def expirementList():
    mapTest={'language':'javascript',"inJavascript":"object"}
    #print(list(mapTest))
    # ['language','inJavascript']
    tupleTest=('hi','good','are','you','okay')
    # print(list(tupleTest))
    # ['hi','good','are','you','okay']
    stringTest="good"
    # print(list(stringTest))
    # ['g','o','o','d']
def experimentForLoop():
    mapTest={'language':'javascript',"inJavascript":"object"}
    #түлхүүрээр явах
    # for key in mapTest:
    #     print(key)
    
    # утгаар явах
    # for value in mapTest.values():
    #     print(value)
    
    #түлхүүр болон утгаар явах
    for key ,value in mapTest.items():
        print('key:',key)
        print('value:',value)