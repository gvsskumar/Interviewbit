# Create a generator pipeline for large file processing
def read_lines(file_path):
    with open('./sample.txt','r') as f:
        for line in f:
            yield line.strip()

def filter_lines(lines,keyWord):
    for line in lines:
        if keyWord in line:
            yield line

def tranformation(leines):
    for line in leines:
        yield line.lower()

def addNumber(lines):
     for i,line in enumerate(lines,1):
         yield f"{i} : {line}"

pipeline =addNumber(tranformation(filter_lines(read_lines('./sample.txt'),'ERROR')))
for line in pipeline:
    print(line)


