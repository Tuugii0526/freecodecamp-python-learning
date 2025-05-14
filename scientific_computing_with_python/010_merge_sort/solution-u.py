# [start:stop:step]
def merge(list1,list2):
    list1Length=len(list1)
    list2Length=len(list2)
    merged=[]
    i=0
    j=0
    while i<list1Length and j < list2Length :
        if list1[i]<list2[j]:
            merged.append(list1[i])
            i+=1
        else:
            merged.append(list2[j])
            j+=1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged
def mergeSort(elements):
    if  len(elements)<=1:
        return elements
    length=len(elements)
    mid=length//2
    list1=elements[:mid]
    list2=elements[mid:]
    sortedList1=mergeSort(list1)
    sortedList2=mergeSort(list2)
    mergedList=merge(sortedList1,sortedList2)
    return mergedList
print('mergeSort:',mergeSort([2,1,3,9,0,8,2]))