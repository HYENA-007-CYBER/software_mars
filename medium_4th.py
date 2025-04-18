file_path = "log.txt"  # Replace with desired file path

with open(file_path, "r") as file:
    data = list(map(int, file.readline().strip().split(",")))
print(data)


size= 3 # declaring globally (Can easily change here)
import numpy as np#for standard deviation

def muchiko_filter(data, size):# getting average
    muchiko = []  
    for i in range(len(data) - size + 1):
        muchiko.append(sum(data[i:i+size]) // size) 
    return muchiko
m = muchiko_filter(data,size)
print("muchiko_result : ",m)  
def sanchiko_filter(data, size):# getting median
    sanchiko = []  
    for i in range(len(data) - size + 1):
        sanchiko.append(sorted(data[i:i+size])[size//2])
    return sanchiko
s = sanchiko_filter(data,size)
print("sanchiko_result : ",s)  
hybrid_result_1 = sanchiko_filter(m,size)
print("Hybrid Filtered Data (Muchiko then Sanchiko) : ", hybrid_result_1)
hybrid_result_2 = muchiko_filter(s,size)
print("Hybrid Filtered Data (Sanchiko then Muchiko) : ", hybrid_result_2)
std_original=np.std(data)#USING STANDARD DEVIATION FROM NUMPY
std_m=np.std(m)
std_s=np.std(s)
std_h1=np.std(hybrid_result_1)
std_h2=np.std(hybrid_result_2)
#TO CALCULATE BY HOW MUCH PERCENT IT FILTERS THE DATA
def per_red(x):
    return ((std_original-x)/std_original)*100
m_per=per_red(std_m)
s_per=per_red(std_s)
h1_per=per_red(std_h1)
h2_per=per_red(std_h2)
#TO PRINT WHICH FILTER IS BEST FOR THE DATASET
if ((m_per>=s_per)and(m_per>=h1_per)and(m_per>=h2_per)):
    print("MUCHIKO FILTER IS BEST")
if ((s_per>=m_per)and(s_per>=h1_per)and(s_per>=h2_per)):
    print("SANCHIKO FILTER IS BEST")
if ((h1_per>=s_per)and(h1_per>=m_per)and(h1_per>=h2_per)):
    print("Hybrid Filtered Data (Muchiko then Sanchiko) IS BEST")
if ((h2_per>=h1_per)and(h2_per>=m_per)and(h2_per>=s_per)):
    print("Hybrid Filtered Data (Sanchiko then Muchiko) IS BEST")










