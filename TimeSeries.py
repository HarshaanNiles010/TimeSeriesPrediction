import threading
import concurrent.futures
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import math
Time1 = []
Output = []
def Display(Itr,Time):
    plt.plot(Itr,Time)
    plt.show()
# Naive Case for calculating the sum
def calcTotal(Data):
    sum = 0
    for i in range(len(Data)):
        sum += Data[i]
    return sum
    #print(f'The sum generated is {round(sum,2)}')

# Recursive way to calculate the total
def RecCalcTotal(Data):
    if(len(Data) == 1):
        return calcTotal(Data)
    else:
        half = int(len(Data) / 2)
        lower = RecCalcTotal(Data[:half])
        upper = RecCalcTotal(Data[half:])
# Iteratively spliting the list into half
#def ItrCalcTotal(Data):
#    while(1):
#        if(len(Data) == 1):
#            calcTotal(Data)
#            break
#        else:


def Activation(Data):
    return [(1/(1+np.exp((-1)*(Data[i])))) for i in range(1,len(Data))]


def gen_uniq_floats(lo, hi, n):
    outed = []
    out = np.empty(n)
    needed = n
    while needed != 0:
        arr = np.random.uniform(lo, hi, needed)
        uniqs = np.setdiff1d(np.unique(arr), out[:n-needed])
        out[n-needed: n-needed+uniqs.size] = uniqs
        needed -= uniqs.size
    np.random.shuffle(out)
    return out.tolist()


def Test(Itr):
    option = 1
    print("Please Choose from the two options")
    print("option 1: Normal addition")
    print("option 2: Recursive Addition")
    option = int(input())
    # Testing method
    Itr = Itr + 1
    startTime = time.perf_counter()
    for i in range(1,Itr):
        TestData = []
        #Generate the test data
        TestData = gen_uniq_floats(-10*i, 10*i, 100)
        for j in range(len(TestData)):
            TestData[j] = round(TestData[j],2)
        #Start the timer
        #Pass the data to the function
        if(option == 1):
            calcTotal(TestData)
        elif(option == 2):
            RecCalcTotal(TestData)
        else:
            print("No option was selected")
        # Stop the timer
        endTime = time.perf_counter()
        #Print the total number of iterations with the time taken
        #print(f'iteration number: [{i}]. Total time taken {round(endTime-startTime,2)}')
        Time1.append(round(endTime-startTime,2))
    # Displaying the total performance of the addition performed
    Time2 = np.asarray(Time1,dtype = np.float32)
    Iterations0 = [i for i in range(1,Itr)]
    Iterations1 = np.asarray(Iterations0,dtype=np.int)
    plt.plot(Time2,Iterations1)
    plt.show()
    # Display the time complexity
    #Display(Itr, Time)


Test(100000000)
