def printTable(n, processSize, allocation, memory_utilized, total_memory):
    print("---------------------------------------------------------") 
    print("|Process No.\t|Process Size\t|Block no.\t\t|")
    print("---------------------------------------------------------") 
    for i in range(n): 
        print("|     ",i+1,"\t|    ",processSize[i],"\t|",end="   ") 
        if allocation[i] != -1: 
            print(allocation[i] + 1,"\t\t\t|") 
        else: 
            print("Not Allocated\t|")  
    print("---------------------------------------------------------") 
    print("Memory Utilization = ",(memory_utilized/total_memory)*100,"%")

def firstFit(blockSize, m, processSize, n, total_memory): 
	allocation = [-1] * n
	memory_utilized = 0
	for i in range(n): 
		for j in range(m): 
			if blockSize[j] >= processSize[i]: 
				allocation[i] = j 
				blockSize[j] -= processSize[i]
				memory_utilized += processSize[i]
				break
	print("\nFirst Fit")
	printTable(n, processSize, allocation, memory_utilized, total_memory)

def worstFit(blockSize, m, processSize, n, total_memory): 
    allocation = [-1] * n 
    memory_utilized = 0
    for i in range(n): 
        wstIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if wstIdx == -1:  
                    wstIdx = j  
                elif blockSize[wstIdx] < blockSize[j]:  
                    wstIdx = j 
                    
        if wstIdx != -1:  
            allocation[i] = wstIdx   
            blockSize[wstIdx] -= processSize[i] 
            memory_utilized += processSize[i]
  
    print("\nWosrt Fit")
    printTable(n, processSize, allocation, memory_utilized, total_memory)
            
def bestFit(blockSize, m, processSize, n, total_memory): 
    allocation = [-1] * n  
    memory_utilized = 0
    for i in range(n):   
        bestIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if bestIdx == -1:  
                    bestIdx = j  
                elif blockSize[bestIdx] > blockSize[j]:  
                    bestIdx = j 
    
        if bestIdx != -1: 
            allocation[i] = bestIdx   
            blockSize[bestIdx] -= processSize[i] 
            memory_utilized += processSize[i]
  
    print("\nBest Fit")
    printTable(n, processSize, allocation, memory_utilized, total_memory)
    
blockSize = [100, 500, 200, 300, 600]
total_memory = sum(blockSize)
p1 = int(input("Enter size of process 1 : "))
p2 = int(input("Enter size of process 2 : "))
p3 = int(input("Enter size of process 3 : "))
p4 = int(input("Enter size of process 4 : "))
processSize = [p1, p2, p3, p4] 
m = len(blockSize) 
n = len(processSize) 

firstFit(blockSize.copy(), m, processSize.copy(), n, total_memory)
worstFit(blockSize.copy(), m, processSize.copy(), n, total_memory)
bestFit(blockSize.copy(), m, processSize.copy(), n, total_memory)