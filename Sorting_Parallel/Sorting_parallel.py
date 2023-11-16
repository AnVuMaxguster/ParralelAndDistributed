import numpy as np
import time
import sys

import multiprocessing
from multiprocessing import Process as Ps


def createRandomArray(lenght):
    newM=np.random.uniform(low=0, high=1000, size=(lenght))
    newM=newM.astype(int)
    return newM
def generate_array(size):
    return np.random.choice(range(size * 3), size, replace=False)

def quicksort_parallel(dalist:list,cpu_limit):
    # print("Cpu left:",cpu_limit.value)
    if cpu_limit.value<2:
        # print("before: ",dalist)
        temp=quicksort(dalist)
        dalist[:]=[]
        dalist.extend(temp)
        del temp
        # print("after: ",dalist)
    else:
        if len(dalist)>1:
            key=dalist[len(dalist)-1]
            smaller=multiprocessing.Manager().list()
            larger=multiprocessing.Manager().list()
            for i in range(0,len(dalist)-1):
                if(dalist[i]>=key):
                    larger.append(dalist[i])
                else:
                    smaller.append(dalist[i])
            result=[]
            cpu_limit.value-=2
            p1=Ps(target=quicksort_parallel,args=(smaller,cpu_limit))
            p2=Ps(target=quicksort_parallel,args=(larger,cpu_limit))
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            cpu_limit.value+=2
            if len(smaller)>=1:
                # print("smaller:", smaller)
                result.extend(smaller)
            result.append(key)
            if len(larger)>=1:
                result.extend(larger)
            dalist[:]=[]
            dalist.extend(result)
            del result




# Offical-------------------------------------------    Start

def quicksort(dalist:list):
    if len(dalist)<=1:
        return dalist
    else:
        key=dalist[len(dalist)-1]
        smaller=[]
        larger=[]
        for i in range(0,len(dalist)-1):
            if(dalist[i]>=key):
                larger.append(dalist[i])
            else:
                smaller.append(dalist[i])
        result=[]
        smaller=quicksort(smaller)
        if len(smaller)>=1:
            result.extend(smaller)
        result.append(key)
        larger=quicksort(larger)
        if len(larger)>=1:
            result.extend(larger)
        return result

  
def merging_sorted_list(lista:list,listb:list):
    i=0
    j=0
    result=[]
    while i<len(lista) and j<len(listb):
        if lista[i]<=listb[j]:
            result.append(lista[i])
            i+=1
        else:
            result.append(listb[j])
            j+=1
    result=result+lista[i:]+listb[j:]
    return result
    
def maximum_merging_couple(ml:list):
    i=0
    tuple_list=[]
    while(i+1<len(ml)):
        tuple_list.append((ml[i],ml[i+1]))
        del ml[i:i+2]
    return tuple_list

def mergesort_parallel(dalist:list,cpu_limit):
    step=len(dalist)//cpu_limit
    i=0
    rearange=[]
    while i<len(dalist):
        rearange.append(dalist[i:i+step+1])
        i+=step+1
    quickpool=multiprocessing.Pool(cpu_limit)
    quicksort_result=quickpool.map(quicksort,rearange)
    while(len(quicksort_result)>1):
        merging_list=maximum_merging_couple(quicksort_result)
        # print (merging_list,"\n\n")
        merge_result=quickpool.starmap(merging_sorted_list,merging_list)
        quicksort_result.extend(merge_result)
        # print(quicksort_result,"\n\n")
    # print(quicksort_result)
    return quicksort_result[0]
            

def parallel_sort(matrix_a):
    CPU_Cap=multiprocessing.Value('i',multiprocessing.cpu_count())
    return mergesort_parallel(matrix_a,CPU_Cap.value)
    
# Offical-------------------------------------------    End!!!



def main():
    # dalist=createRandomArray(100000).tolist()
    dalist=generate_array(100000).tolist()
    print(dalist,"\n\n\n")
    # print(quicksort(dalist))
    input("continue?")
    starttime=time.time()
    result=parallel_sort(dalist)
    endtime=time.time()
    exetime=endtime-starttime
    print (result)
    print("\n\nSORTING TIME: ",exetime)

if __name__=="__main__":
    main()
