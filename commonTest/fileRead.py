print("hello start")

local_path = 'E:\\code\\vscode\\commonTest\\'
text_path = local_path + 'readFile.txt'

def read_file(file_path):
    file = open(file_path,'r',encoding='utf-8')
    data = []
    file_data = file.readlines()
    for line in file_data:
        temp_row = line.split(' ')
        temp_row = line.split('\t')
        temp_row[-1] = temp_row[-1].replace('\n','')
        data.append(temp_row)
    return data

if __name__ == "__main__":
    data = read_file(text_path)
    print(data)

    #----- 输出代码


    for row in data:       
         comment = "//" + row[0] # 注释
         if 'float' in row[1]:
            chose_array = 'bytes2 = steam.read(inpute,0,bytes2.lenth);' # choose byte_array
            encode = 'dataModel.'+row[3]+'= ConvertUtils.ConvertToFloat(bytes2)'  # choose encoder
            print()
            print(comment)
            print(chose_array)
            print(encode)
            

   
