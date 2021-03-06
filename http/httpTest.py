#coding=utf-8

import requests
import json
import xlwt
from xlwt.Formatting import Alignment

path ='E:\Temp\out.xls'
url = 'http://192.168.47.1:60006/api/v4/clients/'

def write_xls(datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)    
    row = 0
    # 设置行高
    sheet1.row(0).height_mismatch = True
    sheet1.row(0).height = 100*20

    # 合并      
    sheet1.write_merge(0, 0, 0, len(list(datas[0][0].keys())) - 1, 'First Merge')

    
    tittlStyle = xlwt.XFStyle()
    al = xlwt.Alignment()
    # 居中
    al.horz = 2
    al.vert = 1
    tittlStyle.alignment = al

    # 字体格式
    tittleFont = xlwt.Font()
    tittleFont.name = '黑体'
    tittleFont.height = 20 * 20
    tittleFont.bold = True
    tittlStyle.font = tittleFont
    
    # 边框
    borders = xlwt.Borders()
    # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
    # 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    tittlStyle.borders = borders

    sheet1.write(row, 0, "远程设备信息列表", tittlStyle)
    

    row += 1
    # row0 = [u'设备标识',u'用户名',u'设备IP',u'设备端口',]

    contentStyle = xlwt.XFStyle()
    contentStyle.borders = borders

    row0 = list(datas[0][0].keys())
    for i in range(len(row0)):
        sheet1.write(row,i,row0[i], contentStyle)
    row += 1   
    for data in datas:       
        for d in data:
            col = 0
            for value in d.values():
                sheet1.write(row, col, value, )
                col += 1
            row += 1

        
    f.save(path)
    


if __name__ == '__main__':

    page, limit = 1,100
    hasnext = True

    #url = 'http://120.24.223.61:28050/api/v4/clients/'
    datas = []
    while (hasnext):
        params = {"_page":page,"_limit":limit}
        headers = {"Authorization":"Basic YWRtaW46cHVibGlj"} #admin/public
        #headers = {"Authorization":"Basic YWRtaW46Q2V0NDU2NyQlXiY="} #admin/Cet4567$%^&
        r = requests.get(url=url,params=params,headers = headers)
        js = json.loads(r.text)
        page += 1
        hasnext = len(datas) < js['meta']['count']
        datas.append(js['data'])
    write_xls(datas) 
    print("pass")