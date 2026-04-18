       
def findDuplicatelines(file_path):
    duplicate = {} 

    with open(file_path,'r',encoding='utf-8') as f:
        for index,line in enumerate(f):
            if line in duplicate:
                duplicate[line] +=1
                print(f"{index}:{line}")
            else:
                duplicate[line] =1 
           
print(findDuplicatelines('./mytext.txt'))