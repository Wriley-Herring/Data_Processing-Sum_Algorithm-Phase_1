'''
Created on Jun 13, 2020

@author: wrileyherring
'''

#Declare number of input files
fileNums = ['1','2','3','4','5']

#Perform the Sum of K algorithm on all files
for num in fileNums:
    
    #Declare Input and Output Files
    filenameIn = 'in'+num+'.txt'
    filenameOut = 'out'+num+'.txt'
    
    #Read input file into algorithm
    f = open(filenameIn,'r')
    lines = f.readlines()
    target = int(lines[1])
    outputList = lines[2]
    listOfNumbers = lines[2].split(" ")
    listOfNumbers.pop()
    
    #declare answer variables
    answer1 = 0
    answer2 = 0
    
    #iterate through list to see if sum values exist
    for num1 in listOfNumbers:
        
        for num2 in listOfNumbers:
            
            #check if the two selected values sum is equal to target
            if (int(num1) + int(num2)) == target:
                answer1 = num1
                answer2 = num2
                break
                
    #check if the algorithm found an answer
    
    #If it did not then write a no response to the output file   
    if answer1 == 0 and answer2 ==0:
        outputFile = open(filenameOut,"w+")
        outputFile.write(str(target))
        outputFile.write('\n')
        outputFile.write(outputList)
        outputFile.write('No')
        
    #if it did find an answer then write a yes response to the output file
    else:
        outputFile = open(filenameOut,"w+")
        outputFile.write(str(target))
        outputFile.write('\n')
        outputFile.write(outputList)
        outputFile.write('Yes')
        outputFile.write('\n')
        outputFile.write(answer1+'+'+answer2+'='+str(target))