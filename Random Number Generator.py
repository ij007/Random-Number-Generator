import time 
import matplotlib.pyplot as plt

def rand_bit():
    a = 918273645210143527345039683
    b = 1564376381919238011039485760361
    x = int((time.time()*(10**7))%1000000)
    n = 817219445776617222361364238353
    
    fig, ax = plt.subplots()
    l = []
    index= []
    for i in range(1000):
        
        x = ((a*x)+b) % n
        
        l.append(x) #for random number--->l.append(x)
        index.append(i)
        
    plt.plot(index, l)
    plt.show()
    
   
    
rand_bit()
