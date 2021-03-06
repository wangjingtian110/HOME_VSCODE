
class SoeInfo:
    header_class = ''
    sub_class = ''
    two_pos = ''
    value = ''
    describe = ''

    def __init__(self, header_class, sub_class, two_pos, value, describe):
        self.header_class = header_class
        self.sub_class = sub_class
        self.two_pos = two_pos
        self.value = value
        self.describe = describe


def notesRemain(codeStr, data_info):
    if (data_info.describe == '预留' or data_info.describe == '保留') and len(codeStr) > 0:
        codeStr = '\t//{}'.format(codeStr)
    return codeStr

def createHashTable(data_info):
    codeStr = ''
    if data_info.header_class != 'FF':
        print()
        print('*******{}*****'.format(data_info.header_class))
        print()
    if data_info.two_pos == '0':
        codeStr = 'hashTable.put({}, "{}");'.format(data_info.sub_class, data_info.describe)

    codeStr = notesRemain(codeStr, data_info)

    print(codeStr)
    return True


def createTowPosHashTable1(data_info,dpi):
    codeStr = ''
    if data_info.header_class != 'FF':
        print()
        print('*******{}*****'.format(data_info.header_class))
        print()
    if '/' in data_info.two_pos:
        
        desc_info = data_info.describe.split('/')

        if (dpi):
            codeStr = 'hashTable.put({}, "{}");'.format(data_info.sub_class, desc_info[0])
        else:
            codeStr = 'hashTable.put({}, "{}");'.format(data_info.sub_class, ''.join(desc_info) )
        
    codeStr = notesRemain(codeStr, data_info)
    print(codeStr)
    return True

def createTowPosHashTable(datas):
    opperCount = 0
    hashTables = {}
    current_header = 'FF'
    for data_info in datas:
        if data_info.header_class != 'FF':
            current_header = data_info.header_class
        if '/' in data_info.two_pos:
            dpi1,dpi2 = data_info.two_pos.split('/')
            dpi1_value, dip2_value = data_info.describe.split('/')

            temp_dict = {}
            if not hashTables.__contains__(current_header):
                temp_dict = {dpi1:[], dpi2:[]}                
            else:
                temp_dict = hashTables[current_header]

            codeStr = 'hashTable.put({}, "{}");'.format(data_info.sub_class, dpi1_value)
            temp_dict[dpi1].append(codeStr)

            codeStr = 'hashTable.put({}, "{}");'.format(data_info.sub_class, '{}{}'.format(dpi1_value,dip2_value))
            temp_dict[dpi2].append(codeStr)

            hashTables[current_header] = temp_dict

            opperCount += 1

    for header,dpi_tables in hashTables.items():
        print('*****')
        print(header)
        print('*****')
        for dpi,values in dpi_tables.items():
            print("-----DPI:{}".format(dpi))
            for value in values:
                print(value)
            print()
    return opperCount



        
    



file = open('E:\\code\\vscode\\codeGene\\testGene.txt','r', encoding='utf-8')
data = []
isFirstLine = True
hasShiftColumn = False
count = 0
opperCount = 0
#current_header_class = ''
invalid_header_class = 'FF'
for line in file.readlines():

    # 过滤标题行
    if (isFirstLine):
        isFirstLine = False
        #if '双位置'  in line:
            #hasShiftColumn = True
        continue
    
    # 过滤偏移列字段 没有用到
    temp = line.split()
    if hasShiftColumn:
        temp = temp[1:]
     
    temp[-1] = temp[-1].replace('\n', "")
    if ('注' in temp[-1]):
        temp = temp[0:-1]
    
    #得到类似---- {  类     子类	双位置  	记 录 值	描述 }   的字样
    # 记录当前大类
    if len(temp) < 5:
        temp.insert(0, invalid_header_class)
    else:
        #current_header_class = temp[0]
        pass
    
    data_info = SoeInfo(temp[0], temp[1], temp[2], temp[3], temp[4])

    #创建hashtable部分数据
    #actived = createHashTable(data_info)

    #创建包含双位信息的hashtable
    data.append(data_info)
    #actived = createTowPosHashTable1(data_info,0)

    #data.append('\t'.join(temp))
    #创建数据DO部分的代码
    #actived = createField(data_info)

    #创建Analysis部分代码
    #actived = createStreamField(data_info, 'basicPowerData')

    #opperCount += 1 if actived else 0
    count += 1

opperCount = createTowPosHashTable(data)



print()
print()
print("生成了{}条数据".format(count))
print("操作了{}条数据".format(opperCount))


