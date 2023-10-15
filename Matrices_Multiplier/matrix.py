import time
import multiprocessing
from multiprocessing import Process as ps
import numpy as np
import math


def createRandomMatrix(rows,collumn):
    newM=np.random.uniform(low=0, high=100, size=(rows,collumn))
    newM=newM.astype(int)
    return newM

def Matrices_Multiplier_Async_calculator(matrix_a:list,matrix_b:list,start_index,end_index):
    result=[]
    for row in matrix_a:
        row_res=[]
        for c in range(start_index,end_index+1):
            temp_column_res=0
            for r in range(0,len(matrix_b)):
                temp_column_res+=row[r]*matrix_b[r][c]
            row_res.append(temp_column_res)
        result.append(row_res)
    return result

def Matrices_Multiplier_AsyncRunColumnDivider(shared_memory:dict,matrix_a:list,matrix_b:list,start_index,end_index,PL,pid):
    if(end_index-start_index+1<=PL):
        shared_memory[pid]=Matrices_Multiplier_Async_calculator(matrix_a,matrix_b,start_index,end_index)
    else:
        Col_res=multiprocessing.Manager().dict()
        sep=int((end_index-start_index+1)/2)
        p1=ps(target=Matrices_Multiplier_AsyncRunColumnDivider,args=(Col_res,matrix_a,matrix_b,start_index,sep,PL,1))
        p2=ps(target=Matrices_Multiplier_AsyncRunColumnDivider,args=(Col_res,matrix_a,matrix_b,sep+1,end_index,PL,2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        temp=Col_res[1]
        temp2=Col_res[2]
        for i in range (0,len(matrix_a)):
            temp[i].extend(temp2.pop(0))
        shared_memory[pid]=temp
        del Col_res

def Matrices_Multiplier_AsyncRunRowDivider(shared_memory:dict,matrix_a:list,matrix_b:list,PL,pid):
    if(len(matrix_a)<=PL):
        Row_res=multiprocessing.Manager().dict()
        Matrices_Multiplier_AsyncRunColumnDivider(Row_res,matrix_a,matrix_b,0,len(matrix_b[0])-1,PL,0)
        shared_memory[pid]=Row_res[0]
        del Row_res
    else:
        P_res=multiprocessing.Manager().dict()
        sep=int(len(matrix_a)/2)
        p1list=matrix_a[0:sep]
        p2list=matrix_a[sep+1:len(matrix_a)]
        p1=ps(target=Matrices_Multiplier_AsyncRunRowDivider,args=(P_res,p1list,matrix_b,PL,1))
        p2=ps(target=Matrices_Multiplier_AsyncRunRowDivider,args=(P_res,p2list,matrix_b,PL,2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        #print(P_res)
        result=P_res[1]
        result.extend(P_res[2])
        shared_memory[pid]=result
        del P_res
                 
def parallel_multiply_matrices(matrix_a:list,matrix_b):
    shared_memory=multiprocessing.Manager().dict()
    PT=2
    PTT=int(math.sqrt(multiprocessing.cpu_count()))
    if PTT > PT:
        PT=PTT
    PL = int(len(matrix_a)/(PT-1))
    Start_time=time.time()
    Matrices_Multiplier_AsyncRunRowDivider(shared_memory,matrix_a,matrix_b,PL,0)
    Stop_time=time.time()
    exe_time=Stop_time-Start_time
    
    #print("\n\nmultiply result = ",shared_memory[0])
    print("\n\nExcution time:", exe_time,"s\n\n")
    del shared_memory
    
    
def Matrixes_Multiplier_SyncRun(matrix_a,matrix_b):
    matrix_full=[]
    for row in matrix_a:
        matrix_row=[]
        for c in range(0,len(matrix_b[0])):
            temp_column_res=0
            for r in range (0,len(matrix_b)):
                temp_column_res+=row[r]*matrix_b[r][c]
            matrix_row.append(temp_column_res)
        matrix_full.append(matrix_row)
    return matrix_full
def Matrixes_Multiplier_SyncFullProcess(matrix_a,matrix_b):
    Start_time=time.time()
    result=Matrixes_Multiplier_SyncRun(matrix_a,matrix_b)
    Stop_time=time.time()
    exe_time=Stop_time-Start_time
    #print("\n\nmultiply result = ",result)
    print("\n\nExcution time:", exe_time,"s\n\n")
    
def main():
    thelista=createRandomMatrix(700,700).tolist()
    thelistb=createRandomMatrix(700,700).tolist()
    #print("list a = ",thelista)
    #print("list b = ",thelistb)
    #Matrixes_Multiplier_SyncFullProcess(thelista,thelistb)
    parallel_multiply_matrices(thelista,thelistb)

if __name__=="__main__":
    main()


    
    